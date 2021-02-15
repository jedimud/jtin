[README.md](../../../) > kill-log.md

----

# Loot Log

Real-time, comma-delimited log of items looted from corpses.

## Usage

Load loot-log tin as class at TinTin++ startup.

`#class mapper read tins/loot-log.tin`

> [Mapper](mapper.md) is required to properly capture zone where corpse was looted.

## Log Format

`{npc},{item},{map}`
> If no item was looted, `{item}` is empty

## Sample Output

````
the Knight,,midgaard-warrior-guild.map
the Ninja Lord,,midgaard-ninja-guild.map
a wooden Dynasty shield,Izumo No Okumi,midgaard-ninja-guild.map
a red silk armband,Izumo No Okumi,midgaard-ninja-guild.map
a black Shinobi Shozoku shirt,Izumo No Okumi,midgaard-ninja-guild.map
a gold Ryo coin on a rawhide string,Izumo No Okumi,midgaard-ninja-guild.map
a little pile of gold coins,a citizen of Midgaard,midgaard.map
a long sword,Welmar's Ranger,midgaard.map
````
