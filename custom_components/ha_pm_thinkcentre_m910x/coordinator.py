import aiohttp
import logging
from datetime import timedelta

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN
from .const import DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class ThinkCentreCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self):

        base_url = self.entry.data.get("url")

        if not base_url:
            return {}

        data = {}

        endpoints = [
            "sensors",
            "smart",
            "smart-extended",
            "memory",
            "health",
            "mounts",
        ]

        async with aiohttp.ClientSession() as session:
            for ep in endpoints:
                try:
                    async with session.get(f"{base_url}/{ep}", timeout=5) as resp:
                        if resp.status == 200:
                            data[ep] = await resp.json()
                        else:
                            data[ep] = {}
                except Exception:
                    data[ep] = {}

        return data
