"""Fete du jour"""
from datetime import date
from datetime import timedelta
import logging
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=60)
CONF_ICON_FETE = 'icon_fete'
CONF_ICON_ANNIVERSAIRE = 'icon_anniversaire'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_ICON_FETE): cv.string,
    vol.Optional(CONF_ICON_ANNIVERSAIRE): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):

    now = date.today()
    date_plus_un = now + timedelta(days=1)
    now= now.strftime("%d:%m")
    date_plus_un = date_plus_un.strftime("%d:%m")

    saint_jour = {}
    today_fete_du_jour = 'aucun'
    anniversaire={}
    personne_anniversaire = 'aucun'
    demain_fete_du_jour = 'aucun'
    demain_personne_anniversaire = 'aucun'

    """Date des saints"""

    saint_jour["01:01"]="le jour de l'An"
    saint_jour["02:01"]="les Basile"
    saint_jour["03:01"]="les Geneviève"
    saint_jour["04:01"]="les Odilon"
    saint_jour["05:01"]="les Édouard"
    saint_jour["06:01"]="les André"
    saint_jour["07:01"]="les Raymond"
    saint_jour["08:01"]="les Lucien"
    saint_jour["09:01"]="les Alix de Ch."
    saint_jour["10:01"]="les Guillaume"
    saint_jour["11:01"]="les Paulin d Aquilee"
    saint_jour["12:01"]="les Tatiana"
    saint_jour["13:01"]="les Yvette"
    saint_jour["14:01"]="les Nina"
    saint_jour["15:01"]="les Rémi"
    saint_jour["16:01"]="les Marcel"
    saint_jour["17:01"]="les Roseline"
    saint_jour["18:01"]="les Prisca"
    saint_jour["19:01"]="les Marius"
    saint_jour["20:01"]="les Sébastien"
    saint_jour["21:01"]="les Agnès"
    saint_jour["22:01"]="les Vincent"
    saint_jour["23:01"]="les Barnard"
    saint_jour["24:01"]="les François"
    saint_jour["25:01"]="la Conversion de Paul"
    saint_jour["26:01"]="les Paule"
    saint_jour["27:01"]="les Angèle"
    saint_jour["28:01"]="les Thomas"
    saint_jour["29:01"]="les Gildas"
    saint_jour["30:01"]="les Martine"
    saint_jour["31:01"]="les Marcelle"
    saint_jour["01:02"]="les Ella"
    saint_jour["02:02"]="les Theophane"
    saint_jour["03:02"]="les Blaise"
    saint_jour["04:02"]="les Véronique"
    saint_jour["05:02"]="les Agathe"
    saint_jour["06:02"]="les Gaston"
    saint_jour["07:02"]="les Eugénie"
    saint_jour["08:02"]="les Jacqueline"
    saint_jour["09:02"]="les Apolline"
    saint_jour["10:02"]="les Arnaud"
    saint_jour["11:02"]="les Severin"
    saint_jour["12:02"]="les Felix"
    saint_jour["13:02"]="les Beatrice"
    saint_jour["14:02"]="les Valentin"
    saint_jour["15:02"]="les Claude"
    saint_jour["16:02"]="les Julienne"
    saint_jour["17:02"]="les Alexis"
    saint_jour["18:02"]="les Bernadette"
    saint_jour["19:02"]="les Gabin"
    saint_jour["20:02"]="les Aimee"
    saint_jour["21:02"]="les Damien"
    saint_jour["22:02"]="les Isabelle"
    saint_jour["23:02"]="les Lazare"
    saint_jour["24:02"]="les Modeste"
    saint_jour["25:02"]="les Romeo"
    saint_jour["26:02"]="les Nestor"
    saint_jour["27:02"]="les Honorine"
    saint_jour["28:02"]="les Romain"
    saint_jour["29:02"]="les Augula"
    saint_jour["01:03"]="les Aubin"
    saint_jour["02:03"]="les Charles"
    saint_jour["03:03"]="les Gwenole"
    saint_jour["04:03"]="les Casimir"
    saint_jour["05:03"]="les Olive"
    saint_jour["06:03"]="les Colette"
    saint_jour["07:03"]="les Félicité"
    saint_jour["08:03"]="les Jean"
    saint_jour["09:03"]="les Françoise"
    saint_jour["10:03"]="les Vivien"
    saint_jour["11:03"]="les Rosine"
    saint_jour["12:03"]="les Justine"
    saint_jour["13:03"]="les Rodrigue"
    saint_jour["14:03"]="les Maud"
    saint_jour["15:03"]="les Louise"
    saint_jour["16:03"]="les Benedicte"
    saint_jour["17:03"]="les Patrick"
    saint_jour["18:03"]="les Cyrille"
    saint_jour["19:03"]="les Joseph"
    saint_jour["20:03"]="les Herbert"
    saint_jour["21:03"]="les Clemence"
    saint_jour["22:03"]="les Lea"
    saint_jour["23:03"]="les Victorien"
    saint_jour["24:03"]="les Catherine"
    saint_jour["25:03"]="les Humbert"
    saint_jour["26:03"]="les Larissa"
    saint_jour["27:03"]="les Habib"
    saint_jour["28:03"]="les Gontran"
    saint_jour["29:03"]="les Gwladys"
    saint_jour["30:03"]="les Amedee"
    saint_jour["31:03"]="les Benjamin"
    saint_jour["01:04"]="les Hugues"
    saint_jour["02:04"]="les Sandrine"
    saint_jour["03:04"]="les Richard"
    saint_jour["04:04"]="les Isidore"
    saint_jour["05:04"]="les Irene"
    saint_jour["06:04"]="les Marcellin"
    saint_jour["07:04"]="les Jean-Baptiste"
    saint_jour["08:04"]="les Julie"
    saint_jour["09:04"]="les Gautier"
    saint_jour["10:04"]="les Fulbert"
    saint_jour["11:04"]="les Stanislas"
    saint_jour["12:04"]="les Jules 1er"
    saint_jour["13:04"]="les Ida"
    saint_jour["14:04"]="les Maxime"
    saint_jour["15:04"]="les Paterne"
    saint_jour["16:04"]="les Benoît"
    saint_jour["17:04"]="les Étienne"
    saint_jour["18:04"]="les Parfait"
    saint_jour["19:04"]="les Emma"
    saint_jour["20:04"]="les Odette"
    saint_jour["21:04"]="les Anselme"
    saint_jour["22:04"]="les Alexandre"
    saint_jour["23:04"]="les Georges"
    saint_jour["24:04"]="les Fidèle"
    saint_jour["25:04"]="les Marc"
    saint_jour["26:04"]="les Alida"
    saint_jour["27:04"]="les Zita"
    saint_jour["28:04"]="les Valérie"
    saint_jour["29:04"]="les Catherine"
    saint_jour["30:04"]="les Robert"
    saint_jour["01:05"]="les Joseph"
    saint_jour["02:05"]="les Boris"
    saint_jour["03:05"]="les Philippe"
    saint_jour["04:05"]="les Sylvain"
    saint_jour["05:05"]="les Judith"
    saint_jour["06:05"]="les Prudence"
    saint_jour["07:05"]="les Gisèle"
    saint_jour["08:05"]="les Desire"
    saint_jour["09:05"]="les Pacôme"
    saint_jour["10:05"]="les Solange"
    saint_jour["11:05"]="les Estelle"
    saint_jour["12:05"]="les Achille"
    saint_jour["13:05"]="les Rolande"
    saint_jour["14:05"]="les Matthias"
    saint_jour["15:05"]="les Denise"
    saint_jour["16:05"]="les Honore"
    saint_jour["17:05"]="les Pascal"
    saint_jour["18:05"]="les Éric"
    saint_jour["19:05"]="les Yves"
    saint_jour["20:05"]="les Bernardin"
    saint_jour["21:05"]="les Constantin"
    saint_jour["22:05"]="les Émile"
    saint_jour["23:05"]="les Didier"
    saint_jour["24:05"]="les Donatien"
    saint_jour["25:05"]="les Sophie"
    saint_jour["26:05"]="les Bérenger"
    saint_jour["27:05"]="les Augula"
    saint_jour["28:05"]="les Germain"
    saint_jour["29:05"]="les Aymard"
    saint_jour["30:05"]="les Ferdinand"
    saint_jour["31:05"]="les Perrine"
    saint_jour["01:06"]="les Justin"
    saint_jour["02:06"]="les Blandine"
    saint_jour["03:06"]="les Charles"
    saint_jour["04:06"]="les Clotilde"
    saint_jour["05:06"]="les Igor"
    saint_jour["06:06"]="les Norbert"
    saint_jour["07:06"]="les Gilbert"
    saint_jour["08:06"]="les Médard"
    saint_jour["09:06"]="les Diane"
    saint_jour["10:06"]="les Landry"
    saint_jour["11:06"]="les Barnabé"
    saint_jour["12:06"]="les Guy"
    saint_jour["13:06"]="les Antoine"
    saint_jour["14:06"]="les Élisée"
    saint_jour["15:06"]="les Germaine"
    saint_jour["16:06"]="les Jean-François"
    saint_jour["17:06"]="les Hervé"
    saint_jour["18:06"]="les Leonce"
    saint_jour["19:06"]="les Romuald"
    saint_jour["20:06"]="les Silvère"
    saint_jour["21:06"]="les Rodolphe"
    saint_jour["22:06"]="les Alban"
    saint_jour["23:06"]="les Audrey"
    saint_jour["24:06"]="les Jean-Baptiste"
    saint_jour["25:06"]="les Prosper"
    saint_jour["26:06"]="les Anthelme"
    saint_jour["27:06"]="les Fernand"
    saint_jour["28:06"]="les Irénée"
    saint_jour["29:06"]="les Pierre et Paul"
    saint_jour["30:06"]="les Martial"
    saint_jour["01:07"]="les Thierry"
    saint_jour["02:07"]="les Martinien"
    saint_jour["03:07"]="les Thomas"
    saint_jour["04:07"]="les Florent"
    saint_jour["05:07"]="les Antoine"
    saint_jour["06:07"]="les Mariette"
    saint_jour["07:07"]="les Raoul"
    saint_jour["08:07"]="les Thibaud"
    saint_jour["09:07"]="les Amandine"
    saint_jour["10:07"]="les Ulric"
    saint_jour["11:07"]="les Benoit"
    saint_jour["12:07"]="les Olivier"
    saint_jour["13:07"]="les Joëlle"
    saint_jour["14:07"]="les Camille"
    saint_jour["15:07"]="les Donald"
    saint_jour["16:07"]="les Elvire"
    saint_jour["17:07"]="les Charlotte"
    saint_jour["18:07"]="les Frédéric"
    saint_jour["19:07"]="les Arsène"
    saint_jour["20:07"]="les Marina"
    saint_jour["21:07"]="les Victor"
    saint_jour["22:07"]="les Marie-Madeleine"
    saint_jour["23:07"]="les Brigitte"
    saint_jour["24:07"]="les Christine"
    saint_jour["25:07"]="les Jacques"
    saint_jour["26:07"]="les Anne"
    saint_jour["27:07"]="les Nathalie"
    saint_jour["28:07"]="les Samson"
    saint_jour["29:07"]="les Marthe"
    saint_jour["30:07"]="les Juliette"
    saint_jour["31:07"]="les Ignace"
    saint_jour["01:08"]="les Alphonse"
    saint_jour["02:08"]="les Julien"
    saint_jour["03:08"]="les Lydie"
    saint_jour["04:08"]="les Jean-Marie"
    saint_jour["05:08"]="les Abel"
    saint_jour["06:08"]="les Octavien"
    saint_jour["07:08"]="les Gaetan"
    saint_jour["08:08"]="les Dominique"
    saint_jour["09:08"]="les Amour"
    saint_jour["10:08"]="les Laurent"
    saint_jour["11:08"]="les Claire"
    saint_jour["12:08"]="les Clarisse"
    saint_jour["13:08"]="les Hippolyte"
    saint_jour["14:08"]="les Evrard"
    saint_jour["15:08"]="les Marie"
    saint_jour["16:08"]="les Armel"
    saint_jour["17:08"]="les Hyacinthe"
    saint_jour["18:08"]="les Hélène"
    saint_jour["19:08"]="les Eudes"
    saint_jour["20:08"]="les Bernard"
    saint_jour["21:08"]="les Christophe"
    saint_jour["22:08"]="les Fabrice"
    saint_jour["23:08"]="les Rose"
    saint_jour["24:08"]="les Barthélemy"
    saint_jour["25:08"]="les Louis"
    saint_jour["26:08"]="les Natacha"
    saint_jour["27:08"]="les Monique"
    saint_jour["28:08"]="les Augustin"
    saint_jour["29:08"]="les Sabine"
    saint_jour["30:08"]="les Fiacre"
    saint_jour["31:08"]="les Aristide"
    saint_jour["01:09"]="les Gilles"
    saint_jour["02:09"]="les Ingrid"
    saint_jour["03:09"]="les Grégoire"
    saint_jour["04:09"]="les Rosalie"
    saint_jour["05:09"]="les Raïssa"
    saint_jour["06:09"]="les Bertrand"
    saint_jour["07:09"]="les Reine"
    saint_jour["08:09"]="les Adrien"
    saint_jour["09:09"]="les Alain"
    saint_jour["10:09"]="les Inès"
    saint_jour["11:09"]="les Adelphe"
    saint_jour["12:09"]="les Apollinaire"
    saint_jour["13:09"]="les Aime"
    saint_jour["14:09"]="les Lubin"
    saint_jour["15:09"]="les Roland"
    saint_jour["16:09"]="les Édith"
    saint_jour["17:09"]="les Renaud"
    saint_jour["18:09"]="les Nadège"
    saint_jour["19:09"]="les Émilie"
    saint_jour["20:09"]="les Davy"
    saint_jour["21:09"]="les Matthieu"
    saint_jour["22:09"]="les Maurice"
    saint_jour["23:09"]="les Constant"
    saint_jour["24:09"]="les Thecle"
    saint_jour["25:09"]="les Hermann"
    saint_jour["26:09"]="les Damien"
    saint_jour["27:09"]="les Vincent"
    saint_jour["28:09"]="les Venceslas"
    saint_jour["29:09"]="les Michel"
    saint_jour["30:09"]="les Jérôme"
    saint_jour["01:10"]="les Thérèse"
    saint_jour["02:10"]="les Léger"
    saint_jour["03:10"]="les Gérard"
    saint_jour["04:10"]="les François"
    saint_jour["05:10"]="les Fleur"
    saint_jour["06:10"]="les Bruno"
    saint_jour["07:10"]="les Serge"
    saint_jour["08:10"]="les Pélagie"
    saint_jour["09:10"]="les Denis"
    saint_jour["10:10"]="les Ghislain"
    saint_jour["11:10"]="les Firmin"
    saint_jour["12:10"]="les Wilfrid"
    saint_jour["13:10"]="les Géraud"
    saint_jour["14:10"]="les Juste"
    saint_jour["15:10"]="les Thérèse"
    saint_jour["16:10"]="les Edwige"
    saint_jour["17:10"]="les Baudouin"
    saint_jour["18:10"]="les Luc"
    saint_jour["19:10"]="les René Goupil"
    saint_jour["20:10"]="les Lina"
    saint_jour["21:10"]="les Céline"
    saint_jour["22:10"]="les Elodie"
    saint_jour["23:10"]="les Jean"
    saint_jour["24:10"]="les Florentin"
    saint_jour["25:10"]="les Crépin"
    saint_jour["26:10"]="les Dimitri"
    saint_jour["27:10"]="les Émeline"
    saint_jour["28:10"]="les Simon"
    saint_jour["29:10"]="les Narcisse"
    saint_jour["30:10"]="les Bienvenue"
    saint_jour["31:10"]="les Quentin"
    saint_jour["01:11"]="la Toussaint"
    saint_jour["02:11"]="les defunts"
    saint_jour["03:11"]="les Hubert"
    saint_jour["04:11"]="les Charles"
    saint_jour["05:11"]="les Sylvie"
    saint_jour["06:11"]="les Bertille"
    saint_jour["07:11"]="les Carine"
    saint_jour["08:11"]="les Geoffroy"
    saint_jour["09:11"]="les Theodore"
    saint_jour["10:11"]="les Leon"
    saint_jour["11:11"]="les Martin"
    saint_jour["12:11"]="les Christian"
    saint_jour["13:11"]="les Brice"
    saint_jour["14:11"]="les Sidoine"
    saint_jour["15:11"]="les Albert"
    saint_jour["16:11"]="les Marguerite"
    saint_jour["17:11"]="les Élisabeth"
    saint_jour["18:11"]="les Aude"
    saint_jour["19:11"]="les Tanguy"
    saint_jour["20:11"]="les Edmond"
    saint_jour["21:11"]="les Albert"
    saint_jour["22:11"]="les Cécile"
    saint_jour["23:11"]="les Clement"
    saint_jour["24:11"]="les Flora"
    saint_jour["25:11"]="les Catherine"
    saint_jour["26:11"]="les Delphine"
    saint_jour["27:11"]="les Severin"
    saint_jour["28:11"]="les Jacques"
    saint_jour["29:11"]="les Saturnin"
    saint_jour["30:11"]="les Andre"
    saint_jour["01:12"]="les Florence"
    saint_jour["02:12"]="les Viviane"
    saint_jour["03:12"]="les Xavier"
    saint_jour["04:12"]="les Barbara"
    saint_jour["05:12"]="les Gerald"
    saint_jour["06:12"]="les Nicolas"
    saint_jour["07:12"]="les Ambroise"
    saint_jour["08:12"]="les Elfie"
    saint_jour["09:12"]="les Pierre"
    saint_jour["10:12"]="les Romaric"
    saint_jour["11:12"]="les Daniel"
    saint_jour["12:12"]="les Chantal"
    saint_jour["13:12"]="les Lucie"
    saint_jour["14:12"]="les Odile"
    saint_jour["15:12"]="les Ninon"
    saint_jour["16:12"]="les Alice"
    saint_jour["17:12"]="les Gael"
    saint_jour["18:12"]="les Gatien"
    saint_jour["19:12"]="les Urbain"
    saint_jour["20:12"]="les Theophile"
    saint_jour["21:12"]="les Pierre"
    saint_jour["22:12"]="les Xaviere"
    saint_jour["23:12"]="les Armand"
    saint_jour["24:12"]="les Adele"
    saint_jour["25:12"]="Noel"
    saint_jour["26:12"]="les Etienne"
    saint_jour["27:12"]="les Jean"
    saint_jour["28:12"]="les Innocents"
    saint_jour["29:12"]="les David"
    saint_jour["30:12"]="les Roger"
    saint_jour["31:12"]="les Sylvestre"

    """Date Anniversaire"""

    anniversaire["15:01"]="Danielle"
    anniversaire["01:04"]="Laura"
    anniversaire["07:11"]="Sébastien"
    anniversaire["15:06"]="Sylvain"

    for s in saint_jour.keys():
        if s == now:
            today_fete_du_jour = saint_jour[now]
        if s == date_plus_un:
            demain_fete_du_jour = saint_jour[date_plus_un]

    for s in anniversaire.keys():
        if s == now:
            personne_anniversaire = anniversaire[now]
        if s == date_plus_un:
            demain_personne_anniversaire = anniversaire[date_plus_un]

    icon_fete = config[CONF_ICON_FETE]
    icon_anniversaire = config[CONF_ICON_ANNIVERSAIRE]
    devices = [FeteDuJourSensor('Fête du jour', today_fete_du_jour,icon_fete)]
    add_entities(devices, True)
    devices = [FeteDuJourSensor('Fête de demain', demain_fete_du_jour,icon_fete)]
    add_entities(devices, True)
    devices = [FeteDuJourSensor('Anniversaire du jour', personne_anniversaire,icon_anniversaire)]
    add_entities(devices, True)
    devices = [FeteDuJourSensor('Anniversaire de demain', demain_personne_anniversaire,icon_anniversaire)]
    add_entities(devices, True)

class FeteDuJourSensor(Entity):
    def __init__(self, name, fete,icon):
        """Initialize the sensor."""
        self._name = name
        self._fete = fete
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
        self._state = self._fete
