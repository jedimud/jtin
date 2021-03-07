import json


class ItemData():

    def load_items(self):
        try:
            with open('data/items.json', 'r') as f:
                data = json.load(f)
                f.close()
                return [] if data == None else data
        except:
            return []

    def write_item_json(self, items):
        items_arr = []
        for item in items:
            items_arr.append(item.__dict__())

        with open('data/items.json', 'w+') as f:
            json.dump(items_arr, f)
