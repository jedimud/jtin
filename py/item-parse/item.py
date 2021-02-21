from item_type import ItemType
from item_ability import ItemAbility
from item_tag import ItemTag
from item_slot import ItemSlot


class Item():

    def __init__(self):

        self.name = str()
        self.type = ItemType
        self.ability = ItemAbility
        self.tags = []
        self.weight = None
        self.value = None
        self.rent = None

        self.min_level = None
        self.max_level = None

        self.ac = None

        self.slots = []
        self.affects = {}

        self.units = None
        self.liq_units = None

        self.spells = []
        self.spell_level = None
        self.charge_max = None
        self.charge_remain = None

        self.dice_face = None
        self.dice_count = None
        self.average_dmg = None
