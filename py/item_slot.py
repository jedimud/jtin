from enum import Enum, unique


@unique
class ItemSlot(Enum):

    FEET = "Feet", "feet"
    WRIST = "Wrist", "wrist"
    ABOUT_BODY = "About Body", "about body"
    ARMS = "Arms", "arms"
    RING = "Ring", "ring"
    HOLD = "Hold", "hold"
    HEAD = "Head", "head"
    LEGS = "Legs", "legs"
    ON_BODY = "On Body", "on body"
    FACE = "Face", "face"
    EARRING = "Earring", "ears"
    NECK = "Neck", "neck"
    HANDS = "Hands", "hands"
    WAIST = "Waist", "waist"
    LIGHT = "Light", "light"
    WIELD = "Wield", "wield"
    SHIELD = "Shield", "shield"

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
