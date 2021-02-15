[README.md](../../../) > kill-log.md

----

# Kill Log

Real-time, comma-delimited log of NPC kills.

## Usage

Load kill-log tin as class at TinTin++ startup.

`#class mapper read tins/kill-log.tin`

> [Mapper](mapper.md) is required to properly capture zone where NPC was killed.

## Log Format

`{npc},{map}`

## Sample Output

````
The Sailor,midgaard.map
The Janitor,midgaard.map
The green enfan,enfan-city.map
The message bot,midgaard-thief-guild.map
The Assassin,midgaard-thief-guild.map
The Knight,midgaard-warrior-guild.map
The Ninja Lord,midgaard-ninja-guild.map
Izumo No Okumi,midgaard-ninja-guild.map
A citizen of Midgaard,midgaard.map
Welmar's Ranger,midgaard.map
````
