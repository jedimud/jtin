from enum import Enum, unique


@unique
class ItemType(Enum):
    AIRSHIP = "AIRSHIP"
    ARMOR = "ARMOR"
    BOAT = "BOAT"
    CONTAINER = "CONTAINER"
    FOOD = "FOOD"
    LIQ_CONTAINER = "LIQ-CONTAINER"
    OTHER = "OTHER"
    POTION = "POTION"
    SCROLL = "SCROLL"
    STAFF = "STAFF"
    WAND = "WAND"
    WORN = "WORN"
    LIGHT = "LIGHT"
    WEAPON = "WEAPON"
    # KEY = "KEY"
    # FIRE_WEAPON = "FIRE-WEAPON"
    TREASURE = "TREASURE"
    # MISSILE = "MISSILE"
    # TRASH = "TRASH"
    # NOTE = "NOTE"
