from enum import Enum, unique


@unique
class ItemType(Enum):

    AIRSHIP = "AIRSHIP", "airship"
    ARMOR = "ARMOR", "armor"
    BOAT = "BOAT", "boat"
    CONTAINER = "CONTAINER", "container"
    DEVICE = "DEVICE", "device"
    FIRE_WEAPON = "FIRE-WEAPON", "fire-weapon"
    FOOD = "FOOD", "food"
    KEY = "KEY", "key"
    LIGHT = "LIGHT", "light"
    LIQ_CONTAINER = "LIQ-CONTAINER", "liq-container"
    MISSILE = "MISSILE", "missile"
    NOTE = "NOTE", "note"
    OTHER = "OTHER", "other"
    PEN = "PEN", "pen"
    POTION = "POTION", "potion"
    SCROLL = "SCROLL", "scroll"
    STAFF = "STAFF", "staff"
    TRASH = "TRASH", "trash"
    TREASURE = "TREASURE", "treasure"
    UNDEFINED = "UNDEFINED", "undefined"
    WAND = "WAND", "wand"
    WEAPON = "WEAPON", "weapon"
    WORN = "WORN", "worn"

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
