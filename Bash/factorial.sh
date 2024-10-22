#!/bin/bash
read -p "Kérek egy számot: " szam
factorial=1
if [ ! $szam -le 0 ]; then
    for x in $(seq 1 $szam); do
        factorial=$((factorial*x))
    done
elif [ $szam == 0 ]; then 
    echo "$szam faktoriálisa: 1"
    exit
else 
    echo "A szám nem lehet negatív."
    exit
fi
echo "$szam faktoriálisa: $factorial"