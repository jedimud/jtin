import json
import sys
from item_type import ItemType
from item_align import ItemAlign
from item_class import ItemClass
from item_tag import ItemTag
from item_affect import ItemAffect
from item_slot import ItemSlot
from item_data import ItemData

class ItemBrief():

    def main(self):
        items = ItemData().load_items()
        self.write_brief(items)

    def load_items(self):
        try:
            with open('data/items.json', 'r') as f:
                data = json.load(f)
                f.close()
                return [] if data == None else data
        except:
            return []

    def parse_brief(self, item):

        item['brief_eq'] = ''
        item['brief_inv'] = ''

        # level
        lev = ''
        if item['min_level'] != None:
            lev = 'mL ' + str(item['min_level']) + ' '
            if item['max_level'] != None:
                lev = lev + '-' + str(item['max_level']) + ' '

        item['brief_eq'] = item['brief_eq'] + lev
        item['brief_inv'] = item['brief_inv'] + lev

        # class + align
        rests = ''
        class_tag = ''
        align_tag = ''
        for tag in item['align']:
            align_tag = align_tag + ItemAlign(tag).brief + ' '

        for tag in item['class']:
            class_tag = class_tag + ItemClass(tag).brief

        if class_tag != '':
            rests = rests + '!' + class_tag + ' '

        if align_tag != '':
            rests = rests + align_tag

        if rests == '':
            rests = '!rests '

        item['brief_eq'] = item['brief_eq'] + rests
        item['brief_inv'] = item['brief_inv'] + rests

        # weapon
        if item['dice_face'] != None and int(item['dice_face']) > 0 and item['type'] != ItemType.FIRE_WEAPON:
            wpn = str(item['dice_count']) + 'D' + str(item['dice_face']) + \
                '(' + str(item['average_dmg']) + ') '
            item['brief_eq'] = item['brief_eq'] + wpn
            item['brief_inv'] = item['brief_inv'] + wpn

        # affects
        if item['slots'].__len__() > 0:
            affects = ''
            for affect in item['affects']:
                for key in affect:
                    if int(affect[key]) > 0:
                        affects = affects + '+' + \
                            str(affect[key]) + ItemAffect[key].brief + ' '

            item['brief_eq'] = item['brief_eq'] + affects
            item['brief_inv'] = item['brief_inv'] + affects

        # ac and other attributes
        if item['ac'] != None and int(item['ac']) > 0:
            ac = '+' + str(item['ac']) + 'ac '
            item['brief_eq'] = item['brief_eq'] + ac
            item['brief_inv'] = item['brief_inv'] + ac
        if item['ac'] != None and int(item['ac']) < 0:
            ac = str(item['ac']) + 'ac '
            item['brief_eq'] = item['brief_eq'] + ac
            item['brief_inv'] = item['brief_inv'] + ac

        # type
        item_type = ItemType(item['type'])
        if item_type == ItemType.CONTAINER:
            item['brief_inv'] = item['brief_inv'] + \
                item_type.brief + '(+' + str(item['units']) + ') '
        elif item_type == ItemType.LIQ_CONTAINER:
            item['brief_inv'] = item['brief_inv'] + item_type.brief + \
                '(+' + str(item['liq_units']) + ') '
        else:
            item['brief_inv'] = item['brief_inv'] + item_type.brief

        # slots
        if item_type != ItemType.LIGHT:
            if item['slots'].__len__() > 0:
                slots = ''
                for slot in item['slots']:
                    if slots != '':
                        slots = slots + ', '
                    slots = slots + ItemSlot(slot).brief
                slots = '(' + slots + ')'

                item['brief_inv'] = item['brief_inv'] + slots

        item['brief_inv'] = item['brief_inv'].strip()
        item['brief_eq'] = item['brief_eq'].strip()

        # sac
        sac = item['sac']

        if sac > 0:
            item['brief_sac'] = '+' + str(sac) + ' sac '
        elif sac <= 0:
            item['brief_sac'] = str(sac) + ' sac '

        item['brief_limited'] = ''
        for tag in item['tags']:
            if ItemTag(tag) == ItemTag.LIMITED:
                item['brief_limited'] = '(L)'
                break
            
        item['brief_spells'] = ''
        if item['spells']:
            uniqueSpells = set(item['spells'])
            item['brief_spells'] = item['brief_spells'] + "["
            
            for indx, spell in enumerate(uniqueSpells):
                item['brief_spells'] = item['brief_spells'] + spell
                count = item['spells'].count(spell)
                if count > 1:
                    item['brief_spells'] = item['brief_spells'] + "(x" + str(count) + ")"
                if item['charge_max'] != None:
                    item['brief_spells'] = item['brief_spells'] + "(x" + str(item['charge_max']) + ")"
                if indx != len(uniqueSpells)-1:
                    item['brief_spells'] = item['brief_spells'] + ", "

            item['brief_spells'] = item['brief_spells'] + "] "
            
    def write_brief(self, items):
        briefs = {}
        for item in items:
            self.parse_brief(item)
            description = {}
            description['inventory'] = item['brief_inv']
            description['equipped'] = item['brief_eq']
            description['sac'] = item['brief_sac']
            description['limited'] = item['brief_limited']
            description['spells'] = item['brief_spells']
            description['value'] = item['value']
            briefs[item['name']] = {}
            briefs[item['name']]['description'] = description
        with open('data/item-briefs.json', 'w') as f:
            json.dump(briefs, f)


if __name__ == '__main__':
    ItemBrief().main()
