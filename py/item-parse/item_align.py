from enum import Enum, unique


@unique
class ItemAlign(Enum):

    EVIL = "EVIL"
    NO_EVIL = "!EVIL"

    NEUTRAL = "NEUTRAL"
    NO_NEUTRAL = "!NEUTRAL"

    GOOD = "GOOD"
    NO_GOOD = "!GOOD"
