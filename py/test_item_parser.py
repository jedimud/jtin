import unittest


from item_parser import ItemParser
from item import Item
from item_type import ItemType
from item_tag import ItemTag
from item_ability import ItemAbility
from item_slot import ItemSlot
from item_class import ItemClass
from item_align import ItemAlign
from item_spell import ItemSpell
from item_affect import ItemAffect
from item_race import ItemRace


class TestItemParser(unittest.TestCase):

    def test_upper(self):
        item = self.read_item_from_file("a-hover-board")

        self.assertEqual(item.name, "a Hover Board")
        self.assertEqual(item.type, ItemType.AIRSHIP)
        self.assertEqual(item.ability, ItemAbility.NOBITS)

    def test_parse_file__a_hover_board(self):
        actual = self.read_item_from_file("a-hover-board")

        item = Item()
        item.name = "a Hover Board"
        item.type = ItemType.AIRSHIP
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemTag.NO_JUNK)
        item.tags.append(ItemTag.UNIQUE)
        item.tags.append(ItemTag.INSURED)
        item.weight = 5
        item.value = 10000
        item.rent = 1000
        item.min_level = 0
        item.affects[ItemAffect.CON] = 2
        # item.constitution = 2
        item.slots.append(ItemSlot.FEET)

        self.assert_equals(item, actual)

    def test_parse_file__a_red_wyvern_scale_bracelet(self):
        actual = self.read_item_from_file("a-red-wyvern-scale-bracelet")

        item = Item()
        item.name = "a red wyvern scale bracelet"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemTag.NO_JUNK)
        item.tags.append(ItemTag.UNIQUE)
        item.tags.append(ItemTag.INSURED)
        item.weight = 3
        item.value = 1500
        item.rent = 1000
        item.min_level = 0
        item.affects[ItemAffect.HITROLL] = 2
        item.affects[ItemAffect.DAMROLL] = 1
        item.ac = 3
        item.slots.append(ItemSlot.WRIST)

        self.assert_equals(item, actual)

    def test_parse_file__a_dinosaur_skin_cape(self):
        actual = self.read_item_from_file("a-dinosaur-skin-cape")

        item = Item()
        item.name = "a Dinosaur skin cape"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemTag.NO_JUNK)
        item.tags.append(ItemTag.UNIQUE)
        item.tags.append(ItemTag.INSURED)
        item.weight = 10
        item.value = 50
        item.rent = 5000
        item.min_level = 10
        item.affects[ItemAffect.DAMROLL] = 1
        item.affects[ItemAffect.DEX] = -1
        item.ac = 10
        item.slots.append(ItemSlot.ABOUT_BODY)

        self.assert_equals(item, actual)

    def test_parse_file__some_spiked_sleeves(self):
        actual = self.read_item_from_file("some-spiked-sleeves")

        item = Item()
        item.name = "some spiked sleeves"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 10
        item.value = 400
        item.rent = 100
        item.min_level = 0
        item.affects[ItemAffect.HITROLL] = -1
        item.ac = 2
        item.slots.append(ItemSlot.ARMS)

        self.assert_equals(item, actual)

    def test_parse_file__a_garnet_ring(self):
        actual = self.read_item_from_file("a-garnet-ring")

        item = Item()
        item.name = "a garnet ring"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 1
        item.value = 6000
        item.rent = 2000
        item.min_level = 0
        item.affects[ItemAffect.MANA] = 10
        item.affects[ItemAffect.MOVE_REGEN] = -4
        item.ac = 1
        item.slots.append(ItemSlot.RING)

        self.assert_equals(item, actual)

    def test_parse_file__a_ring_of_delusion(self):
        actual = self.read_item_from_file("a-ring-of-delusion")

        item = Item()
        item.name = "a ring of delusion"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 5
        item.value = 225
        item.rent = 100
        item.min_level = 0
        item.affects[ItemAffect.MANA] = 1
        item.affects[ItemAffect.HIT] = 1
        item.ac = 2
        item.slots.append(ItemSlot.RING)
        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_ring_of_the_guardian(self):
        actual = self.read_item_from_file("a-ring-of-the-guardian")

        item = Item()
        item.name = "a ring of the guardian"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemAlign.NEUTRAL)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 2
        item.value = 1500
        item.rent = 5500
        item.min_level = 0
        item.affects[ItemAffect.DAMROLL] = 1
        item.affects[ItemAffect.HIT] = 2
        item.ac = 2
        item.slots.append(ItemSlot.RING)

        self.assert_equals(item, actual)

    def test_parse_file__a_gallery_champion_crown(self):
        actual = self.read_item_from_file("a-gallery-champion-crown")

        item = Item()
        item.name = "a Gallery Champion crown"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.BLESS)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 5
        item.value = 10000
        item.rent = 2500
        item.min_level = 10
        item.affects[ItemAffect.HITROLL] = 1
        item.affects[ItemAffect.HIT_REGEN] = 10
        item.ac = -4
        item.slots.append(ItemSlot.HEAD)

        self.assert_equals(item, actual)

    def test_parse_file__a_set_of_smooth_leggings(self):
        actual = self.read_item_from_file("a-set-of-smooth-leggings")

        item = Item()
        item.name = "a set of smooth leggings"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 10
        item.value = 1000
        item.rent = 200
        item.min_level = 0
        item.affects[ItemAffect.STR] = -1
        item.ac = 10
        item.slots.append(ItemSlot.LEGS)

        self.assert_equals(item, actual)

    def test_parse_file__a_white_leather_dress(self):
        actual = self.read_item_from_file("a-white-leather-dress")

        item = Item()
        item.name = "a white leather dress"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_JEDI)
        item.tags.append(ItemTag.LIMITED)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 4
        item.value = 5500
        item.rent = 2750
        item.min_level = 15
        item.affects[ItemAffect.MANA] = 20
        item.affects[ItemAffect.STR] = -1
        item.ac = 12
        item.slots.append(ItemSlot.ON_BODY)

        self.assert_equals(item, actual)

    def test_parse_file__ben_kenobis_medallion(self):
        actual = self.read_item_from_file("ben-kenobis-medallion")

        item = Item()
        item.name = "Ben Kenobi's medallion"
        item.type = ItemType.OTHER
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 1
        item.value = 8500
        item.rent = 8000
        item.min_level = 0
        item.affects[ItemAffect.WIS] = 3
        item.affects[ItemAffect.MANA] = 15
        item.slots.append(ItemSlot.NECK)

        self.assert_equals(item, actual)

    def test_parse_file__a_pair_of_thin_white_gloves(self):
        actual = self.read_item_from_file("a-pair-of-thin-white-gloves")

        item = Item()
        item.name = "a pair of thin white gloves"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.NO_DROP)
        item.tags.append(ItemAlign.NO_NEUTRAL)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_JEDI)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 2
        item.value = 500
        item.rent = 250
        item.min_level = 0
        item.ac = 3
        item.affects[ItemAffect.HITROLL] = -1
        item.affects[ItemAffect.DAMROLL] = 1
        item.slots.append(ItemSlot.HANDS)

        self.assert_equals(item, actual)

    def test_parse_file__a_two_sided_leather_belt(self):
        actual = self.read_item_from_file("a-two-sided-leather-belt")

        item = Item()
        item.name = "a two sided leather belt"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemTag.UNIQUE)
        item.weight = 1
        item.value = 50
        item.rent = 0
        item.min_level = 0
        item.ac = 1
        item.affects[ItemAffect.STR] = 1
        item.affects[ItemAffect.CHARISMA] = 1
        item.slots.append(ItemSlot.WAIST)

        self.assert_equals(item, actual)

    def test_parse_file__the_map_makers_compass(self):
        actual = self.read_item_from_file("the-map-makers-compass")

        item = Item()
        item.name = "the Map maker's compass"
        item.type = ItemType.LIGHT
        item.ability = ItemAbility.NOBITS
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 7000
        item.rent = 3500
        item.min_level = 0

        item.affects[ItemAffect.MOVE] = 15
        item.affects[ItemAffect.AGE] = 5

        item.slots.append(ItemSlot.LIGHT)

        self.assert_equals(item, actual)

    def test_parse_file__an_old_leather_belt(self):
        actual = self.read_item_from_file("an-old-leather-belt")

        item = Item()
        item.name = "an old leather belt"
        item.type = ItemType.WORN
        item.ability = ItemAbility.INVIS
        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 5000
        item.rent = 1600
        item.min_level = 0

        item.affects[ItemAffect.STR] = 1
        item.affects[ItemAffect.WIS] = 1

        item.slots.append(ItemSlot.WAIST)

        self.assert_equals(item, actual)

    def test_parse_file__julians_blade(self):
        actual = self.read_item_from_file("julians-blade")

        item = Item()
        item.name = "Julian's blade"
        item.type = ItemType.WEAPON
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 18
        item.value = 25000
        item.rent = 12500
        item.min_level = 0

        item.dice_count = 4
        item.dice_face = 5
        item.average_dmg = 12.0
        item.affects[ItemAffect.HITROLL] = 2
        item.affects[ItemAffect.DAMROLL] = 1

        item.slots.append(ItemSlot.WIELD)

        self.assert_equals(item, actual)

    def test_parse_file__a_paladins_shield_of_faith(self):
        actual = self.read_item_from_file("a-paladins-shield-of-faith")

        item = Item()
        item.name = "a Paladin's Shield of Faith"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.BLESS)
        item.tags.append(ItemAlign.NO_EVIL)
        item.tags.append(ItemAlign.NO_NEUTRAL)
        item.tags.append(ItemAlign.GOOD)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_APAL)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemClass.NO_JEDI)
        item.tags.append(ItemClass.NO_SOHEI)
        item.tags.append(ItemClass.NO_RANGER)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 20
        item.value = 3000
        item.rent = 150
        item.min_level = 6
        item.ac = 5

        item.affects[ItemAffect.HIT] = 5
        item.affects[ItemAffect.HIT_REGEN] = 2

        item.slots.append(ItemSlot.SHIELD)

        self.assert_equals(item, actual)

    def test_parse_file__a_raft(self):
        actual = self.read_item_from_file("a-raft")

        item = Item()
        item.name = "a raft"
        item.type = ItemType.BOAT
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemTag.UNIQUE)
        item.tags.append(ItemTag.ASSM)

        item.weight = 75
        item.value = 400
        item.rent = 0
        item.min_level = 0

        self.assert_equals(item, actual)

    def test_parse_file__a_mands_diamond_ring(self):
        actual = self.read_item_from_file("a-mans-diamond-ring")

        item = Item()
        item.name = "a man's diamond ring"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemAlign.EVIL)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemAlign.NO_GOOD)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_PAL)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemTag.LIMITED)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 4000
        item.rent = 4000
        item.min_level = 15
        item.ac = 0

        item.affects[ItemAffect.MANA] = 6
        item.affects[ItemAffect.DAMROLL] = 1

        item.slots.append(ItemSlot.RING)

        self.assert_equals(item, actual)

    def test_parse_file__a_yellow_potion(self):
        actual = self.read_item_from_file("a-yellow-potion")

        item = Item()
        item.name = "a yellow potion"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 2000
        item.rent = 1000
        item.min_level = 0

        item.spell_level = 15
        item.spells.append(ItemSpell.STRENGTH)
        item.spells.append(ItemSpell.BLINDNESS)

        self.assert_equals(item, actual)

    def test_parse_file__a_scroll_of_recall(self):
        actual = self.read_item_from_file("a-scroll-of-recall")

        item = Item()
        item.name = "a scroll of recall"
        item.type = ItemType.SCROLL
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)
        item.tags.append(ItemTag.ASSM)

        item.weight = 4
        item.value = 2400
        item.rent = 600
        item.min_level = 0

        item.spell_level = 12
        item.spells.append(ItemSpell.WORD_OF_RECALL)
        item.spells.append(ItemSpell.CONTROL_WEATHER)
        item.spells.append(ItemSpell.CONTROL_WEATHER)

        self.assert_equals(item, actual)

    def test_parse_file__sims_pineapple_tart(self):
        actual = self.read_item_from_file("sims-pineapple-tart")

        item = Item()
        item.name = "Sim's Pineapple Tart"
        item.type = ItemType.FOOD
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 20
        item.rent = 10
        item.min_level = 0

        self.assert_equals(item, actual)

    def test_parse_file__a_sturdy_beltpack(self):
        actual = self.read_item_from_file("a-sturdy-beltpack")

        item = Item()
        item.name = "a sturdy beltpack"
        item.type = ItemType.CONTAINER
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.UNIQUE)

        item.weight = 5
        item.value = 5000
        item.rent = 1000
        item.min_level = 0

        item.units = 200
        item.slots.append(ItemSlot.WAIST)

        self.assert_equals(item, actual)

    def test_parse_file__a_block_of_krrf(self):
        actual = self.read_item_from_file("a-block-of-krrf")

        item = Item()
        item.name = "a block of krrf"
        item.type = ItemType.LIQ_CONTAINER
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 5
        item.value = 2000
        item.rent = 12
        item.min_level = 0

        item.liq_units = 50

        self.assert_equals(item, actual)

    def test_parse_file__a_pebble(self):
        actual = self.read_item_from_file("a-pebble")

        item = Item()
        item.name = "a pebble"
        item.type = ItemType.STAFF
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 10
        item.rent = 5000
        item.min_level = 15

        item.spell_level = 0
        item.spells.append(ItemSpell.EARTHQUAKE)
        item.charge_max = 1
        item.charge_remain = 1

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_shroud_of_mist(self):
        actual = self.read_item_from_file("a-shroud-of-mist")

        item = Item()
        item.name = "a shroud of mist"
        item.type = ItemType.WAND
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemAlign.GOOD)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 2500
        item.rent = 25
        item.min_level = 0

        item.spell_level = 5
        item.spells.append(ItemSpell.REJUVENTATE)
        item.charge_max = 3
        item.charge_remain = 3

        item.slots.append(ItemSlot.ABOUT_BODY)
        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_golden_amulet(self):
        actual = self.read_item_from_file("a-golden-amulet")

        item = Item()
        item.name = "a golden amulet"
        item.type = ItemType.STAFF
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemAlign.NO_GOOD)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_PAL)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 4000
        item.rent = 1500
        item.min_level = 9

        item.spell_level = 20
        item.spells.append(ItemSpell.CALL_LIGHTNING)
        item.charge_max = 3
        item.charge_remain = 3

        item.affects[ItemAffect.MANA] = 11
        item.affects[ItemAffect.HITROLL] = -1

        item.slots.append(ItemSlot.NECK)
        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_blue_potion(self):
        actual = self.read_item_from_file("a-blue-potion")

        item = Item()
        item.name = "a blue potion"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 6000
        item.rent = 3000
        item.min_level = 0

        item.spell_level = 15
        item.spells.append(ItemSpell.CURE_CRITIC)
        item.spells.append(ItemSpell.CURE_CRITIC)
        item.spells.append(ItemSpell.CURE_SERIOUS)

        self.assert_equals(item, actual)

    def test_parse_file__the_medallion_of_enchantment(self):
        actual = self.read_item_from_file("the-medallion-of-enchantment")

        item = Item()
        item.name = "the medallion of enchantment"
        item.type = ItemType.STAFF
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemAlign.EVIL)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemAlign.NO_GOOD)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_PAL)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemClass.NO_RANGER)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 3
        item.value = 40000
        item.rent = 250
        item.min_level = 14
        item.max_level = 20

        item.affects[ItemAffect.CHARISMA] = 1
        item.affects[ItemAffect.MANA_REGEN] = 1

        item.spell_level = 14
        item.spells.append(ItemSpell.CHARM_PERSON)
        item.charge_remain = 1
        item.charge_max = 1

        item.slots.append(ItemSlot.NECK)
        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_hell_stone(self):
        actual = self.read_item_from_file("a-hell-stone")

        item = Item()
        item.name = "a hell stone"
        item.type = ItemType.STAFF
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 10
        item.rent = 5000
        item.min_level = 0

        item.spell_level = 20
        item.spells.append(ItemSpell.CURSE)
        item.charge_remain = 1
        item.charge_max = 1

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_small_vial(self):
        actual = self.read_item_from_file("a-small-vial")

        item = Item()
        item.name = "a small vial"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 200
        item.rent = 50
        item.min_level = 0

        item.spell_level = 15
        item.spells.append(ItemSpell.SENSE_LIFE)

        self.assert_equals(item, actual)

    def test_parse_file__the_pinball_wizard_hat(self):
        actual = self.read_item_from_file("the-pinball-wizard-hat")

        item = Item()
        item.name = "the Pinball Wizard hat"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_PAL)
        item.tags.append(ItemClass.NO_APAL)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemClass.NO_JEDI)
        item.tags.append(ItemTag.LIMITED)
        item.tags.append(ItemClass.NO_RANGER)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 15000
        item.rent = 7500
        item.min_level = 12
        item.ac = 8

        item.affects[ItemAffect.MANA] = 8
        item.affects[ItemAffect.INT] = 1

        item.slots.append(ItemSlot.HEAD)

        self.assert_equals(item, actual)

    def test_parse_file__a_wand_of_invisibility(self):
        actual = self.read_item_from_file("a-wand-of-invisibility")

        item = Item()
        item.name = "a wand of invisibility"
        item.type = ItemType.WAND
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 5500
        item.rent = 1375
        item.min_level = 0

        item.spell_level = 12
        item.spells.append(ItemSpell.INVISIBLE)
        item.charge_max = 3
        item.charge_remain = 3

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_yellow_potion_of_see_invisible(self):
        actual = self.read_item_from_file("a-yellow-potion-of-see-invisible")

        item = Item()
        item.name = "a yellow potion of see invisible, by \"Froboz, Inc\"(tm)"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 500
        item.rent = 250
        item.min_level = 0

        item.spell_level = 12
        item.spells.append(ItemSpell.DETECT_INVISIBILITY)
        item.spells.append(ItemSpell.DETECT_INVISIBILITY)
        item.spells.append(ItemSpell.DETECT_INVISIBILITY)

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_shiny_breast_plate(self):
        actual = self.read_item_from_file("a-shiny-breast-plate")

        item = Item()
        item.name = "a shiny breast plate"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemClass.NO_RANGER)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 50
        item.value = 40000
        item.rent = 12000
        item.min_level = 12
        item.ac = 25

        item.affects[ItemAffect.ARMOR] = -4

        item.slots.append(ItemSlot.ON_BODY)

        self.assert_equals(item, actual)

    def test_parse_file__a_slimey_key(self):
        actual = self.read_item_from_file("a-slimey-key")

        item = Item()
        item.name = "a slimey key"
        item.type = ItemType.KEY
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 3
        item.value = 1
        item.rent = 100
        item.min_level = 0

        self.assert_equals(item, actual)

    def test_parse_file__a_longbow(self):
        actual = self.read_item_from_file("a-longbow")

        item = Item()
        item.name = "a longbow"
        item.type = ItemType.FIRE_WEAPON
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 9
        item.value = 10000
        item.rent = 5000
        item.min_level = 13

        item.charge_remain = 15
        item.charge_max = 6
        item.dice_face = 5
        item.dice_count = 3

        self.assert_equals(item, actual)

    def test_parse_file__a_small_bright_green_hat(self):
        actual = self.read_item_from_file("a-small-bright-green-hat")

        item = Item()
        item.name = "a small bright green hat"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.NO_DROP)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 200
        item.rent = 50
        item.min_level = 0

        item.ac = 6
        item.affects[ItemAffect.MOVE_REGEN] = 5
        item.affects[ItemAffect.HEIGHT] = 20

        item.slots.append(ItemSlot.HEAD)

        self.assert_equals(item, actual)

    def test_parse_file__a_silvery_blue_wand(self):
        actual = self.read_item_from_file("a-silvery-blue-wand")

        item = Item()
        item.name = "a silvery blue wand"
        item.type = ItemType.WAND
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 5000
        item.rent = 2500
        item.min_level = 0

        item.spell_level = 10
        item.spells.append(ItemSpell.LIGHTNING_BOLT)
        item.charge_max = 3
        item.charge_remain = 3

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_blood_red_potion(self):
        actual = self.read_item_from_file("a-blood-red-potion")

        item = Item()
        item.name = "a blood red potion"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 2
        item.value = 5000
        item.rent = 0
        item.min_level = 0

        item.spell_level = 20
        item.spells.append(ItemSpell.CURE_BLIND)
        item.spells.append(ItemSpell.CURE_CRITIC)
        item.spells.append(ItemSpell.CURE_CRITIC)

        self.assert_equals(item, actual)

    def test_parse_file__a_pitch_black_potion(self):
        actual = self.read_item_from_file("a-pitch-black-potion")

        item = Item()
        item.name = "a pitch black potion"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 1800
        item.rent = 900
        item.min_level = 0

        item.spell_level = 20
        item.spells.append(ItemSpell.ENERGY_DRAIN)

        self.assert_equals(item, actual)

    def test_parse_file__a_stupid_bardic_colleges_t_shirt(self):
        actual = self.read_item_from_file("a-stupid-bardic-colleges-t-shirt")

        item = Item()
        item.name = "a stupid bardic colleges T-shirt"
        item.type = ItemType.TREASURE
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_DROP)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_PAL)
        item.tags.append(ItemClass.NO_APAL)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemClass.NO_JEDI)
        item.tags.append(ItemClass.NO_SOHEI)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemClass.NO_RANGER)
        item.tags.append(ItemClass.NO_BARD)

        item.weight = 3
        item.value = 0
        item.rent = 0
        item.min_level = 16

        item.affects[ItemAffect.MANA_REGEN] = 5
        item.affects[ItemAffect.MOVE] = -99

        item.slots.append(ItemSlot.ON_BODY)

        self.assert_equals(item, actual)

    def test_parse_file__a_shining_black_ninja_star(self):
        actual = self.read_item_from_file("a-shining-black-ninja-star")

        item = Item()
        item.name = "a shining black ninja star"
        item.type = ItemType.MISSILE
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemClass.NO_WAR)
        item.tags.append(ItemClass.NO_PAL)
        item.tags.append(ItemClass.NO_APAL)
        item.tags.append(ItemClass.NO_JEDI)
        item.tags.append(ItemTag.LIMITED)
        item.tags.append(ItemClass.NO_RANGER)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 1250
        item.rent = 625
        item.min_level = 0

        self.assert_equals(item, actual)

    def test_parse_file__an_opal_potion(self):
        actual = self.read_item_from_file("an-opal-potion")

        item = Item()
        item.name = "an opal potion"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 25000
        item.rent = 0
        item.min_level = 0

        item.spell_level = 15
        item.spells.append(ItemSpell.SANCTUARY)
        item.spells.append(ItemSpell.REMOVE_POISON)
        item.spells.append(ItemSpell.CAUSE_SERIOUS)

        self.assert_equals(item, actual)

    def test_parse_file__metallic_shield(self):
        actual = self.read_item_from_file("metallic-shield")

        item = Item()
        item.name = "metallic shield"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 1000
        item.rent = 200
        item.min_level = 0

        item.ac = 5
        item.affects[ItemAffect.SAVE_SPELL] = -2

        item.slots.append(ItemSlot.SHIELD)

        self.assert_equals(item, actual)

    def test_parse_file__a_small_leaflet(self):
        actual = self.read_item_from_file("a-small-leaflet")

        item = Item()
        item.name = "a small leaflet"
        item.type = ItemType.TRASH
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 1
        item.rent = 0
        item.min_level = 0

        self.assert_equals(item, actual)

    def test_parse_file__a_scroll_of_identify(self):
        actual = self.read_item_from_file("a-scroll-of-identify")

        item = Item()
        item.name = "a scroll of identify"
        item.type = ItemType.SCROLL
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)
        item.tags.append(ItemTag.ASSM)

        item.weight = 1
        item.value = 2000
        item.rent = 250
        item.min_level = 0

        item.spell_level = 12
        item.spells.append(ItemSpell.IDENTIFY)

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__the_head_of_medusa(self):
        actual = self.read_item_from_file("the-head-of-medusa")

        item = Item()
        item.name = "the Head of Medusa"
        item.type = ItemType.WAND
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 20000
        item.rent = 7500
        item.min_level = 15

        item.spell_level = 27
        item.spells.append(ItemSpell.PETRIFICATION)
        item.charge_max = 2
        item.charge_remain = 2

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_large_icon(self):
        actual = self.read_item_from_file("a-large-icon")

        item = Item()
        item.name = "a large icon"
        item.type = ItemType.WAND
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_DROP)
        item.tags.append(ItemAlign.NO_GOOD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 5000
        item.rent = 1250
        item.min_level = 0

        item.spell_level = 35
        item.spells.append(ItemSpell.MAGIC_MISSILE)
        item.charge_max = 10
        item.charge_remain = 10

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_crumbled_piece_of_paper(self):
        actual = self.read_item_from_file("a-crumpled-piece-of-paper")

        item = Item()
        item.name = "a crumpled piece of paper"
        item.type = ItemType.NOTE
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 1
        item.rent = 100000
        item.min_level = 0

        self.assert_equals(item, actual)

    def test_parse_file__a_silver_mirror(self):
        actual = self.read_item_from_file("a-silver-mirror")

        item = Item()
        item.name = "a silver mirror"
        item.type = ItemType.WAND
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_RENT)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 15000
        item.rent = 0
        item.min_level = 0

        item.spell_level = 0
        item.spells.append(ItemSpell.CLONE)

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__the_ancient_vessel_of_aquarius(self):
        actual = self.read_item_from_file("the-ancient-vessel-of-aquarius")

        item = Item()
        item.name = "the Ancient Vessel of Aquarius"
        item.type = ItemType.STAFF
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemAlign.NO_EVIL)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 12
        item.value = 10000
        item.rent = 5000
        item.min_level = 0

        item.spell_level = 5
        item.spells.append(ItemSpell.CREATE_WATER)
        item.charge_max = 10
        item.charge_remain = 10

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__an_ugly_skull_of_draco(self):
        actual = self.read_item_from_file("an-ugly-skull-of-draco")

        item = Item()
        item.name = "an ugly skull of Draco"
        item.type = ItemType.WAND
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_DROP)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 20
        item.value = 10000
        item.rent = 3000
        item.min_level = 0

        item.spells.append(ItemSpell.FIREBALL)
        item.spell_level = 15
        item.charge_remain = 3
        item.charge_max = 3

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_purple_potion(self):
        actual = self.read_item_from_file("a-purple-potion")

        item = Item()
        item.name = "a purple potion"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 10000
        item.rent = 5000
        item.min_level = 0

        item.spells.append(ItemSpell.BLINDNESS)
        item.spells.append(ItemSpell.SANCTUARY)
        item.spells.append(ItemSpell.POISON)
        item.spell_level = 17

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_fountain_pen(self):
        actual = self.read_item_from_file("a-fountain-pen")

        item = Item()
        item.name = 'a fountain pen'
        item.type = ItemType.WEAPON
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.NO_PURGE)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 80
        item.rent = 10
        item.min_level = 0

        item.affects[ItemAffect.HITROLL] = 1
        item.affects[ItemAffect.DAMROLL] = 1

        item.average_dmg = 3.0
        item.dice_count = 1
        item.dice_face = 5

        item.slots.append(ItemSlot.WIELD)

        self.assert_equals(item, actual)

    def test_parse_file__a_huge_plastic_mustache(self):
        actual = self.read_item_from_file("a-huge-plastic-mustache")

        item = Item()
        item.name = "a Huge Plastic Mustache"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.INVIS)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_CLER)
        item.tags.append(ItemClass.NO_PAL)
        item.tags.append(ItemClass.NO_APAL)
        item.tags.append(ItemClass.NO_JEDI)
        item.tags.append(ItemClass.NO_SOHEI)
        item.tags.append(ItemTag.NO_DONATE)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.NO_JUNK)
        item.tags.append(ItemTag.UNIQUE)
        item.tags.append(ItemRace.NO_HUMAN)
        item.tags.append(ItemRace.NO_ELF)
        item.tags.append(ItemRace.NO_DWARF)
        item.tags.append(ItemRace.NO_ORC)
        item.tags.append(ItemRace.NO_HALF_ORC)
        item.tags.append(ItemRace.NO_GOBLIN)
        item.tags.append(ItemRace.NO_URUKHAI)
        item.tags.append(ItemTag.INSURED)
        item.tags.append(ItemRace.NO_HALF_ELF)

        item.weight = 1
        item.value = 5000
        item.rent = 0
        item.min_level = 15
        item.ac = 0

        item.affects[ItemAffect.DEX] = 1
        item.affects[ItemAffect.HITROLL] = 3

        item.slots.append(ItemSlot.FACE)

        self.assert_equals(item, actual)

    def test_parse_file__a_tattered_scroll(self):
        actual = self.read_item_from_file("a-tattered-scroll")

        item = Item()
        item.name = "a tattered scroll"
        item.type = ItemType.SCROLL
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 10000
        item.rent = 5000
        item.min_level = 0

        item.spell_level = 24
        item.spells.append(ItemSpell.ENCHANT_WEAPON)

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_sturdy_iron_shield(self):
        actual = self.read_item_from_file("a-sturdy-iron-shield")

        item = Item()
        item.name = "a sturdy iron shield"
        item.type = ItemType.ARMOR
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.GLOW)
        item.tags.append(ItemClass.NO_MAGE)
        item.tags.append(ItemClass.NO_THF)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemClass.NO_BARD)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 5
        item.value = 5000
        item.rent = 1250
        item.min_level = 10

        item.ac = 7

        item.affects[ItemAffect.SAVE_BREATH] = -2
        item.affects[ItemAffect.SAVE_SPELL] = -2

        item.slots.append(ItemSlot.SHIELD)

        self.assert_equals(item, actual)

    def test_parse_file__a_peaceful_potion(self):
        actual = self.read_item_from_file("a-peaceful-potion")

        item = Item()
        item.name = "a peaceful potion"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 17542
        item.rent = 5625
        item.min_level = 0

        item.spell_level = 10
        item.spells.append(ItemSpell.PROTECTION_FROM_EVIL)
        item.spells.append(ItemSpell.PROTECTION_FROM_GOOD)
        item.spells.append(ItemSpell.INVISIBLE)

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_rod_made_of_polished_stone(self):
        actual = self.read_item_from_file("a-rod-made-of-polished-stone")

        item = Item()
        item.name = "a rod made of polished stone"
        item.type = ItemType.STAFF
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemAlign.GOOD)
        item.tags.append(ItemClass.NO_APAL)
        item.tags.append(ItemClass.NO_NINJA)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 10
        item.value = 65700
        item.rent = 5000
        item.min_level = 0

        item.spell_level = 20
        item.spells.append(ItemSpell.CALM)
        item.charge_max = 2
        item.charge_remain = 2

        item.slots.append(ItemSlot.HOLD)

        self.assert_equals(item, actual)

    def test_parse_file__a_murky_grey_vial(self):
        actual = self.read_item_from_file("a-murky-grey-vial")

        item = Item()
        item.name = "a murky grey vial"
        item.type = ItemType.POTION
        item.ability = ItemAbility.NOBITS

        item.tags.append(ItemTag.HUM)
        item.tags.append(ItemTag.MAG)
        item.tags.append(ItemTag.NO_DROP)
        item.tags.append(ItemTag.UNIQUE)

        item.weight = 1
        item.value = 250
        item.rent = 62
        item.min_level = 0

        item.spell_level = 20
        item.spells.append(ItemSpell.HARM)
        item.spells.append(ItemSpell.SLEEP)

        self.assert_equals(item, actual)

    def assert_equals(self, expected, actual):
        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.ability, actual.ability)
        self.assertEqual(expected.type, actual.type)
        self.assertEqual(expected.weight, actual.weight)
        self.assertEqual(expected.value, actual.value)
        self.assertEqual(expected.rent, actual.rent)
        self.assertEqual(expected.min_level, actual.min_level)
        self.assertEqual(expected.max_level, actual.max_level)
        self.assertEqual(expected.units, actual.units)
        self.assertEqual(expected.liq_units, actual.liq_units)
        self.assertEqual(expected.ac, actual.ac)
        self.assertEqual(expected.tags, actual.tags)
        self.assertEqual(expected.slots, actual.slots)
        self.assertEqual(expected.affects, actual.affects)
        self.assertEqual(expected.spell_level, actual.spell_level)
        self.assertEqual(expected.charge_max, actual.charge_max)
        self.assertEqual(expected.charge_remain, actual.charge_remain)
        self.assertEqual(expected.spells, actual.spells)
        self.assertEqual(expected.dice_face, actual.dice_face)
        self.assertEqual(expected.dice_count, actual.dice_count)
        self.assertEqual(expected.average_dmg, actual.average_dmg)

    def read_item_from_file(self, fname):
        ip = ItemParser()
        lines = ip.read_file("py/test-items/" + fname + ".txt")
        return ip.parse_file(lines)[-1]


if __name__ == "__main__":
    unittest.main()
