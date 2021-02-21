from enum import Enum, unique


@unique
class ItemAffect(Enum):

    CON = "CON", "con"
    STR = "STR", "str"
    INT = "INT", "int"
    WIS = "WIS", "wis"
    DEX = "DEX", "dex"
    CHARISMA = "CHARISMA", "cha"

    ARMOR = "ARMOR", "arm"

    AGE = "AGE", "age"
    HEIGHT = "HEIGHT", "height"

    HITROLL = "HITROLL", "hit"
    DAMROLL = "DAMROLL", "dam"

    MANA = "MANA", "mn"
    MANA_REGEN = "MANA_REGEN", "mnR"

    HIT = "HIT", "hp"
    HIT_REGEN = "HIT_REGEN", "hpR"

    MOV = "MOVE", "mv"
    MOVE_REGEN = "MOVE_REGEN", "mvR"

    SAVE_SPELL = "SAVE_SPELL", "ss"

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
