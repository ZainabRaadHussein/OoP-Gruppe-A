import csv
import os
import psutil
import cv2
import pyttsx3
import statistics
import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QTabWidget, QSlider, QSpinBox,
    QFileDialog, QTableWidget, QTableWidgetItem,QMessageBox)
from PyQt6.QtCore import QTimer, Qt, QDateTime
from PyQt6.QtGui import QPixmap, QImage, QColor
import pyqtgraph as pg
from pyqtgraph import PlotWidget, BarGraphItem, TextItem
from sensor_simulator import SensorSimulator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Sensor Monitor Dashboard")
        self.setMinimumSize(1280, 800)
        self.sensor = SensorSimulator()
        self.x_data = list(range(100))
        self.y_data = [0] * 100
        self.threshold = 80
        self.dark_mode = False
        self.tts = pyttsx3.init()
        self.count_ok = 0
        self.count_near = 0
        self.count_warn = 0
        self.warn_count = 0
        self.recording = False
        self.video_writer = None

        os.makedirs("screenshots", exist_ok=True)
        os.makedirs("videos", exist_ok=True)

        self.init_ui()
        self.init_plot()
        self.init_timer()
        self.init_camera()
        self.init_menu()

    def init_ui(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(QWidget())
        main_layout = QVBoxLayout()
        self.centralWidget().setLayout(main_layout)

        # === Header ===
        header_layout = QHBoxLayout()
        self.user_label = QLabel(" Ingenieur/-in:")
        self.user_name_label = QLabel("Name")
        self.name_input = QComboBox()
        self.name_input.setEditable(True)
        self.name_input.addItems(["Alhammoud Yazan", "Alhammoud Yamen", "Hussein Zainab Raad Hussein", "Wendt Celine"])
        self.name_button = QPushButton("✅ Übernehmen")
        self.name_button.clicked.connect(self.change_name)
        self.datetime_label = QLabel()
        self.theme_button = QPushButton("🌞 Light Mode")
        self.theme_button.clicked.connect(self.toggle_theme)
        self.tab_selector = QComboBox()
        self.tab_selector.addItems(["Live-Plot", " Historie", " Statistik", " Analyse", " Kamera"])
        self.tab_selector.currentIndexChanged.connect(self.change_tab)
        self.screenshot_button = QPushButton("📸 Screenshot")
        self.screenshot_button.clicked.connect(self.take_screenshot)

        header_layout.addWidget(self.user_label)
        header_layout.addWidget(self.user_name_label)
        header_layout.addWidget(QLabel("🔧 Name ändern:"))
        header_layout.addWidget(self.name_input)
        header_layout.addWidget(self.name_button)
        header_layout.addStretch()
        header_layout.addWidget(self.datetime_label)
        header_layout.addWidget(self.tab_selector)
        header_layout.addWidget(self.screenshot_button)
        header_layout.addWidget(self.theme_button)
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.tabs)

        # === Tabs ===
        self.init_tabs()

    def init_tabs(self):
        # === Tab 0: Live-Plot ===
        self.plot_widget = PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("Live Temperatur Monitoring", color='k', size='12pt')
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setLabel('left', 'Temperatur (°C)')
        self.plot_widget.setLabel('bottom', 'Index')
        self.auto_freq_label = QLabel("🔄 CPU-Auslastung wird geprüft ...")
        self.freq_slider = QSlider(Qt.Orientation.Horizontal)
        self.freq_slider.setMinimum(1)
        self.freq_slider.setMaximum(10)
        self.freq_slider.setValue(5)
        self.freq_slider.setEnabled(False)
        self.threshold_input = QSpinBox()
        self.threshold_input.setMinimum(0)
        self.threshold_input.setMaximum(150)
        self.threshold_input.setValue(self.threshold)
        self.threshold_input.valueChanged.connect(self.update_threshold)
        self.start_button = QPushButton("▶ Start")
        self.start_button.setEnabled(False)  # Start zunächst deaktiviert
        self.stop_button = QPushButton("⏹ Stop")
        self.stop_button.setEnabled(False)   # Stop ebenfalls
        self.export_button = QPushButton(" CSV exportieren")
        self.start_button.clicked.connect(self.start_plot)
        self.stop_button.clicked.connect(self.stop_plot)
        self.export_button.clicked.connect(self.export_csv)
        self.label_avg = QLabel("Mittelwert: ---")
        self.label_max = QLabel("Max: ---")
        self.label_min = QLabel("Min: ---")
        self.status_label = QLabel("Status: Normal")
        self.status_label.setStyleSheet("color: green; font-weight: bold;")

        control_panel = QVBoxLayout()
        control_panel.addWidget(QLabel("Frequenz (Hz):"))
        control_panel.addWidget(self.freq_slider)
        control_panel.addWidget(self.auto_freq_label)
        control_panel.addWidget(QLabel("Grenzwert °C:"))
        control_panel.addWidget(self.threshold_input)
        control_panel.addWidget(self.start_button)
        control_panel.addWidget(self.stop_button)
        control_panel.addWidget(self.export_button)
        control_panel.addStretch()
        control_panel.addWidget(self.label_avg)
        control_panel.addWidget(self.label_max)
        control_panel.addWidget(self.label_min)
        control_panel.addWidget(self.status_label)

        layout0 = QHBoxLayout()
        layout0.addLayout(control_panel, 1)
        layout0.addWidget(self.plot_widget, 3)
        tab0 = QWidget()
        tab0.setLayout(layout0)

        # === Tab 1: Historie ===
        self.log_table = QTableWidget()
        self.log_table.setColumnCount(4)
        self.log_table.setHorizontalHeaderLabels(["Zeit", "Sensor", "Wert", "Status"])
        tab1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(self.log_table)
        tab1.setLayout(layout1)

        # === Tab 2: Statistik ===
        self.bar_widget = PlotWidget()
        self.bar_widget.setBackground('w')
        self.bar_widget.setTitle(" Temperatur Statistik", color='k', size='12pt')
        self.bar_widget.showGrid(x=True, y=True)
        self.bar_widget.setLabel('left', 'Wert')
        self.bar_widget.setLabel('bottom', 'Typen')
        self.stat_label = QLabel("⚙️ Statistik (aktuell)")
        self.warn_label = QLabel("🚨 Warnungen: 0")
        self.count_label = QLabel("Anzahl: ✅ Normal: 0 | ⚠️ Grenzwert Nah: 0 | 🚨 Grenzwert Warnung: 0")
        layout2 = QVBoxLayout()
        layout2.addWidget(self.bar_widget)
        layout2.addWidget(self.stat_label)
        layout2.addWidget(self.warn_label)
        layout2.addWidget(self.count_label)
        tab2 = QWidget()
        tab2.setLayout(layout2)

        # === Tab 3: Analyse ===
        self.trend_plot = PlotWidget()
        self.trend_plot.setBackground('w')
        self.trend_plot.setTitle(" Temperatur Analyse", color='k', size='12pt')
        self.trend_plot.showGrid(x=True, y=True)
        self.trend_plot.setLabel('left', 'Temperatur (°C)')
        self.trend_plot.setLabel('bottom', 'Index')
        self.trend_label = QLabel("📈 Trend: ---")
        layout3 = QVBoxLayout()
        layout3.addWidget(self.trend_label)
        layout3.addWidget(self.trend_plot)
        tab3 = QWidget()
        tab3.setLayout(layout3)

        # === Tab 4: Kamera ===
        self.camera_label = QLabel(" Live-Kamera")
        self.camera_label.setFixedSize(640, 360)
        self.kamera_name_label = QLabel(f" {self.user_name_label.text()} – Live-Überwachung")
        self.snapshot_button = QPushButton(" Snapshot speichern")
        self.snapshot_button.clicked.connect(self.save_snapshot)
        self.record_button = QPushButton(" Video aufnehmen")
        self.record_button.clicked.connect(self.toggle_recording)
        layout4 = QVBoxLayout()
        layout4.addWidget(self.camera_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout4.addWidget(self.kamera_name_label)
        layout4.addWidget(self.snapshot_button)
        layout4.addWidget(self.record_button)
        tab4 = QWidget()
        tab4.setLayout(layout4)
        self.tabs.addTab(tab0, " Live-Plot")
        self.tabs.setTabToolTip(0, "Echtzeit-Visualisierung der Sensordaten.")
        self.tabs.addTab(tab1, " Historie")
        self.tabs.setTabToolTip(1, "Tabellarische Aufzeichnung aller Messwerte.")
        self.tabs.addTab(tab2, " Statistik")
        self.tabs.setTabToolTip(2, "Max, Min, Durchschnitt und Statuszählung.")
        self.tabs.addTab(tab3, " Analyse")
        self.tabs.setTabToolTip(3, "Trendanalyse der letzten Sensordaten.")
        self.tabs.addTab(tab4, " Kamera")
        self.tabs.setTabToolTip(4, "Livebild, Snapshot, Videoaufnahme.")

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Datei")
        self.new_action = file_menu.addAction("Neu")
        self.new_action.triggered.connect(self.reset_dashboard)
        self.open_action = file_menu.addAction("Öffnen")  # war: "CSV-Ordner öffnen"
        self.open_action.triggered.connect(self.open_csv_folder)
        file_menu.addSeparator()
        self.exit_action = file_menu.addAction("Beenden")
        self.exit_action.triggered.connect(self.close)
        # Beim Start aktiv lassen
        self.set_menu_enabled(True)
    def open_csv_folder(self):
        folder = os.getcwd()  # aktuelles Projektverzeichnis
        os.startfile(folder)  # öffnet den Ordner im Explorer
    def set_menu_enabled(self, enabled):
        self.new_action.setEnabled(enabled)
        self.open_action.setEnabled(enabled)
    def reset_dashboard(self):
        reply = QMessageBox.question(
            self,
            "Bestätigung",
            "Möchten Sie wirklich alle Messwerte löschen und neu starten?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            # Stoppe ggf. laufende Messung
            if hasattr(self, 'timer'):
                self.timer.stop()
            self.y_data = [0] * 100
            self.count_ok = 0
            self.count_near = 0
            self.count_warn = 0
            self.warn_count = 0
            # Tabelle leeren
            if hasattr(self, 'log_table'):
                self.log_table.setRowCount(0)
            # Diagramme und Status zurücksetzen
            if hasattr(self, 'plot_widget'):
                self.plot_widget.clear()
            if hasattr(self, 'trend_plot'):
                self.trend_plot.clear()
            if hasattr(self, 'bar_widget'):
                self.bar_widget.clear()
            if hasattr(self, 'label_avg'):
                self.label_avg.setText("Mittelwert: ---")
            if hasattr(self, 'label_max'):
                self.label_max.setText("Max: ---")
            if hasattr(self, 'label_min'):
                self.label_min.setText("Min: ---")
            if hasattr(self, 'status_label'):
                self.status_label.setText("Status: Bereit")
                self.status_label.setStyleSheet("color: black; font-weight: normal;")
            if hasattr(self, 'warn_label'):
                self.warn_label.setText("🚨 Warnungen: 0")
            if hasattr(self, 'count_label'):
                self.count_label.setText("Anzahl: ✅ Normal 0 | ⚠️ Grenzwert Nah 0 | 🚨 Grenzwert überschritten 0")
            self.set_menu_enabled(True)
    def init_plot(self):
        self.plot_widget.clear()
    def init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.cpu_freq_timer = QTimer()
        self.cpu_freq_timer.timeout.connect(self.adjust_frequency_by_cpu)
        self.cpu_freq_timer.start(3000)
        self.datetime_timer = QTimer()
        self.datetime_timer.timeout.connect(self.update_datetime)
        self.datetime_timer.start(1000)
        self.cam_timer = QTimer()
        self.cam_timer.timeout.connect(self.update_camera)
        self.cam_timer.start(100)

    def init_camera(self):
        self.cap = cv2.VideoCapture(0)

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            img = QImage(rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)
            pix = QPixmap.fromImage(img)
            self.camera_label.setPixmap(pix.scaled(640, 360))
            if self.recording and self.video_writer:
                self.video_writer.write(cv2.resize(frame, (640, 360)))

    def adjust_frequency_by_cpu(self):
        cpu = psutil.cpu_percent()
        freq = 10 if cpu < 20 else 8 if cpu < 40 else 6 if cpu < 60 else 4 if cpu < 80 else 2
        self.timer.setInterval(int(1000 / freq))
        self.freq_slider.setValue(freq)
        self.auto_freq_label.setText(f" CPU: {cpu:.1f}% → Auto-Frequenz: {freq} Hz")

    def update_datetime(self):
        self.datetime_label.setText("🕒 " + QDateTime.currentDateTime().toString("dd.MM.yyyy – HH:mm:ss"))

    def change_name(self):
        name = self.name_input.currentText()
        self.user_name_label.setText(name)
        self.kamera_name_label.setText(f" {name} – Live-Überwachung")

        # Buttons aktivieren
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(True)

    def change_tab(self, index):
        self.tabs.setCurrentIndex(index)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        bg = 'k' if self.dark_mode else 'w'
        self.plot_widget.setBackground(bg)
        self.bar_widget.setBackground(bg)
        self.trend_plot.setBackground(bg)
        self.theme_button.setText("🌙 Dark Mode" if not self.dark_mode else "🌞 Light Mode")

    def start_plot(self):
        self.timer.start()
        self.set_menu_enabled(False)  # Menüeinträge deaktivieren

    def stop_plot(self):
        reply = QMessageBox.question(
            self,
            "Bestätigung",
            "Möchten Sie die Temperaturmessung wirklich stoppen?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.timer.stop()
            self.set_menu_enabled(True)
            self.status_label.setText("Messung gestoppt.")

    def update_threshold(self, val):
        self.threshold = val

    def update_plot(self):
        value = self.sensor.read_value()
        self.y_data = self.y_data[1:] + [value]
        self.plot_widget.clear()
        self.plot_widget.plot(self.x_data, self.y_data, pen=pg.mkPen('gray', width=2))
        for i, val in enumerate(self.y_data):
            color = QColor(255, 0, 0) if val > self.threshold + 5 else QColor(255, 165, 0) if val > self.threshold - 5 else QColor(0, 180, 0)
            self.plot_widget.plot([self.x_data[i]], [val], pen=None, symbol='o', symbolSize=6, symbolBrush=color)
        avg = statistics.mean(self.y_data)
        self.label_avg.setText(f"Mittelwert: {avg:.2f} °C")
        self.label_max.setText(f"Max: {max(self.y_data):.2f} °C")
        self.label_min.setText(f"Min: {min(self.y_data):.2f} °C")
        if value > self.threshold + 5:
            self.status_label.setText("⚠️ WARNUNG: Temperatur zu hoch!")
            self.status_label.setStyleSheet("color: red; font-weight: bold;")
            self.tts.say("Warnung, Temperaturgrenzwert überschritten")
            self.tts.runAndWait()
            status = "WARNUNG"
            self.count_warn += 1
        elif value > self.threshold - 5:
            self.status_label.setText("⚠️ Grenzwert bald erreicht")
            self.status_label.setStyleSheet("color: orange; font-weight: bold;")
            status = "Grenzwert nah"
            self.count_near += 1
        else:
            self.status_label.setText("✅ Normal")
            self.status_label.setStyleSheet("color: green; font-weight: bold;")
            status = "OK"
            self.count_ok += 1
        row = self.log_table.rowCount()
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_table.insertRow(row)
        self.log_table.setItem(row, 0, QTableWidgetItem(time_now))
        self.log_table.setItem(row, 1, QTableWidgetItem("Temperatur"))
        self.log_table.setItem(row, 2, QTableWidgetItem(f"{value:.2f} °C"))
        self.log_table.setItem(row, 3, QTableWidgetItem(status))
        self.warn_label.setText(f"🚨 Warnungen: {self.count_warn}")
        self.count_label.setText(f"Anzahl: ✅ Normal {self.count_ok} | ⚠️ Grenzwert Nah {self.count_near} | 🚨 Grenzwert überschritten {self.count_warn}")
        self.bar_widget.clear()
        metrics = [self.tr("Max"), self.tr("Min"), self.tr("Average")]
        values = [max(self.y_data), min(self.y_data), avg]
        colors = ['r', 'g', 'orange']
        bars = BarGraphItem(x=[0, 1, 2], height=values, width=1, brushes=colors)
        self.bar_widget.addItem(bars)
        for i, val in enumerate(values):
            label = ['Max', 'Min', 'Ø'][i]
            text = TextItem(f"{label}: {val:.1f}", anchor=(0.5, 0))
            text.setColor('k')
            self.bar_widget.addItem(text)
            text.setPos(i, val + 0.1)
        self.trend_plot.clear()

        # Trendlinie berechnen
        x = list(range(len(self.y_data)))
        y = self.y_data
        if len(set(y)) > 1:  # Regressionslinie nur berechnen, wenn genug Variation
            slope, intercept = statistics.linear_regression(x, y)
            trend_line = [slope * xi + intercept for xi in x]
            self.trend_plot.plot(x, trend_line, pen=pg.mkPen('r', style=Qt.PenStyle.DashLine))
            trend_direction = "steigend" if slope > 0 else "fallend" if slope < 0 else "konstant"
            self.trend_label.setText(f"📈 Trend: {trend_direction} (Steigung: {slope:.2f})")
        else:
            self.trend_label.setText("📈 Trend: konstant")

        # Originaldaten in grün
        self.trend_plot.plot(x, y, pen=pg.mkPen('g', width=2))
    def export_csv(self):
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        fname, _ = QFileDialog.getSaveFileName(
            self, "CSV speichern", f"sensor_data_{now}.csv", "CSV Dateien (*.csv)"
        )
        if fname:
            with open(fname, 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                # Benutzerzeile
                benutzer = self.user_name_label.text()
                f.write(f'Benutzer: {benutzer}\n')
                # Kopfzeile
                writer.writerow(["Zeit", "Sensor", "Wert", "Status"])
                # Datenzeilen
                for row in range(self.log_table.rowCount()):
                    zeit_item = self.log_table.item(row, 0)
                    sensor_item = self.log_table.item(row, 1)
                    wert_item = self.log_table.item(row, 2)
                    status_item = self.log_table.item(row, 3)

                    zeit = f"'{zeit_item.text()}" if zeit_item else ""
                    sensor = sensor_item.text() if sensor_item else ""
                    wert = wert_item.text() if wert_item else ""
                    status = status_item.text() if status_item else ""

                    writer.writerow([zeit, sensor, wert, status])

            self.status_label.setText(f"CSV gespeichert: {fname}")
    def save_snapshot(self):
        ret, frame = self.cap.read()
        if ret:
            path = f"screenshots/snapshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(path, frame)
            self.status_label.setText(f"Snapshot gespeichert: {path}")

    def take_screenshot(self):
        screen = QApplication.primaryScreen()
        if screen:
            path = f"screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screen.grabWindow(self.winId()).save(path)
            self.status_label.setText(f"Screenshot gespeichert: {path}")

    def toggle_recording(self):
        if not self.recording:
            path = f"videos/video_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video_writer = cv2.VideoWriter(path, fourcc, 10.0, (640, 360))
            self.recording = True
            self.record_button.setText("⏹ Aufnahme stoppen")
            self.status_label.setText(f" Aufnahme gestartet: {path}")
        else:
            self.video_writer.release()
            self.recording = False
            self.record_button.setText(" Video aufnehmen")
            self.status_label.setText(" Aufnahme gespeichert.")

app = QApplication([])
win = MainWindow()
win.show()
app.exec()