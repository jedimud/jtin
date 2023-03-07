#!/bin/bash

export map="./maps/"$@".map"

# linked areas
export linked=$(grep 'R {' "$map" | grep '<fff>' | grep '{}{}{}{}{}' | wc -l)
echo $linked

# count of mapped rooms
export mapped=$(grep 'R {' "$map" | wc -l)
echo $mapped

# count of unmapped rooms
export unmapped=$(grep 'R {' "$map" | grep '<efa>' | wc -l)
echo $unmapped

# total rooms
export total=$((mapped + unmapped))
echo $total

# percent mapped
export percent=$((mapped * 100 / total * 100 / 100))
echo $percent
