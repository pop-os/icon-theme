#!/bin/bash
#
# Description:
#   A script for quick generation of symlinks of an in-development icon theme
#
# Legal Stuff:
#
# This script is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# This script is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/gpl-3.0.txt>


DIR=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
THEME="Pop"

# echo $DIR

# Icon sizes and contexts
CONTEXTS=("actions" "apps" "devices" "emblems" "categories" "mimetypes" "places" "status")
SIZES=("8x8" "16x16" "24x24" "32x32" "48x48" "64x64" "128x128" "256x256" "512x512")
SCALES=('@2x')

# Fullcolor icons
echo "Generating links for full-color icons..."
# contexts for loop
for CONTEXT in "${CONTEXTS[@]}"
do
	echo " -- "${CONTEXT}
	# Sizes Loop
	for SIZE in "${SIZES[@]}"
	do
		LIST="$DIR/fullcolor/$CONTEXT.list"
		# Check if directory exists
		if [ -d "$DIR/../../$THEME/$SIZE/$CONTEXT" ]; then
		    echo "  -- linking "$SIZE"/"$CONTEXT
			cd $DIR/../../$THEME/$SIZE/$CONTEXT
			while read line;
			do
    			ln -sf $line
			done < $LIST
			cd $DIR/../../$THEME
		else
			echo "  ** skipping "$SIZE"/"$CONTEXT
		fi
	done
done
echo "Done."


# Symbolic icons
echo "Generating links for symbolic icons..."
# contexts for loop
for CONTEXT in "${CONTEXTS[@]}"
do
	echo " -- "${CONTEXT}
	LIST="$DIR/scalable/$CONTEXT.list"
	# Check if directory exists
	if [ -d "$DIR/../../$THEME/$SIZE/$CONTEXT" ]; then
	    echo "  -- linking "$SIZE"/"$CONTEXT
		cd $DIR/../../$THEME/$SIZE/$CONTEXT
		while read line;
		do
			ln -sf $line
		done < $LIST
		cd $DIR/../../$THEME
	else
		echo "  ** skipping "$SIZE"/"$CONTEXT
	fi
done
echo "Done."


# # HiDPI
# for SCALE in "${SCALES[@]}"
# do
# 	for SIZE in "${SIZES[@]}"
# 	do
# 		echo "  -- Linking HiDPI icons for "$SIZE""$SCALE"..."
# 		cd $DIR/../../$THEME/
# 		ln -fs $SIZE $SIZE$SCALE
# 	done
# done


# echo $DIR
# Clear symlink errors
if command -v symlinks 2>&1 >/dev/null; then
	echo "Deleting broken links..."
	symlinks -cdr $DIR/../../$THEME > /dev/null
	echo "Done."
fi
