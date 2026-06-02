# ThinkCentre M910x Monitor (Home Assistant Custom Integration)

Eine Home Assistant Custom Integration zur Überwachung eines  
Lenovo ThinkCentre M910x über eine REST API.

Sie liest Systemdaten wie CPU-Temperaturen, NVMe-Health, RAM und Systemstatus aus und stellt sie als Home Assistant Sensoren bereit.

---

## 📊 Funktionen

- CPU Temperatur (Package + Cores)
- NVMe SSD Temperatur & Verschleiß
- NVMe Betriebsstunden
- RAM Gesamt
- System Health Status
- Automatische Aktualisierung alle 30 Sekunden
- Geräteintegration im Home Assistant Device Registry

---

## 🖥️ Unterstützte API Endpunkte

Die Integration erwartet folgende REST API Struktur:

http://<ip>:9000/sensors  
http://<ip>:9000/smart  
http://<ip>:9000/smart-extended  
http://<ip>:9000/memory  
http://<ip>:9000/health  
http://<ip>:9000/mounts  

---

## ⚙️ Installation

### 1. Custom Components Ordner

Lege die Integration hier ab:

/config/custom_components/thinkcentre_m910x/

---

### 2. Dateien kopieren

Folgende Dateien müssen enthalten sein:

manifest.json  
__init__.py  
config_flow.py  
coordinator.py  
sensor.py  
const.py  

---

### 3. Home Assistant Neustart

Nach dem Kopieren muss Home Assistant vollständig neu gestartet werden.

---

## ➕ Einrichtung

Nach dem Neustart:

1. Gehe zu Einstellungen → Geräte & Dienste  
2. Klicke auf Integration hinzufügen  
3. Suche nach: ThinkCentre M910x Monitor  
4. URL eintragen: http://<IP-DEINES-SERVERS>:9000  

---

## 🖥️ Gerät in Home Assistant

Nach der Einrichtung wird automatisch ein Gerät erstellt:

Lenovo ThinkCentre M910x  

Alle Sensoren werden diesem Gerät zugeordnet.

---

## 📡 Sensoren

CPU:
- CPU Package Temperatur  
- CPU Core 0–3 Temperatur  

NVMe SSD:
- Temperatur  
- Verschleiß (% used)  
- Betriebsstunden  

RAM:
- Gesamter Arbeitsspeicher  

System:
- Health Status  

---

## 🔄 Update Intervall

Standard: 30 Sekunden  
Anpassbar im Coordinator  

---

## ⚠️ Hinweise

- Custom Integration (nicht offiziell von Home Assistant geprüft)
- API muss erreichbar sein, sonst keine Werte
- Home Assistant bleibt stabil bei API-Ausfall

---

## 🧠 Architektur

- DataUpdateCoordinator sammelt REST Daten zentral
- Sensoren greifen nur auf gecachte Daten zu
- Device Registry sorgt für saubere Gerätezuordnung

---

## 🛠️ Fehlerbehebung

Integration erscheint nicht:
- Neustart Home Assistant
- Ordnername muss exakt thinkcentre_m910x sein

Keine Sensorwerte:
- API erreichbar?
- URL korrekt?

Einrichtungsfehler:
- Logs prüfen: Einstellungen → System → Protokolle

---

## 📌 Beispiel API Antwort

/sensors:
{
  "coretemp-isa-0000": {
    "Package id 0": {
      "temp1_input": 55.0
    }
  }
}

/smart:
{
  "nvme0": {
    "percentage_used": 17,
    "power_on_hours": 56678
  }
}

---

## 🧩 Kompatibilität

- Home Assistant 2025.x
- Home Assistant 2026.x
- Linux Sensor API kompatible Systeme

---

## 📜 Lizenz

Private / Custom Use

---

## 🚀 Nächste Schritte

Optional:

- Dashboard für Lovelace
- Temperatur-Alarme
- Verlaufsdiagramme
- automatische Sensor-Erkennung
