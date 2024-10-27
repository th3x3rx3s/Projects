#!/bin/bash
file=$1
units=("" "KB" "MB" "GB")
if [ "$1" == "" ]; then
    echo "Usage: $0 file"
    exit 1
elif [ -f $file ]; then
    size=$(stat -c %s $file)
    n=0
    while [ $(echo "$size >= 1024" | awk '{printf ($1 >= 1024)}') -eq 1 ] && [ $n -lt "${#units[@]}" ]; do
        size=$(echo "$size / 1024" | awk '{printf "%.2f", $1 / 1024}')
        ((n++))
    done
else
    echo "Nincs ilyen fájl."
    exit 1
fi
echo "$size ${units[$n]}"
