from enum import Enum, unique


@unique
class ItemTag(Enum):

    BLESS = "BLESS"
    GLOW = "GLOW"
    HUM = "HUM"
    INVIS = "INVIS"
    INSURED = "INSURED"
    LIMITED = "LIMITED"
    MAG = "MAG"
    NO_DONATE = "!DONATE"
    NO_DROP = "!DROP"
    NO_LOCATE = "!LOCATE"
    UNIQUE = "UNIQUE"
    NO_JUNK = "!JUNK"
    ASSM = "ASSM"
    NO_RENT = "!RENT"
    NO_PURGE = "!PURGE"
    NOBITS = "NOBITS"
    NO_MORT = "!MORT"
