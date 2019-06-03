"""Support for Linky."""
import logging
import json
from datetime import timedelta

import voluptuous as vol

from homeassistant.const import (CONF_USERNAME, CONF_PASSWORD, CONF_TIMEOUT,
                                 ENERGY_KILO_WATT_HOUR)
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=10)
DEFAULT_TIMEOUT = 10
CONF_PRIX = 'prix'
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_USERNAME): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
    vol.Optional(CONF_PRIX): cv.string,
    vol.Optional(CONF_TIMEOUT, default=DEFAULT_TIMEOUT): cv.positive_int,
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Configure the platform and add the Linky sensor."""
    username = config[CONF_USERNAME]
    password = config[CONF_PASSWORD]
    timeout = config[CONF_TIMEOUT]
    prix = config[CONF_PRIX]
    _LOGGER.debug("prix : "+ str(prix))
    from pylinky.client import LinkyClient, PyLinkyError
    client = LinkyClient(username, password, None, timeout)
    try:
        client.login()
        client.fetch_data()
    except PyLinkyError as exp:
        _LOGGER.error(exp)
        client.close_session()
        return

    devices = [LinkySensor('Linky / hier', client, 'daily','compteur', None)]
    add_entities(devices, True)

    devices = [LinkySensor('Linky / Mois Current', client,"monthly",'compteur',None)]
    add_entities(devices, True)

    devices = [LinkySensor('Linky / Année Current', client, "yearly",'compteur',None)]
    add_entities(devices, True)

    devices = [LinkySensor('Prix / hier', client, 'daily','prix',prix)]
    add_entities(devices, True)

    devices = [LinkySensor('Prix / Mois Current', client, "monthly",'prix',prix)]
    add_entities(devices, True)

    devices = [LinkySensor('prix / Année Current', client, "yearly",'prix',prix)]
    add_entities(devices, True)
    # devices = []
    # devices.append(LinkySensor('Linky / hier', client, 'daily'))
    # devices.append(LinkySensor('Linky / Mois Current', client,"monthly"))
    # devices.append(LinkySensor('Linky / Année Current', client, "yearly"))
    # add_entities(devices,True)

class LinkySensor(Entity):
    """Representation of a sensor entity for Linky."""

    def __init__(self, name, client,periode,type,prix):
        """Initialize the sensor."""
        self._name = name
        self._client = client
        self._state = None
        self._periode = periode
        self._type = type
        self._prix = prix

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        if self._type == 'compteur':
            return ENERGY_KILO_WATT_HOUR
        else:
            return "€"

    @Throttle(SCAN_INTERVAL)
    def update(self):
        """Fetch new state data for the sensor."""
        from pylinky.client import PyLinkyError
        try:
            self._client.fetch_data()
        except PyLinkyError as exp:
            _LOGGER.error(exp)
            self._client.close_session()
            return
        if self._periode == "daily":
            derniere = 2
        else:
            derniere = 1
        # _LOGGER.debug(json.dumps(self._client.get_data(), indent=2))

        if self._client.get_data():
            # get the last past day data
            if self._type == 'compteur':
                self._state = self._client.get_data()[self._periode][-derniere]['conso']
            elif self._type == 'prix':
                total = float(self._prix) * float(self._client.get_data()[self._periode][-derniere]['conso'])
                _LOGGER.debug("total :" + str(round(float(total),3)))
                self._state = round(float(total),3)
        else:
            self._state = None
        _LOGGER.debug(" update linky " + str(self._periode) + str(" : ") + str(self._client.get_data()[self._periode][-derniere]['conso']))