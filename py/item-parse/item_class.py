from enum import Enum, unique


@unique
class ItemClass(Enum):

    NO_MAGE = "!MAGE"
    NO_THF = "!THF"
    NO_NINJA = "!NINJA"
    NO_WAR = "!WAR"
    NO_JEDI = "!JEDI"
    NO_CLER = "!CLER"
    NO_PAL = "!PAL"
    NO_APAL = "!APAL"
    NO_RANGER = "!RANGER"
    NO_BARD = "!BARD"
    NO_SOHEI = "!SOHEI"