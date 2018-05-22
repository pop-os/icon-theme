#!/bin/bash -e

APPS=(
    builder
    org.gnome.builder
    org.gnome.Builder
)

SCALES=(
    16x16
    22x22
    24x24
    32x32
    48x48
    64x64
    symbolic
)

if [ ! -d "$1" -o ! -d "$2" ]
then
    echo "$0 [original directory] [new directory]"
    exit 1
fi

ORIGINAL="$(realpath "$1")"
NEW="$(realpath "$2")"

cd "$ORIGINAL"
for app in "${APPS[@]}"
do
    for scale in "${SCALES[@]}"
    do
        folder="$scale/apps"
        if [ -d "$folder" ]
        then
            file="$folder/$app.svg"
            if [ -f "$file" -o -L "$file" ]
            then
                mkdir -pv "$NEW/$folder"
                mv -v "$file" "$NEW/$file"
            fi
        fi
    done
done
