# HA PM ThinkCentre M910x

Monitor für Lenovo ThinkCentre M910x PCs: CPU, RAM, NVMe, System Health.

## Proxmox-Skripte erforderlich

Damit die HA PM ThinkCentre M910x Integration korrekt funktioniert, müssen auf dem Proxmox-Host die Sensoren aus [proxmox_sensors](https://github.com/Javisen/proxmox_sensors/blob/main/docs/de/01-install-sensors.md) installiert und verfügbar sein.

### Benötigte Links:
- ```http://DEINE_PROXMOX_IP:9000/sensors```
- ```http://DEINE_PROXMOX_IP:9000//smart```
- ```http://DEINE_PROXMOX_IP:9000//smart-extended```
- ```http://DEINE_PROXMOX_IP:9000//memory```
- ```http://DEINE_PROXMOX_IP:9000//health```
- ```http://DEINE_PROXMOX_IP:9000//mounts```

## Installation

1. Öffne HACS → Integrationen → `+` → „Repository hinzufügen“  
2. Füge URL ein: `https://github.com/BerndeDGF/ha-pm-thinkcentre-m910x`  
3. Installieren → Home Assistant neu starten

## Konfiguration

1. Gehe zu **Einstellungen → Geräte & Dienste → Integration hinzufügen**  
2. Wähle **HA PM ThinkCentre M910x**  
3. Gib Name + URL deines ThinkCentre ein  
4. Die Sensoren erscheinen automatisch:

- CPU Temperaturen (Package & Cores)  
- NVMe Temperatur & Nutzung  
- RAM Gesamt  
- Systemstatus

## Unterstützt

- Home Assistant 2026.05.1 und neuer  
- HACS Integration