from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL


class ThinkCentreM910XConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            return self.async_create_entry(
                title=user_input["name"],
                data=user_input,
            )

        schema = vol.Schema({
            vol.Required("name", default="Lenovo ThinkCentre M910x"): str,
            vol.Required("url", default="http://192.168.2.16:9000"): str,

            vol.Optional(
                "scan_interval",
                default=DEFAULT_SCAN_INTERVAL
            ): vol.All(int, vol.Range(min=10, max=300)),
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )