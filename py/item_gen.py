import random
from item_align import ItemAlign
from item_affect import ItemAffect
from item_type import ItemType
from item_slot import ItemSlot
from item_spell import ItemSpell

# Function to generate a shorthand item description
def generate_item():
    item = ""
    limited = False

    # type
    item_types = [ItemType.ARMOR,
                  ItemType.CONTAINER,
                  ItemType.LIGHT,
                  ItemType.LIQ_CONTAINER,
                  ItemType.POTION,
                  ItemType.SCROLL,
                  ItemType.STAFF,
                  ItemType.WAND,
                  ItemType.WEAPON,
                  ItemType.WORN]
    item_type = random.choice([item_type.brief for item_type in item_types])

   # restrictable
    restrictable = False
    if item_type in [ItemType.ARMOR.brief,
                  ItemType.CONTAINER.brief,
                  ItemType.LIGHT.brief,
                  ItemType.LIQ_CONTAINER.brief,
                  ItemType.WEAPON.brief,
                  ItemType.WORN.brief]:
        restrictable = True

    # ml
    ml = 'ml 0'
    if restrictable:
        ml_start = random.randint(0, 12)
        ml_end = random.randint(ml_start + 5, 22)
        ml = f"ml {ml_start}-{ml_end}"
    item += ml

    # item align
    random_align = f" {random.choice([enum.brief for enum in ItemAlign])}" if random.randint(
        0, 4) == 0 else ""

    # class align
    random_class = "".join(
        char for char in "cmtwpanjsrb" if random.randint(0, 10) == 0)
    random_class = "!" + random_class if random_class else ""

    # combine align + class
    if restrictable:
        item += " !REST " if random_align == "" and random_class == "" else f"{random_align} {random_class} "
    else:
        item += " !REST "
    item = item.strip() + " "

    # stats
    affect_values = [enum.brief for enum in ItemAffect]

    # dice
    if item_type == ItemType.WEAPON.brief:
        num_dice = random.randint(1, 3)
        if num_dice == 3:
            limited = True
            sides_per_die = random.choice([4, 6, 8])
        else:
            sides_per_die = random.choice([4, 6, 8, 10, 12])
        average_damage = (num_dice * (sides_per_die + 1)) / 2
        item += str(num_dice) + 'D' + str(sides_per_die) + '(' + str(average_damage) + ') '

    # affects
    s = random.randint(0, 3)
    aff1 = ''
    aff2 = ''
    if s == 0:
        limited = True
        while True:
            aff1 = random.choice(affect_values)
            while True:
                aff2 = random.choice(affect_values)
                if aff2 != aff1:
                    break
            if aff1 in [ItemAffect.STR.brief, ItemAffect.CON.brief, ItemAffect.WIS.brief, ItemAffect.INT.brief, ItemAffect.CHARISMA.brief, ItemAffect.DEX.brief]:
                aff1 = f"+{random.randint(2, 3)}{aff1}"
            elif aff1 in [ItemAffect.AGE.brief]:
                aff1 = f"+{random.randint(10, 20)}{aff1}"
            elif aff1 in [ItemAffect.DAMROLL.brief, ItemAffect.HITROLL.brief]:
                aff1 = f"+{random.randint(2, 3)}{aff1}"
            elif aff1 in [ItemAffect.MANA.brief, ItemAffect.HIT.brief, ItemAffect.MOVE.brief]:
                aff1 = f"+{random.randint(10, 30)}{aff1}"
            elif aff1 in [ItemAffect.MANA_REGEN.brief, ItemAffect.HIT_REGEN.brief, ItemAffect.MOVE_REGEN.brief]:
                aff1 = f"+{random.randint(10, 20)}{aff1}"
            else:
                continue

            if aff2 in [ItemAffect.STR.brief, ItemAffect.CON.brief, ItemAffect.WIS.brief, ItemAffect.INT.brief, ItemAffect.CHARISMA.brief, ItemAffect.DEX.brief]:
                aff2 = f" {random.randint(-3, -1)}{aff2}"
            elif aff2 in [ItemAffect.AGE.brief]:
                aff2 = f" {random.randint(-10,-1)}{aff2}"
            elif aff2 in [ItemAffect.DAMROLL.brief, ItemAffect.HITROLL.brief]:
                aff2 = f" {random.randint(-2, -1)}{aff2}"
            elif aff2 in [ItemAffect.MANA.brief, ItemAffect.HIT.brief, ItemAffect.MOVE.brief]:
                aff2 = f" {random.randint(-10, -5)}{aff2}"
            elif aff2 in [ItemAffect.MANA_REGEN.brief, ItemAffect.HIT_REGEN.brief, ItemAffect.MOVE_REGEN.brief]:
                aff2 = f" {random.randint(-8, -2)}{aff2}"
            else:
                continue
            break

    elif s == 1:
        while True:
            aff1 = random.choice(affect_values)
            while True:
                aff2 = random.choice(affect_values)
                if aff2 != aff1:
                    break
            if aff1 in [ItemAffect.STR.brief, ItemAffect.CON.brief, ItemAffect.WIS.brief, ItemAffect.INT.brief, ItemAffect.CHARISMA.brief, ItemAffect.DEX.brief]:
                aff1 = f"+{random.randint(1, 1)}{aff1}"
            elif aff1 in [ItemAffect.AGE.brief]:
                aff1 = f"+{random.randint(1, 9)}{aff1}"
            elif aff1 in [ItemAffect.DAMROLL.brief, ItemAffect.HITROLL.brief]:
                aff1 = f"+{random.randint(1, 1)}{aff1}"
            elif aff1 in [ItemAffect.MANA.brief, ItemAffect.HIT.brief, ItemAffect.MOVE.brief]:
                aff1 = f"+{random.randint(1,9)}{aff1}"
            elif aff1 in [ItemAffect.MANA_REGEN.brief, ItemAffect.HIT_REGEN.brief, ItemAffect.MOVE_REGEN.brief]:
                aff1 = f"+{random.randint(1,9)}{aff1}"
            else:
                continue

            if aff2 in [ItemAffect.STR.brief, ItemAffect.CON.brief, ItemAffect.WIS.brief, ItemAffect.INT.brief, ItemAffect.CHARISMA.brief, ItemAffect.DEX.brief]:
                aff2 = f" +{random.randint(1,1)}{aff2}"
            elif aff2 in [ItemAffect.AGE.brief]:
                aff2 = f" +{random.randint(1,9)}{aff2}"
            elif aff2 in [ItemAffect.DAMROLL.brief, ItemAffect.HITROLL.brief]:
                aff2 = f" +{random.randint(1,1)}{aff2}"
            elif aff2 in [ItemAffect.MANA.brief, ItemAffect.HIT.brief, ItemAffect.MOVE.brief]:
                aff2 = f" +{random.randint(1,9)}{aff2}"
            elif aff2 in [ItemAffect.MANA_REGEN.brief, ItemAffect.HIT_REGEN.brief, ItemAffect.MOVE_REGEN.brief]:
                aff2 = f" +{random.randint(1,9)}{aff2}"
            else:
                continue
            break
    else:
        while True:
            aff1 = random.choice(affect_values)
            if aff1 in [ItemAffect.STR.brief, ItemAffect.CON.brief, ItemAffect.WIS.brief, ItemAffect.INT.brief, ItemAffect.CHARISMA.brief, ItemAffect.DEX.brief]:
                aff1 = f"+{random.randint(1, 1)}{aff1}"
            elif aff1 in [ItemAffect.AGE.brief]:
                aff1 = f"+{random.randint(1, 9)}{aff1}"
            elif aff1 in [ItemAffect.DAMROLL.brief, ItemAffect.HITROLL.brief]:
                aff1 = f"+{random.randint(1, 1)}{aff1}"
            elif aff1 in [ItemAffect.MANA.brief, ItemAffect.HIT.brief, ItemAffect.MOVE.brief]:
                aff1 = f"+{random.randint(1,9)}{aff1}"
            elif aff1 in [ItemAffect.MANA_REGEN.brief, ItemAffect.HIT_REGEN.brief, ItemAffect.MOVE_REGEN.brief]:
                aff1 = f"+{random.randint(1,9)}{aff1}"
            else:
                continue
            break
    affectable = item_type in [
            ItemType.CONTAINER.brief,
            ItemType.LIQ_CONTAINER.brief,
            ItemType.LIGHT.brief,
            ItemType.WEAPON.brief,
            ItemType.ARMOR.brief,
            ItemType.WORN.brief,
        ]
    if affectable:
        item += f"{aff1}{aff2} "

    # can hold
    holdable = (
        item_type in [
            ItemType.CONTAINER.brief,
            ItemType.LIQ_CONTAINER.brief,
            ItemType.POTION.brief,
            ItemType.SCROLL.brief,
            ItemType.STAFF.brief,
            ItemType.WAND.brief,
        ]
        or (item_type == ItemType.WEAPON.brief and random.randint(1, 2) == 1)
    )

    # slot
    slot = random.choice([enum.brief for enum in ItemSlot if enum not in [ItemSlot.WIELD, ItemSlot.HOLD, ItemSlot.LIGHT]]) if item_type in [
        ItemType.CONTAINER.brief, ItemType.LIQ_CONTAINER.brief, ItemType.WORN.brief, ItemType.ARMOR.brief] else ""

    # show type and slot
    if (item_type == ItemType.LIQ_CONTAINER.brief):
        if (slot != ""):
            item = f"{item}{item_type}(+{random.choice(range(5, 201, 5))}, {slot}, held)"
        elif (holdable):
            item = f"{item}{item_type}(+{random.choice(range(5, 201, 5))}, held)"
        else:
            item = f"{item}{item_type}(+{random.choice(range(5, 201, 5))})"
    elif (item_type == ItemType.CONTAINER.brief):
        if (slot != ""):
            item = f"{item}{item_type}(+{random.choice(range(100, 2001, 5))}, {slot}, held)"
        elif (holdable):
            item = f"{item}{item_type}(+{random.choice(range(100, 2001, 5))}, held)"
        else:
            item = f"{item}{item_type}(+{random.choice(range(100, 2001, 5))})"
    elif (slot != ""):
        if holdable:
            item += f"{item_type}({slot}, held)"
        else:
            item += f"{item_type}({slot})"
    elif (item_type == ItemType.WEAPON.brief):
        if holdable:
            item += f"{item_type}(wield, held)"
        else: 
            item += f"{item_type}(wield)"
    elif (holdable):
        item += f"{item_type}(held)"
    else:
        item += f"{item_type}"

    # spells
    if item_type in [ItemType.WAND.brief, ItemType.SCROLL.brief, ItemType.STAFF.brief, ItemType.POTION.brief]:
        item += " ["
        for i in range(0, random.randint(1, 3)):
            item += random.choice([item_spell.value for item_spell in ItemSpell]) + ', '
        item = item.strip()[:-1]+ "]"

    # limited
    if limited:
        item += " (L)"

    return item


# Generate and print 10 items
for _ in range(1000):
    print(generate_item())
