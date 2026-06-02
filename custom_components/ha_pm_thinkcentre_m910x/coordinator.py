import aiohttp
import asyncio
import logging
from datetime import timedelta

from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL, CONF_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class ThinkCentreCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, entry):
        self.entry = entry
        self.session = async_get_clientsession(hass)

        interval = self.entry.data.get(
            CONF_SCAN_INTERVAL,
            DEFAULT_SCAN_INTERVAL
        )

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=interval),
        )

    async def _async_update_data(self):

        base_url = self.entry.data.get("url")
        if not base_url:
            raise UpdateFailed("Missing base URL")

        endpoints = [
            "sensors",
            "smart",
            "smart-extended",
            "memory",
            "health",
            "mounts",
        ]

        try:
            tasks = [
                self.session.get(f"{base_url}/{ep}", timeout=5)
                for ep in endpoints
            ]

            responses = await asyncio.gather(*tasks, return_exceptions=True)

            data = {}

            for ep, resp in zip(endpoints, responses):

                if isinstance(resp, Exception):
                    _LOGGER.warning("Endpoint failed: %s (%s)", ep, resp)
                    data[ep] = {}
                    continue

                if resp.status == 200:
                    data[ep] = await resp.json()
                else:
                    _LOGGER.warning("Bad response %s: %s", ep, resp.status)
                    data[ep] = {}

            return data

        except Exception as err:
            _LOGGER.exception("Coordinator update failed")
            raise UpdateFailed(str(err)) from err