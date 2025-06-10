
# 📊 Sensor Monitor Dashboard

Ein interaktives PyQt6-Dashboard zur Visualisierung und Analyse simulierten Temperaturdaten mit zusätzlichen Funktionen wie Kamera-Livestream, CSV-Export, Snapshot- und Videoaufzeichnung.

---

## 🧠 Projektbeschreibung

Projektbeschreibung 
Der Sensor Monitor ist eine interaktive Anwendung, mit der sich Temperaturdaten von 
Sensoren in Echtzeit überwachen, analysieren und dokumentieren lassen. Entwickelt wurde das 
Projekt im Rahmen eines Softwareentwicklungsprojekts mit Python und PyQt6. Ziel war es, 
eine benutzerfreundliche Oberfläche zu schaffen, die nicht nur Messwerte live darstellt, sondern 
auch Auswertungen ermöglicht und praktische Zusatzfunktionen bietet. 
Die Anwendung zeigt die Temperaturdaten in einem Live-Diagramm an und protokolliert alle 
Werte automatisch in einer Tabelle, sodass der Verlauf jederzeit nachvollzogen werden kann. 
Neben der reinen Anzeige werden auch statistische Kennzahlen wie Minimum, Maximum und 
Durchschnitt berechnet und grafisch aufbereitet. Zusätzlich erkennt das System kritische 
Wertebereiche und reagiert bei Überschreitungen mit visuellen Hinweisen und einer 
Sprachausgabe als akustische Warnung. 
Ein weiteres Highlight ist die integrierte Kamerafunktion. Damit kann man ein Livebild 
anzeigen lassen, Schnappschüsse machen oder Videoaufnahmen starten – etwa zur zusätzlichen 
Dokumentation von Umgebungsbedingungen. Auch ein Screenshot der Benutzeroberfläche 
kann mit einem Klick erstellt werden. 
Die Daten lassen sich bei Bedarf als CSV-Datei exportieren oder als PDF-Bericht ausgeben. 
Darüber hinaus gibt es eine Druckfunktion, um Ergebnisse direkt zu Papier zu bringen. 
Die Anwendung unterstützt sowohl einen hellen als auch einen dunklen Modus und passt die 
Abtastrate automatisch an die aktuelle CPU-Auslastung an, um effizient zu arbeiten. 
So bietet das Sensor Monitor eine umfassende Lösung zur Messwerterfassung und -auswertung mit 
vielen nützlichen Funktionen, die im Alltag eines technischen oder wissenschaftlichen Projekts 
echten Mehrwert schaffen. 

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
