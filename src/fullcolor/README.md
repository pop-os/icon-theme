## Full Color Icon Sources

 - To modify an icon, edit the source SVG files found in subfolders within this directory (or create a new one using the [Template](Template.svg)).
 - This folder is subdivided into subfolders that organize the icons sources by `context` 
 - To edit the icons you will need `inkscape` and you'll need `python` installed to run the render script.
 - Files in the `tmp` folder are ignored by the render script
 - Once you have completed your icon/edits, be sure to group each icon into a single object. Set the name for this object using the format {icon-name}-{size} (e.g. edit-delete-64)
    - Do this for each size of icon. This is crucial to rendering the icons without having redundant data.
    - If the final rendered icons are blank, double-check that the correct object is named. 

**[render-fullcolor.py](./render-bitmaps.py) - the render script**
 - This script will render SVG icons, provided the source file has been modified. Icons are rendered as SVG so they correctly scale to larger scale factors automatically.
 - You can render a single icon by passing the icon name to this script: `./render-bitmaps.rb <icon-name>`

**[Template.svg](./Template.svg) - a blank icon template**
 - A blank template file for the fullcolor Pop icons (every icon follows this template.)
 - The template has as _Baseplate_ layer which will contain the necessary metadata for rendering an icon. (hidden by default)
 - There is also a _Margins_ layer which gives some example margins/sizes for icons following general aspect ratios. Try to design icons following these aspect ratios as a start, and adapt where required. The margins are setup to give each icon a consistent general apparent size in the grid of all icons.
 - You **must** change the `context` and `icon-name` labels on the _Baseplate_ for an icon to render properly (also hide the layer). Also, be sure to group each icon into a single object. Set the name for this object using the format {icon-name}-{size} (e.g. edit-delete-64)