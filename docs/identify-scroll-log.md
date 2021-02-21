[README.md](../../../) > kill-log.md

----

# Identify Scroll Log

Line-delimited log of `scroll of identify` outputs. Items are additionally tested for wearable, holdable, wieldable attributes.

## Usage

Load tin as class at TinTin++ startup.

`#class ident-log read tins/ident-log.tin`

Run alias on item in inventory.

`ident krrf`

> The item being scanned and `scroll of identify` must both be in inventory

## Sample Log

````
-----
Object 'a combat jumpsuit', Item type: ARMOR
Item will give you following abilities:  NOBITS 
Item is: GLOW INVIS LIMITED !DONATE !JUNK UNIQUE INSURED 
Weight: 4, Value: 20000, Rent: 5000, Min. level: 10
AC-apply is 6
Can affect you as :
   Affects: DAMROLL By 1
ItemSlot: About Body
-----
Object 'a dart', Item type: WEAPON
Item will give you following abilities:  NOBITS 
Item is: !CLER UNIQUE 
Weight: 1, Value: 5, Rent: 0, Min. level: 0
Damage Dice is '1D2' for an average per-round damage of 1.5.
ItemSlot: Weapon
ItemSlot: Hold
````
> Items are delimited by `-----`
