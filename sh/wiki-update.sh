#!/bin/bash

# append template
cat ./templates/wiki-map-template.md > ../jtin.wiki/Unicode-Maps.md

# stats
echo "Total: **"$(ls maps | wc -l | sed 's/^[ \t]*//')"** maps, **"$(grep -rni "R {" maps/* | wc -l | sed 's/^[ \t]*//')"** Rooms, **"$(grep -rni "E {" maps/* | wc -l | sed 's/^[ \t]*//')"** paths" >> ../jtin.wiki/Unicode-Maps.md
echo "" >> ../jtin.wiki/Unicode-Maps.md

python3 ./py/wiki_map_list.py >> ../jtin.wiki/Unicode-Maps.md
