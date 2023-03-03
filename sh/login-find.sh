#!/bin/bash
while IFS=, read -r user password window cmd
do
    if [[ "$@" == $user ]]; then
        echo "$user"
        echo "$password"
        echo "$window"
        echo "$cmd"
    fi;
done < ./data/login.csv
