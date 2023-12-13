from item_data import ItemData
from item_slot import ItemSlot
from item_align import ItemAlign
from item_class import ItemClass
from item_affect import ItemAffect
from item_tag import ItemTag
import json
import os
import csv


class ItemSacCSV():

    def __init__(self):
        self.item_data = ItemData()

    def write_to_file(self):

        data = []

        # header

        h = 'Name,,Limited,Sac'
        data.append(h.split(','))

        # data

        for item in sorted(list({v['name']: v for v in self.item_data.load_items()}.values()), key=lambda i: i['sac'], reverse=True):
            row = []

            # name

            row.append(item['name'])
            row.append('')

            # limited

            found = False
            for tag in item['tags']:
                if ItemTag(tag) == ItemTag.LIMITED:
                    row.append('X')
                    found = True
                    break

            if not found:
                row.append('')

            # sac

            sac = item['sac']
            row.append(sac)
            row.append('')

            # cr

            if sac > 0:
                data.append(row)

        with open('data/item-sac.csv', mode='w') as f:
            writer = csv.writer(
                f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)


if __name__ == '__main__':
    ItemSacCSV().write_to_file()
