import json
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
            lev = str(item['min_level']) + ' '
            if item['max_level'] != None:
                lev = lev + '-' + str(item['max_level']) + ' '

        item['brief_ml'] = lev.strip()
        item['brief_eq'] = item['brief_eq'] + 'mL ' + lev
        item['brief_inv'] = item['brief_inv'] + 'mL ' + lev

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

        item['brief_rests'] = rests.strip()
        item['brief_eq'] = item['brief_eq'] + rests
        item['brief_inv'] = item['brief_inv'] + rests

        # weapon
        affects = ''
        if item['dice_face'] != None and int(item['dice_face']) > 0 and item['type'] != ItemType.FIRE_WEAPON:
            wpn = str(item['dice_count']) + 'D' + str(item['dice_face']) + \
                '(' + str(item['average_dmg']) + ') '
            item['brief_eq'] = item['brief_eq'] + wpn
            item['brief_inv'] = item['brief_inv'] + wpn
            affects += wpn

        # affects
        if item['slots'].__len__() > 0:
            for affect in item['affects']:
                for key in affect:
                    if int(affect[key]) > 0:
                        affects = affects + '+' + \
                            str(affect[key]) + ItemAffect[key].brief + ' '
                    else:
                        affects = affects + \
                            str(affect[key]) + ItemAffect[key].brief + ' '

        # ac and other attributes
        ac = ''
        if item['ac'] != None and int(item['ac']) > 0:
            ac = '+' + str(item['ac']) + 'ac '
            item['brief_eq'] = item['brief_eq'] + ac
            item['brief_inv'] = item['brief_inv'] + ac
        if item['ac'] != None and int(item['ac']) < 0:
            ac = str(item['ac']) + 'ac '
            item['brief_eq'] = item['brief_eq'] + ac
            item['brief_inv'] = item['brief_inv'] + ac
        affects += ac
        item['brief_affects'] = affects

        # type
        type = ''
        item_type = ItemType(item['type'])
        if item_type == ItemType.CONTAINER:
            type = item_type.brief + '(+' + str(item['units']) + ') '
        elif item_type == ItemType.LIQ_CONTAINER:
            type = item_type.brief + '(+' + str(item['liq_units']) + ') '
        else:
            type = item_type.brief
        item['brief_inv'] += type

        # slots
        slots = ''
        if item_type != ItemType.LIGHT:
            if item['slots'].__len__() > 0:
                for slot in item['slots']:
                    if slots != '':
                        slots = slots + ', '
                    slots = slots + ItemSlot(slot).brief
                slots = '(' + slots + ')'

                item['brief_inv'] += slots

        item['brief_inv'] = item['brief_inv'].strip()
        item['brief_eq'] = item['brief_eq'].strip()
        item['brief_type'] = type + slots.strip()

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
            
        spells = item['brief_spells'] = ''
        if item['spells']:
            uniqueSpells = sorted(set(item['spells']))
            
            for indx, spell in enumerate(uniqueSpells):
                spells += spell
                count = item['spells'].count(spell)
                if count > 1:
                    spells += "(x" + str(count) + ")"
                if item['charge_max'] != None:
                    spells += "(x" + str(item['charge_max']) + ")"
                if indx != len(uniqueSpells)-1:
                    spells += ", "

            if (spells != ''): 
                spells = "[" + spells + "]"
            item['brief_spells'] = spells
            
    def write_brief(self, items):
        briefs = {}
        for item in items:
            self.parse_brief(item)
            description = {}
            description['ml'] = item['brief_ml'].strip()
            description['rests'] = item['brief_rests'].strip()
            description['affects'] = item['brief_affects'].strip()
            description['type'] = item['brief_type'].strip()
            description['spells'] = item['brief_spells'].strip()
            description['tag'] = (item['name'].lower() + ': ' + item['brief_inv'] + ' ' + item['brief_spells']).strip()
            description['sac'] = (item['name'].lower() + ': ' + item['brief_sac'] + item['brief_limited']).strip()
            key = item['name']
            briefs[key] = {}
            briefs[key]['description'] = description
        with open('data/wiki-item-briefs.json', 'w') as f:
            json.dump(briefs, f)


if __name__ == '__main__':
    ItemBrief().main()
