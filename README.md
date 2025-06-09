
# 📊 Sensor Monitor Dashboard

Ein interaktives PyQt6-Dashboard zur Visualisierung und Analyse simulierten Temperaturdaten mit zusätzlichen Funktionen wie Kamera-Livestream, CSV-Export, Snapshot- und Videoaufzeichnung.

---

## 🧠 Projektbeschreibung

Ziel war es, ein intuitives System zu entwickeln, das Sensordaten in Echtzeit überwacht, Grenzwertüberschreitungen erkennt, visualisiert und automatisch Benutzer*innen warnt. Erweiterte Funktionen ermöglichen statistische Auswertungen sowie multimediale Aufzeichnungen (Snapshot/Video).

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
python main.py
```

**Benötigte Bibliotheken:**
- PyQt6
- pyqtgraph
- psutil
- opencv-python
- pyttsx3

---

## 🖥️ GUI-Funktionen

### 🧭 Allgemeine GUI-Elemente
| Funktion | Beschreibung |
|----------|--------------|
| 👤 Benutzerauswahl | Dropdown zur Auswahl bzw. Eingabe des Benutzernamens |
| 🕒 Datum & Uhrzeit | Anzeige der aktuellen Systemzeit, automatische Aktualisierung |
| 🌙 Theme-Umschalter | Wechsel zwischen Light Mode und Dark Mode |
| 📸 Screenshot erstellen | Speichert ein Screenshot der gesamten Anwendung |
| 🗂️ Menüleiste | Datei-Menü mit Optionen: Neu, Öffnen, Beenden |

### 📊 Tab 1: Live-Plot
| Funktion | Beschreibung |
|----------|--------------|
| 📈 Live-Diagramm | Darstellung der aktuellen Sensordaten mit Farbmarkierung nach Status |
| ⚙️ Frequenz-Slider | Zeigt aktuelle Messfrequenz, automatisch gesteuert je nach CPU |
| 🌡️ Grenzwert-Eingabe | Benutzerdefinierter Schwellenwert (in °C) |
| ▶️ / ⏹ Start/Stop | Startet oder stoppt die Datenmessung |
| 💾 CSV-Export | Exportiert alle Messdaten als CSV mit Benutzername |
| 📢 Sprachwarnung (TTS) | Automatisierte Sprachausgabe bei kritischer Temperatur |
| 📊 Statistiken | Anzeige von Mittelwert, Maximalwert, Minimalwert |
| ✅⚠️🚨 Statusanzeige | Farbige Anzeige des Temperaturstatus: Normal, nah, kritisch |

### 📜 Tab 2: Historie
| Funktion | Beschreibung |
|----------|--------------|
| 🧾 Tabelle mit Logdaten | Zeigt alle bisherigen Messwerte mit Zeit, Sensorname, Wert, Status |

### 📊 Tab 3: Statistik
| Funktion | Beschreibung |
|----------|--------------|
| 📊 Balkendiagramm | Visualisiert Max, Min und Mittelwert |
| 🔢 Zähler | Zeigt Anzahl aller Normal-, Warn- und Kritisch-Werte |
| 🚨 Warnungszähler | Separater Zähler für kritische Grenzwertüberschreitungen |

### 📈 Tab 4: Analyse
| Funktion | Beschreibung |
|----------|--------------|
| 📈 Trenddiagramm | Darstellung des Temperaturverlaufs der letzten 100 Werte |
| ℹ️ Trendanzeige | Textanzeige des aktuellen Trends (optional erweiterbar) |

### 🎥 Tab 5: Kamera
| Funktion | Beschreibung |
|----------|--------------|
| 📷 Livebildanzeige | Anzeige des Kamerabildes in Echtzeit (OpenCV) |
| 📸 Snapshot speichern | Speichert ein aktuelles Kamerabild |
| 🎥 Videoaufnahme | Startet/stoppt eine Aufnahme des Kamerabildes als .avi-Datei |

---

## 🗂️ Menüfunktionen

| Menüpunkt | Funktion |
|-----------|----------|
| **Neu**   | Setzt das gesamte Dashboard zurück: löscht Messwerte, Statistik, Diagramme |
| **Öffnen**| Öffnet das Projektverzeichnis im Datei-Explorer |
| **Beenden**| Schließt das Programm |

---

## 👥 Wer hat was gemacht?

| Name                          | Aufgabenbereiche                              |
|------------------------------|-----------------------------------------------|
| Alhammoud Yazan              | Hauptlogik, Statistik-Dashboard, Warnsystem   |
| Alhammoud Yamen              | GUI-Design, Kamera-Integration, Snapshot      |
| Hussein Zainab Raad Hussein | CSV-Export, Trendanalyse, Tabellenanzeige     |
| Wendt Celine                 | Dark Mode, Benutzerwechsel, Präsentation      |

---

## 🎯 Projektverlauf

1. Ideenfindung
2. UI-Prototyping
3. Sensor-Logik
4. Live-Plot und Alarmierung
5. Statistik & CSV-Export
6. Kamera & Video
7. Tests & Optimierung
8. Doku & Präsentation
