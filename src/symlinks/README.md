## Symbolic Links

To save on space many icons are just symbolic links to generic icons and, to keep track of all links, sets of lists are maintained that corresponds to a icon `context` for both the bitmap, symbolic and panel icons set.

Symbolic link definitions are separated out into `fullcolor` for the full-color icons, and `scalable` for the symbolic icons. Each directory contains a `.list` file for each icon category. Each line in a `.list` file defines exactly one output symlink. The format for each line is `link-target link-name` similar to the `ln` command.

To generate symlinks icons you will only need the provided script, but to clear broken symlinks you'll need `symlinks` installed.

 - [fullcolor](./fullcolor) - the list files for bitmap icon links
 - [scalable](./scalable) -  the list files for scalable icon links
 - [generate-symlinks.sh](./generate-symlinks.sh) - the generation script