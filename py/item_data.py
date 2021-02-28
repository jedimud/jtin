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

    def write_item_json(self, items, existing_items):
        for item in items:
            existing_items.append(item.__dict__())

        with open('data/items.json', 'w+') as f:
            json.dump(existing_items, f)
