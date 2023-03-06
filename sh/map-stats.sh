#!/bin/bash

#count of areas
echo $(ls maps | wc -l)

# count of rooms
echo $(grep -rni "R {" maps/* | wc -l)

# count of paths
echo $(grep -rni "E {" maps/* | wc -l)
