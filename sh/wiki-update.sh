#!/bin/bash

# append template
cat ./sh/wiki-map-template.md > ../jtin.wiki/Unicode-Maps.md

# stats
echo "Total: **"$(ls maps | wc -l | sed 's/^[ \t]*//')"** maps, **"$(grep -rni "R {" maps/* | wc -l | sed 's/^[ \t]*//')"** Rooms, **"$(grep -rni "E {" maps/* | wc -l | sed 's/^[ \t]*//')"** paths" >> ../jtin.wiki/Unicode-Maps.md
echo "" >> ../jtin.wiki/Unicode-Maps.md

python3 ./py/wiki_map_list.py >> ../jtin.wiki/Unicode-Maps.md

rm -rf ../jtin.wiki/items
python3 ./py/wiki_item_brief.py
python3 ./py/wiki_item_create.py

rm -rf ../jtin.wiki/zones
python3 ./py/wiki_map_create.py

rm -rf ../jtin.wiki/npcs
python3 ./py/wiki_npc_kill_brief.py
python3 ./py/wiki_npc_loot_brief.py
python3 ./py/wiki_npc_create.py
