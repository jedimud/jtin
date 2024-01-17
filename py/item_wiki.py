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

    def parse_item(self, item):
        data = {}
        data['detail'] = {}
        data['brief'] = {}
        data['brief']['line'] = ""
        #  rests-brief, affects-brief, type-brief, spells-brief
        # affects, class, align, type, slot, spells

        # level
        
        data['detail']['min_level'] = item['min_level']
        data['detail']['max_level'] = item['max_level']
        ml = ""
        if item['min_level'] != None:
            ml += 'mL ' + str(item['min_level']) + ' '
            if item['max_level'] != None:
                ml += '-' + str(item['max_level']) + ' '
        data['brief']['line'] += ml
        data['brief']['ml'] = ml

        # class + align
        rests = ''
        class_tag = ''
        align_tag = ''
        for tag in item['align']:
            align_tag += ItemAlign(tag).brief + ' '

        data['detail']['class']['MAGE'] = True
        data['detail']['class']['CLER'] = True
        data['detail']['class']['THF'] = True
        data['detail']['class']['WAR'] = True
        data['detail']['class']['PAL'] = True
        data['detail']['class']['APAL'] = True
        data['detail']['class']['NINJA'] = True
        data['detail']['class']['JEDI'] = True
        data['detail']['class']['SOHEI'] = True
        data['detail']['class']['RANGER'] = True
        data['detail']['class']['BARD'] = True
        for tag in item['class']:
            if (tag == ItemClass.NO_MAGE.value):
                data['detail']['class']['MAGE'] = False
            elif (tag == ItemClass.NO_CLER.value):
                data['detail']['class']['CLER'] = False
            elif (tag == ItemClass.NO_THF.value):
                data['detail']['class']['THF'] = False
            elif (tag == ItemClass.NO_WAR.value):
                data['detail']['class']['WAR'] = False
            elif (tag == ItemClass.NO_PAL.value):
                data['detail']['class']['PAL'] = False
            elif (tag == ItemClass.NO_APAL.value):
                data['detail']['class']['APAL'] = False
            elif (tag == ItemClass.NO_NINJA.value):
                data['detail']['class']['NINJA'] = False
            elif (tag == ItemClass.NO_JEDI.value):
                data['detail']['class']['JEDI'] = False
            elif (tag == ItemClass.NO_SOHEI.value):
                data['detail']['class']['SOHEI'] = False
            elif (tag == ItemClass.NO_RANGER.value):
                data['detail']['class']['RANGER'] = False
            elif (tag == ItemClass.NO_BARD.value):
                data['detail']['class']['BARD'] = False
            class_tag += ItemClass(tag).brief

        if class_tag != '':
            rests += '!' + class_tag + ' '

        if align_tag != '':
            rests += align_tag

        if rests == '':
            rests = '!rests '

        data['brief']['rests'] = rests
        data['brief']['line'] += rests
        data['detail']['class'] = class_tag
        data['detail']['align'] = align_tag
        

    #     # weapon
    #     if item['dice_face'] != None and int(item['dice_face']) > 0 and item['type'] != ItemType.FIRE_WEAPON:
    #         wpn = str(item['dice_count']) + 'D' + str(item['dice_face']) + \
    #             '(' + str(item['average_dmg']) + ') '
    #         item['brief_eq'] = item['brief_eq'] + wpn
    #         item['brief_inv'] = item['brief_inv'] + wpn

    #     # affects
    #     if item['slots'].__len__() > 0:
    #         affects = ''
    #         for affect in item['affects']:
    #             for key in affect:
    #                 if int(affect[key]) > 0:
    #                     affects = affects + '+' + \
    #                         str(affect[key]) + ItemAffect[key].brief + ' '
    #                 else:
    #                     affects = affects + \
    #                         str(affect[key]) + ItemAffect[key].brief + ' '

    #         item['brief_eq'] = item['brief_eq'] + affects
    #         item['brief_inv'] = item['brief_inv'] + affects

    #     # ac and other attributes
    #     if item['ac'] != None and int(item['ac']) > 0:
    #         ac = '+' + str(item['ac']) + 'ac '
    #         item['brief_eq'] = item['brief_eq'] + ac
    #         item['brief_inv'] = item['brief_inv'] + ac
    #     if item['ac'] != None and int(item['ac']) < 0:
    #         ac = str(item['ac']) + 'ac '
    #         item['brief_eq'] = item['brief_eq'] + ac
    #         item['brief_inv'] = item['brief_inv'] + ac

    #     # type
    #     item_type = ItemType(item['type'])
    #     if item_type == ItemType.CONTAINER:
    #         item['brief_inv'] = item['brief_inv'] + \
    #             item_type.brief + '(+' + str(item['units']) + ') '
    #     elif item_type == ItemType.LIQ_CONTAINER:
    #         item['brief_inv'] = item['brief_inv'] + item_type.brief + \
    #             '(+' + str(item['liq_units']) + ') '
    #     else:
    #         item['brief_inv'] = item['brief_inv'] + item_type.brief

    #     # slots
    #     if item_type != ItemType.LIGHT:
    #         if item['slots'].__len__() > 0:
    #             slots = ''
    #             for slot in item['slots']:
    #                 if slots != '':
    #                     slots = slots + ', '
    #                 slots = slots + ItemSlot(slot).brief
    #             slots = '(' + slots + ')'

    #             item['brief_inv'] = item['brief_inv'] + slots

    #     item['brief_inv'] = item['brief_inv'].strip()
    #     item['brief_eq'] = item['brief_eq'].strip()

    #     # sac
    #     sac = item['sac']

    #     if sac > 0:
    #         item['brief_sac'] = '+' + str(sac) + ' sac '
    #     elif sac <= 0:
    #         item['brief_sac'] = str(sac) + ' sac '

    #     item['brief_limited'] = ''
    #     for tag in item['tags']:
    #         if ItemTag(tag) == ItemTag.LIMITED:
    #             item['brief_limited'] = '(L)'
    #             break
            
    #     item['brief_spells'] = ''
    #     if item['spells']:
    #         uniqueSpells = set(item['spells'])
    #         item['brief_spells'] = item['brief_spells'] + "["
            
    #         for indx, spell in enumerate(uniqueSpells):
    #             item['brief_spells'] = item['brief_spells'] + spell
    #             count = item['spells'].count(spell)
    #             if count > 1:
    #                 item['brief_spells'] = item['brief_spells'] + "(x" + str(count) + ")"
    #             if item['charge_max'] != None:
    #                 item['brief_spells'] = item['brief_spells'] + "(x" + str(item['charge_max']) + ")"
    #             if indx != len(uniqueSpells)-1:
    #                 item['brief_spells'] = item['brief_spells'] + ", "

    #         item['brief_spells'] = item['brief_spells'] + "] "
        
        return data
            
    def write_brief(self, items):
        data = {}
        for item in items:
            key = item['name']
            data[key] = self.parse_item(item)
        with open('data/item-wikis.json', 'w') as f:
            json.dump(data, f)


if __name__ == '__main__':
    ItemBrief().main()
