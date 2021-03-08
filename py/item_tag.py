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
    UNIQUE = "UNIQUE"
    NO_JUNK = "!JUNK"
    ASSM = "ASSM"
    NO_RENT = "!RENT"
    NO_PURGE = "!PURGE"
