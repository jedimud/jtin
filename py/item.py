from item_type import ItemType
from item_ability import ItemAbility
from item_tag import ItemTag
from item_class import ItemClass
from item_align import ItemAlign
from item_slot import ItemSlot
import json
from copy import deepcopy


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

        self.brief_inv = str()
        self.brief_eq = str()
        self.brief_sac = str()
        self.brief_limited = str()

    def __dict__(self):
        item = {}
        item['name'] = self.name
        item['type'] = self.type.value
        item['ability'] = self.ability.value

        item['tags'] = []
        item['class'] = []
        item['align'] = []
        for tag in self.tags:
            if isinstance(tag, ItemTag):
                item['tags'].append(tag.value)
            elif isinstance(tag, ItemClass):
                item['class'].append(tag.value)
            elif isinstance(tag, ItemAlign):
                item['align'].append(tag.value)

        item['weight'] = self.weight
        item['value'] = self.value
        item['rent'] = self.rent

        item['min_level'] = self.min_level
        item['max_level'] = self.max_level
        item['ac'] = self.ac

        item['slots'] = []
        for slot in self.slots:
            item['slots'].append(slot.value)

        item['affects'] = []
        for affect in list(self.affects.items()):
            d = {}
            d[affect[0].value] = affect[1]
            item['affects'].append(d)

        item['units'] = self.units
        item['liq_units'] = self.liq_units

        item['spells'] = []
        for spell in self.spells:
            item['spells'].append(spell.value)

        item['spell_level'] = self.spell_level
        item['charge_max'] = self.charge_max
        item['charge_remain'] = self.charge_remain

        item['dice_face'] = self.dice_face
        item['dice_count'] = self.dice_count
        item['average_dmg'] = self.average_dmg

        return item
