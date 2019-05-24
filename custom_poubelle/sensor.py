"""Support for Custom Poubelle."""
from datetime import date
import logging
from datetime import timedelta
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=60)
CONF_JOUR_PAIRE = 'jour_paire'
CONF_JOUR_IMPAIRE = 'jour_impaire'
CONF_JOUR = 'jour'
CONF_ICON = 'icon'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_JOUR_PAIRE): cv.string,
    vol.Optional(CONF_JOUR_IMPAIRE): cv.string,
    vol.Optional(CONF_JOUR): cv.positive_int,
    vol.Optional(CONF_ICON): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Configure the platform and add the Poubelle sensor."""
    now = date.today()
    numero_jour = now.isoweekday()
    numero_semaine = now.strftime("%V")

    poubelle_paire = config[CONF_JOUR_PAIRE]
    poubelle_impaire = config[CONF_JOUR_IMPAIRE]
    jour = config[CONF_JOUR]
    icon = config[CONF_ICON]

    devices = [PoubelleSensor('Poubelle de la semaine', numero_jour,jour,numero_semaine,poubelle_paire,poubelle_impaire,icon)]
    add_entities(devices, True)

class PoubelleSensor(Entity):
    """Representation of a sensor entity for Linky."""

    def __init__(self, name, numero_jour,jour,numero_semaine,poubelle_paire,poubelle_impaire,icon):
        """Initialize the sensor."""
        self._name = name
        self._numero_jour = numero_jour
        self._jour = jour
        self._numero_semaine = numero_semaine
        self._poubelle_paire = poubelle_paire
        self._poubelle_impaire = poubelle_impaire
        self._state = None
        self._icon = icon

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
        return None

    @property
    def icon(self):
        """Return icon."""
        return self._icon

    @Throttle(SCAN_INTERVAL)
    def update(self):
        now = date.today()
        numero_jour = now.isoweekday()
        numero_semaine = now.strftime("%V")

        """Fetch new state data for the sensor."""
        if (int(numero_semaine) % 2) == 0 and numero_jour > self._jour:
            self._state = self._poubelle_impaire
        elif (int(numero_semaine) % 2) == 0 and numero_jour <= self._jour:
            self._state = self._poubelle_paire

        elif (int(numero_semaine) % 2) != 0 and numero_jour > self._jour:
            self._state = self._poubelle_paire
        elif (int(numero_semaine) % 2) != 0 and numero_jour <= self._jour:
            self._state = self._poubelle_impaire
