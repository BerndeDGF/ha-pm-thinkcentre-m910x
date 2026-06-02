from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN


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
        })

        return self.async_show_form(step_id="user", data_schema=schema)
