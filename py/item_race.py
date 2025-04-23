from enum import Enum, unique


@unique
class ItemRace(Enum):

    NO_HUMAN = "!HUMAN"
    NO_ELF = "!ELF"
    NO_DWARF = "!DWARF"
    NO_ORC = "!ORC"
    NO_HALF_ORC = "!HALF-ORC"
    NO_GOBLIN = "!GOBLIN"
    NO_URUKHAI = "!URUKHAI"
    NO_HALF_ELF = "!HALF_ELF"
    NO_GNOME = "!GNOME"
    NO_HOBBIT = "!HOBBIT"
    NO_KENDER = "!KENDER"
