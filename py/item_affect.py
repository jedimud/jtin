from enum import Enum, unique


@unique
class ItemAffect(Enum):

    CON = "CON", "con", True
    STR = "STR", "str", True
    INT = "INT", "int", True
    WIS = "WIS", "wis", True
    DEX = "DEX", "dex", True
    CHARISMA = "CHARISMA", "cha", True

    ARMOR = "ARMOR", "arm", False

    AGE = "AGE", "age", False
    HEIGHT = "HEIGHT", "height", False
    WEIGHT = "WEIGHT", "weight", False

    HITROLL = "HITROLL", "hit", True
    DAMROLL = "DAMROLL", "dam", True

    MANA = "MANA", "mn", True
    MANA_REGEN = "MANA_REGEN", "mnR", False

    HIT = "HIT", "hp", True
    HIT_REGEN = "HIT_REGEN", "hpR", False

    MOVE = "MOVE", "mv", True
    MOVE_REGEN = "MOVE_REGEN", "mvR", False

    SAVE_SPELL = "SAVE_SPELL", "ss", False
    SAVE_BREATH = "SAVE_BREATH", "sb", False
    SAVE_PETRI = "SAVE_PETRI", "sp", False
    SAVE_ROD = "SAVE_ROD", "sr", False
    SAVE_PARA = "SAVE_PARA", "sp", False

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, brief: str = None, sac: bool = False):
        self._brief_ = brief
        self._sac_ = sac

    def __str__(self):
        return self.value

    @property
    def brief(self):
        return self._brief_

    @property
    def sac(self):
        return self._sac_
        