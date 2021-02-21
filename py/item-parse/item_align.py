from enum import Enum, unique


@unique
class ItemAlign(Enum):

    EVIL = "EVIL", "e!"
    NO_EVIL = "!EVIL", "!e"

    NEUTRAL = "NEUTRAL", "n!"
    NO_NEUTRAL = "!NEUTRAL", "!n"

    GOOD = "GOOD", "g!"
    NO_GOOD = "!GOOD", "!g"

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
