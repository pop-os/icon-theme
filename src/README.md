## Source Files

Do not edit icon assets directly (i.e. tweaking those in the "Pop" folder with a raster editor)! For ease of development and organization's sake, the sources for all the different icons and cursors are kept in various subfolders: 

 - [bitmaps](./bitmaps) contains the source files and render scripts for all bitmap icons.
 - [scalable](./scalable) contains the source files and render scripts for all symbolic icons.
 - [cursors](./cursors) contains the source files and render scripts for the cursor theme.
 - [symlinks](./symlinks) contains the data lits and generation scripts to create symbolic links the icon theme.

## Modifications

To modify the theme files, first edit the relevant source file in one of the 
above-mentioned directories. Following this, you must delete the original icon 
file/symlink from the main theme folder (in the `Pop` folder) and re-render the
theme using the `master-render.py` script in the root directory. For 
convenience, the render scripts are set up to skip items which are already 
present in the output folder (hence the need to delete the existing output file).

For larger changes, or before releasing a new version, it may be required to 
clear all of the existing output files and re-render the entire theme. To do 
this, use the `--clean` flag for the `master-render.py` script to clear the 
directory first. 

## Resources

**[Pop.gpl](./Pop.gpl)**
- The Inkscape colour palette for the Pop icons. You can copy it to `.config/inkscape/palettes` and restart Inkscape to able to choose it from the palette menu (in the lower right corner).