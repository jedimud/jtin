from item_data import ItemData
from item_slot import ItemSlot
from item_align import ItemAlign
from item_class import ItemClass
from item_affect import ItemAffect
import json
import os
import csv


class ItemCSV():

    def __init__(self):
        self.item_data = ItemData()

    def write_to_file(self):

        data = []

        # header

        h = 'Name,,Slot,Hold,,Min,Max,,G,N,E,,m,c,t,w,p,a,n,j,s,r,b,,STR,INT,WIS,DEX,CON,CHA,,DAMR,HITR,HP,HP_R,MN,MN_R,MV,MV_R,AC'
        data.append(h.split(','))

        # data

        for item in sorted(list({v['name']: v for v in self.item_data.load_items()}.values()), key=lambda i: i['name']):
            if item['slots'].__len__() < 1:
                continue

            row = []

            # name

            row.append(item['name'])
            row.append('')

            # slots

            slot_found = False
            slot_hold = False
            for slot in item['slots']:
                if ItemSlot(slot) != ItemSlot.HOLD:
                    if slot_hold == True:
                        raise Exception
                    row.append(slot)
                    slot_found = True
                else:
                    slot_hold = True

            if not slot_found:
                row.append('')

            if slot_hold:
                row.append(ItemSlot.HOLD)
            else:
                row.append('')

            row.append('')

            # min/max level

            row.append(item['min_level'])
            row.append(item['max_level'])
            row.append('')

            # align

            align_good = True
            align_neutral = True
            align_evil = True
            for align in item['align']:
                a = ItemAlign(align)
                if a == ItemAlign.NO_EVIL:
                    align_evil = False
                elif a == ItemAlign.NO_NEUTRAL:
                    align_neutral = False
                elif a == ItemAlign.NO_GOOD:
                    align_good = False

            row.append('X' if align_good else '')
            row.append('X' if align_neutral else '')
            row.append('X' if align_evil else '')
            row.append('')

            # class

            for cl in ItemClass:
                for _cl in item['class']:
                    if cl == ItemClass(_cl):
                        row.append('')
                        break
                else:
                    row.append('X')

            row.append('')

            # affects

            affect_found = False
            for aff in [ItemAffect.STR, ItemAffect.INT, ItemAffect.WIS,
                        ItemAffect.DEX, ItemAffect.CON, ItemAffect.CHARISMA]:
                matched = False
                for _aff in item['affects']:
                    for key in _aff:
                        if aff == ItemAffect(key):
                            row.append(_aff[key])
                            affect_found = True
                            matched = True
                if not matched:
                    row.append('')

            row.append('')

            for aff in [ItemAffect.DAMROLL, ItemAffect.HITROLL,
                        ItemAffect.HIT, ItemAffect.HIT_REGEN,
                        ItemAffect.MANA, ItemAffect.MANA_REGEN,
                        ItemAffect.MOVE, ItemAffect.MOVE_REGEN]:
                matched = False
                for _aff in item['affects']:
                    for key in _aff:
                        if aff == ItemAffect(key):
                            row.append(_aff[key])
                            affect_found = True
                            matched = True
                if not matched:
                    row.append('')

            if item['ac'] != None and int(item['ac']) > 0:
                row.append(item['ac'])
                affect_found = True
            else:
                row.append('')

            # cr

            if affect_found:
                data.append(row)

        with open('data/item-wearables.csv', mode='w') as f:
            writer = csv.writer(
                f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)


if __name__ == '__main__':
    ItemCSV().write_to_file()
