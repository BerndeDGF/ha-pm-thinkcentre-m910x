from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers import device_registry as dr

from .const import DOMAIN


def safe(data, path):
    try:
        for p in path:
            data = data[p]
        return data
    except Exception:
        return None


SENSOR_MAP = [
    ("cpu_package_temp", "CPU Package Temperatur", "°C",
     ["sensors", "coretemp-isa-0000", "Package id 0", "temp1_input"]),

    ("cpu_core0", "CPU Core 0", "°C",
     ["sensors", "coretemp-isa-0000", "Core 0", "temp2_input"]),

    ("cpu_core1", "CPU Core 1", "°C",
     ["sensors", "coretemp-isa-0000", "Core 1", "temp3_input"]),

    ("cpu_core2", "CPU Core 2", "°C",
     ["sensors", "coretemp-isa-0000", "Core 2", "temp4_input"]),

    ("cpu_core3", "CPU Core 3", "°C",
     ["sensors", "coretemp-isa-0000", "Core 3", "temp5_input"]),

    ("nvme_temp", "NVMe Temperatur", "°C",
     ["sensors", "nvme-pci-0100", "Composite", "temp1_input"]),

    ("nvme_usage", "NVMe Nutzung", "%",
     ["smart", "nvme0", "percentage_used"]),

    ("nvme_hours", "NVMe Betriebsstunden", "h",
     ["smart", "nvme0", "power_on_hours"]),

    ("ram_total", "RAM Gesamt", "GB",
     ["memory", "total_gb"]),

    ("system_health", "System Status", None,
     ["health", "status"]),
]


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, entry.entry_id)},
        name=entry.data.get("name", "ThinkCentre M910x"),
        manufacturer="Lenovo",
        model="ThinkCentre M910x",
        configuration_url=entry.data.get("url"),
    )

    async_add_entities([
        ThinkCentreSensor(coordinator, entry, key, name, unit, path)
        for key, name, unit, path in SENSOR_MAP
    ])


class ThinkCentreSensor(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator, entry, key, name, unit, path):
        super().__init__(coordinator)
        self.entry = entry
        self._key = key
        self._name = name
        self._unit = unit
        self._path = path

    @property
    def name(self):
        return f"{self.entry.data.get('name', 'ThinkCentre M910x')} {self._name}"

    @property
    def unique_id(self):
        return f"{self.entry.entry_id}_{self._key}"

    @property
    def state(self):
        return safe(self.coordinator.data, self._path)

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.entry.entry_id)},
            "name": self.entry.data.get("name"),
            "manufacturer": "Lenovo",
            "model": "ThinkCentre M910x",
        }
