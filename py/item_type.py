from enum import Enum, unique


@unique
class ItemType(Enum):

    AIRSHIP = "AIRSHIP", "airship"
    ARMOR = "ARMOR", "armor"
    BOAT = "BOAT", "boat"
    CONTAINER = "CONTAINER", "container"
    FOOD = "FOOD", "food"
    LIQ_CONTAINER = "LIQ-CONTAINER", "liq-container"
    OTHER = "OTHER", "other"
    POTION = "POTION", "potion"
    SCROLL = "SCROLL", "scroll"
    STAFF = "STAFF", "staff"
    WAND = "WAND", "wand"
    WORN = "WORN", "worn"
    LIGHT = "LIGHT", "light"
    WEAPON = "WEAPON", "weapon"
    KEY = "KEY", "key"
    FIRE_WEAPON = "FIRE-WEAPON", "fire-weapon"
    TREASURE = "TREASURE", "treasure"
    MISSILE = "MISSILE", "missile"
    TRASH = "TRASH", "trash"
    NOTE = "NOTE", "note"
    UNDEFINED = "UNDEFINED", "undefined"
    PEN = "PEN", "pen"

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, brief: str = None):
        self._brief_ = brief

    def __str__(self):
        return self.value

    @property
    def brief(self):
        return self._brief_
