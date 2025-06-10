
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
Die Umsetzung des Projekts erfolgte im Team und wurde von Anfang an gemeinsam geplant 
und besprochen. Wir haben alle Schritte, vom ersten Entwurf über die Umsetzung bis hin zum 
Testen, als Gruppe abgestimmt, wodurch jeder jederzeit einen Überblick über das 
Gesamtprojekt hatte. Gleichzeitig hat aber auch jede Person eine konkrete Aufgabe 
übernommen, um die Arbeit effizient zu strukturieren und Verantwortung zu verteilen. In der 
Hier sieht man die Verantwortung der einzelnen Projektmitglieder:
| Name                          | Beiträge                                                                                         |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| **Yamen Alhammoud**           | Kamera- und Speicherfunktion <br> • Nutzung von OpenCV zur Anzeige von Live-Bildern <br> • Speichern von Bildern und Videos in Ordnern <br> • Integration der Kamerabilder in die GUI <br> • CSV |
| **Yazan Alhammoud**           | Diagramme und Statistik-Update <br> • Datenvisualisierung <br> • Trendanalyse <br> • Statistische Auswertung von Sensorwerten <br> • Balkendiagramm |
| **Celine Wendt**              | Bedienelemente und Menüführung <br> • Start- und Stopp-Funktionen <br> • Steuerung der Sensor Datenübertragung <br> • Allgemeine Menüstruktur <br> • Tabs |
| **Zainab Raad Hussein Hussein** | Benutzerinteraktion und Anzeige <br> • Themenauswahl via ComboBox <br> • Statistische Kennzahlen <br> • Frequenz-Slider und Eingabeelemente <br> • Timer |

## 🎯 Projektverlauf

1. Ideenfindung
2. UI-Prototyping
3. Sensor-Logik
4. Live-Plot und Alarmierung
5. Statistik & CSV-Export
6. Kamera & Video
7. Tests & Optimierung
8. Doku & Präsentation
