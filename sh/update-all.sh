#!/bin/bash

sh/item-brief-update.sh

python3 py/item_wearable_csv.py
python3 py/item_sac_csv.py
