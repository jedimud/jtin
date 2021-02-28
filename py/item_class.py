from enum import Enum, unique


@unique
class ItemClass(Enum):

    NO_MAGE = "!MAGE", "m"
    NO_CLER = "!CLER", "c"
    NO_THF = "!THF", "t"
    NO_WAR = "!WAR", "w"
    NO_PAL = "!PAL", "p"
    NO_APAL = "!APAL", "a"
    NO_NINJA = "!NINJA", "n"
    NO_JEDI = "!JEDI", "j"
    NO_SOHEI = "!SOHEI", "s"
    NO_RANGER = "!RANGER", "r"
    NO_BARD = "!BARD", "b"

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
