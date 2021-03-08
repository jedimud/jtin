[README.md](../../../) > kill-log.md

----

# Kill Log

Real-time, comma-delimited log of NPC kills.

## Usage

Load kill-log tin as class at TinTin++ startup.

`#class kill-log read tins/kill-log.tin`

> [Mapper](mapper.md) is required to properly capture zone where NPC was killed.

## Log Format

`{npc},{map}`

## Sample Output

````
The Sailor,midgaard
The Janitor,midgaard
The green enfan,enfan-city
The message bot,midgaard-thief-guild
The Assassin,midgaard-thief-guild
The Knight,midgaard-warrior-guild
The Ninja Lord,midgaard-ninja-guild
Izumo No Okumi,midgaard-ninja-guild
A citizen of Midgaard,midgaard
Welmar's Ranger,midgaard
````
