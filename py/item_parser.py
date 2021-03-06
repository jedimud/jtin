from item_type import ItemType
from item_ability import ItemAbility
from item_tag import ItemTag
from item_affect import ItemAffect
from item_slot import ItemSlot
from item_class import ItemClass
from item_align import ItemAlign
from item_spell import ItemSpell
from item_race import ItemRace
from item import Item
from item_data import ItemData
import json
import os


class ItemParser():

    def __init__(self):
        self.item_data = ItemData()

    def parse_and_archive_file(self, fname):
        lines = []
        try:
            lines = self.read_file(fname)
        except:
            pass

        if lines.__len__() > 0:
            items = self.parse_file(lines)
            existingItems = self.item_data.load_items()
            self.item_data.write_item_json(items, existingItems)
            self.archive_data(fname, lines)

    def parse_file(self, lines):
        line_break = "-----"
        desc_break = "+++++"
        error_break = "ERROR - IGNORE THIS RECORD"
        sub_lines = []
        items = []
        is_desc = False
        for line in lines:
            if line.strip().__len__() == 0:
                pass
            elif error_break == line:
                is_desc = False
                sub_lines.clear()
            elif line_break == line:
                if (sub_lines.__len__() > 0):
                    item = self.parse_lines(sub_lines)
                    items.append(item)
                sub_lines.clear()
                is_desc = False
            elif desc_break == line:
                is_desc = True
            elif not is_desc:
                sub_lines.append(line)

        if (sub_lines.__len__() > 0):
            item = self.parse_lines(sub_lines)
            items.append(item)

        return items

    def parse_lines(self, lines):
        item = Item()
        for line in lines:
            self.parse_line(line, item)

        self.validate(item)
        self.update_sac(item)

        return item

    def parse_line(self, line, item):
        line = line.strip()
        if line.startswith("Object '"):
            self.parse_name_type(line, item)
        elif line.startswith("Item will give you following abilities:"):
            self.parse_ability(line, item)
        elif line.startswith("Item is: "):
            self.parse_tags(line, item)
        elif line.startswith("Weight: "):
            self.parse_meta(line, item)
        elif line.startswith("Can affect you as :"):
            pass
        elif line.startswith("Affects: "):
            self.parse_affects(line, item)
        elif line.startswith("Item slot: "):
            self.parse_slot(line, item)
        elif line.startswith("Damage Dice is '") and line.endswith(" charges."):
            self.parse_spell_damage_dice(line, item)
        elif line.startswith("Damage Dice is '"):
            self.parse_damage_dice(line, item)
        elif line.startswith("AC-apply is "):
            self.parse_ac_apply(line, item)
        elif line.startswith("This STAFF casts: "):
            self.parse_weapon_cast(line, item)
        elif line.startswith("This WAND casts: "):
            self.parse_weapon_cast(line, item)
        elif line.startswith("This SCROLL casts: "):
            self.parse_item_cast(line, item)
        elif line.startswith("This POTION casts: "):
            self.parse_item_cast(line, item)
        elif line.startswith("It has ") and line.endswith(" remaining."):
            self.parse_charge(line, item)
        elif line.startswith("This item has a maximum level of "):
            self.parse_max_level(line, item)
        elif line.startswith("It can hold approximately ") and line.endswith("units of liquid."):
            self.parse_liq_container(line, item)
        elif line.startswith("It can hold approximately "):
            self.parse_container(line, item)
        else:
            raise Exception("unknown line: " + line)

    def parse_name_type(self, line, item):
        """Object 'a Hover Board', Item type: AIRSHIP"""
        name = line[8:]
        i = name.rfind("'")
        name = name[:i]
        item.name = name

        i = line.find("', Item type:") + 14
        item.type = ItemType(line[i:])

        parsed = "Object '"+item.name+"', Item type: " + item.type.value
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_ability(self, line, item):
        """Item will give you following abilities:  NOBITS"""
        item.ability = ItemAbility(line[41:])

        parsed = "Item will give you following abilities:  " + item.ability.value
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_tags(self, line, item):
        """Item is: GLOW HUM INVIS MAG !DONATE !JUNK UNIQUE INSURED"""
        tokens = line[9:].split(' ')

        item.tags.clear
        for token in tokens:
            found = False
            try:
                tag = ItemTag(token)
                item.tags.append(tag)
                found = True
            except:
                pass

            try:
                tag = ItemClass(token)
                item.tags.append(tag)
                found = True
            except:
                pass

            try:
                tag = ItemRace(token)
                item.tags.append(tag)
                found = True
            except:
                pass

            try:
                tag = ItemAlign(token)
                item.tags.append(tag)
                found = True
            except:
                pass

            if not found:
                raise Exception("unknown tag: " + token)

        parsed = "Item is:"
        for tag in item.tags:
            parsed = parsed + " " + tag.value

        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_meta(self, line, item):
        """Weight: 5, Value: 10000, Rent: 1000, Min. level: 0"""
        weight = line[8:]
        i = weight.find(",")
        item.weight = int(weight[0:i])

        i = line.find(", Value:") + 9
        value = line[i:]
        i = value.find(",")
        item.value = int(value[:i])

        i = line.find(", Rent: ") + 8
        rent = line[i:]
        i = rent.find(",")
        item.rent = int(rent[:i])

        i = line.find(", Min. level: ") + 14
        item.min_level = int(line[i:])

        parsed = "Weight: " + str(item.weight) + ", Value: " + \
            str(item.value) + ", Rent: " + str(item.rent) + \
            ", Min. level: " + str(item.min_level)
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_affects(self, line, item):
        """Affects: CON By 2"""
        i = line.find("Affects: ") + 9
        tokens = line[i:].split(" ")
        affect = ItemAffect(tokens[0])
        item.affects[affect] = int(tokens[2])

        affect = list(item.affects.items())[-1]
        parsed = "Affects: " + affect[0].value + " By " + str(affect[1])
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_slot(self, line, item):
        """Item slot: Feet"""
        slot = ItemSlot(line[11:])
        if not item.slots.__contains__(slot):
            item.slots.append(slot)
        else:
            raise Exception

        parsed = "Item slot: " + item.slots[-1].value
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_damage_dice(self, line, item):
        """Damage Dice is '6D6' for an average per-round damage of 21.0."""
        count = line[16:]
        i = count.find("D")
        item.dice_count = int(count[:i])

        face = line[16:]
        i = face.find("D") + 1
        face = face[i:]
        i = face.find("'")
        item.dice_face = int(face[:i])

        i = line.find("damage of ") + 10
        avg = line[i:]
        i = avg.rfind(".")
        item.average_dmg = float(avg[:i])

        parsed = "Damage Dice is '" + str(item.dice_count) + \
            "D" + str(item.dice_face) + "' for an average per-round damage of " + \
            str(item.average_dmg) + "."
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_spell_damage_dice(self, line, item):
        """Damage Dice is '3D5' This weapon currently has 15 of a maximum 6 charges."""

        count = line[16:]
        i = count.find("D")
        item.dice_count = int(count[:i])

        face = line[16:]
        i = face.find("D") + 1
        face = face[i:]
        i = face.find("'")
        item.dice_face = int(face[:i])

        i = line.find(" maximum ") + 9
        max = line[i:]
        i = max.find(" charges.")
        item.charge_max = int(max[:i])

        i = line.find(" currently has ") + 15
        remain = line[i:]
        i = remain.find(" of a ")
        item.charge_remain = int(remain[:i])

        parsed = "Damage Dice is '" + str(item.dice_count) + "D" + str(item.dice_face) + \
            "' This weapon currently has " + str(item.charge_remain) + \
            " of a maximum " + str(item.charge_max) + " charges."
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_ac_apply(self, line, item):
        """AC-apply is 3"""
        item.ac = int(line[12:])
        parsed = "AC-apply is " + str(item.ac)
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_weapon_cast(self, line, item):
        """This STAFF casts: call lightning of level 20"""

        i = line.find("casts: ") + 7
        spell = line[i:]
        i = spell.find(" of level ")
        spell = spell[:i]
        item.spells.append(ItemSpell(spell))

        i = line.find(" of level ") + 10
        item.spell_level = int(line[i:])

        parsed = "This " + item.type.value + " casts: " + \
            item.spells[-1].value + " of level " + str(item.spell_level)
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_item_cast(self, line, item):
        """This SCROLL casts:  Level 12 of word of recall control weather control weather"""
        i = line.find("casts:  Level ") + 14
        level = line[i:]
        i = level.find(" of ")
        item.spell_level = int(level[:i])

        i = line.find("casts:  Level ") + 14
        spells = line[i:]
        i = spells.find(" of ") + 4
        spells = spells[i:]

        while spells.__len__() > 0:
            found = False
            for sp in list(ItemSpell):
                if (spells.startswith(sp.value)):
                    item.spells.append(sp)
                    i = sp.value.__len__()
                    spells = spells[i:].strip()
                    found = True
                    continue
            if not found:
                raise Exception("unknown spell " + spells)

        parsed = "This " + item.type.value + \
            " casts:  Level " + str(item.spell_level) + " of"
        for sp in item.spells:
            parsed = parsed + " " + sp.value
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_charge(self, line, item):
        """It has 3 maximum charges and 3 remaining."""

        max = line[7:]
        i = max.find(" maximum")
        item.charge_max = int(max[:i])

        i = line.find(" and ") + 5
        remain = line[i:]
        i = remain.find(" remaining")
        item.charge_remain = int(remain[:i])

        parsed = "It has " + str(item.charge_max) + \
            " maximum charges and " + str(item.charge_remain) + " remaining."
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_max_level(self, line, item):
        """This item has a maximum level of 20."""

        i = line.find("level of ") + 9
        max = line[i:]
        i = max.find(".")
        item.max_level = int(max[:i])

        parsed = "This item has a maximum level of " + \
            str(item.max_level) + "."
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_container(self, line, item):
        """It can hold approximately 200 units."""

        i = line.find("approximately ") + 14
        units = line[i:]
        i = units.find(" units.")
        item.units = int(units[:i])

        parsed = "It can hold approximately " + str(item.units) + " units."
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def parse_liq_container(self, line, item):
        """It can hold approximately 8 units of liquid."""

        i = line.find("approximately ") + 14
        units = line[i:]
        i = units.find(" units")
        item.liq_units = int(units[:i])

        parsed = "It can hold approximately " + \
            str(item.liq_units) + " units of liquid."
        assert line == parsed, "[" + line + "] != [" + parsed + "]"

    def validate(self, item):
        assert item.name != ""
        assert item.type != ""

    def update_sac(self, item):
        for aff in list(item.affects.items()):
            if ItemAffect(aff[0]).sac:
                item.sac = item.sac + int(aff[1])

    def read_file(self, fname):
        with open(fname) as f:
            lines = [line.rstrip() for line in f]
            f.close()
            return lines

    def archive_data(self, fname, lines):
        with open(fname + ".arc", "a") as f:
            for line in lines:
                f.write(line)
                f.write("\r")
            f.close()
        os.remove(fname)

    def load_items(self):
        try:
            with open("data/items.json", "r") as f:
                data = json.load(f)
                f.close()
                return [] if data == None else data
        except:
            return []


if __name__ == '__main__':
    ItemParser().parse_and_archive_file("logs/ident.log")
