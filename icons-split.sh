#!/bin/bash -e

APPS=(
    builder
    org.gnome.builder
    org.gnome.Builder
)

if [ ! -d "$1" -o ! -d "$2" ]
then
    echo "$0 [original] [new]"
    exit 1
fi

ORIGINAL="$(realpath "$1")"
NEW="$(realpath "$2")"

cd "$ORIGINAL"
for app in "${APPS[@]}"
do
    for folder in */apps
    do
        file="$folder/$app.svg"
        if [ -f "$file" ]
        then
            mkdir -pv "$NEW/$folder"
            mv -v "$file" "$NEW/$file"
        fi
    done
done
