import unittest


from item_parser import ItemParser
from item import Item
from item_type import ItemType
from item_ability import ItemAbility


class TestItemParser(unittest.TestCase):

    def test_upper(self):
        line = "Object 'a Hover Board', Item type: AIRSHIP"
        item = Item()
        ItemParser().parse_line(line, item)

        self.assertEqual(item.name, "a Hover Board")
        self.assertEqual(item.type, ItemType.AIRSHIP)
        self.assertEqual(item.ability, ItemAbility.NOBITS)


if __name__ == '__main__':
    unittest.main()
