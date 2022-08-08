Pop_Icons
================

Pop_Icons are the standard icons for Pop!_OS. It uses a semi-flat design with raised 3D motifs to help give depth to icons. Included in the theme are flat symbolic (single-color) icons as well as full-color stylized icons.

Pop_Icons take inspiration from the Adwaita GNOME Icons. 

## Copying or Reusing

This project has mixed licencing. You are free to copy, redistribute and/or modify aspects of this work under the terms of each licence accordingly (unless otherwise specified).

The icon assets (any and all source `.svg` files or rendered `.png` files) are licenced under the terms of the [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

Included scripts are free software licenced under the terms of the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.txt).

When reusing this work please include a proper attribution:

> "[Pop Icons](http://github.com/pop-os/icon-theme)" by [System76](http://system76.com/) is licensed under [CC-SA-4.0](http://creativecommons.org/licenses/by-sa/4.0/)

## Downloading Pop

It is recommended to install Pop_Icons through your system package manager, e.g.:

```sh
sudo apt update
sudo apt install pop-icon-theme
```

If your OS does not package Pop_Icons, you can install them from git:

```sh
git clone https://github.com/pop-os/icon-theme pop-icon-theme
cd pop-icon-theme
meson build
sudo ninja -C "build" install
```

By default the theme installs to `/usr/`, but you can specify a different directory with a prefix like `/usr/local` or `$HOME/.local`, for example:

```sh
meson -Dprefix=$HOME/.local build
ninja -C "build" install
```

After which you should be able to pick Pop as your icon or cursor theme in GNOME Tweaks, or you can set either from a terminal with:

```sh
# set the icon theme
gsettings set org.gnome.desktop.interface icon-theme "Pop"
# or the cursor theme
gsettings set org.gnome.desktop.interface cursor-theme "Pop"
```

### Uninstalling Pop

To uninstall Pop, simply run the following. (If you installed it without superuser priveleges just omit the  `sudo`.)

```sh
sudo ninja -C "build" uninstall
```

Once uninstalled you can reset your icon and cursor theme to the default setting by running the following.

```sh
# reset icon theme to default
gsettings reset org.gnome.desktop.interface icon-theme
# reset cursor theme to default
gsettings reset org.gnome.desktop.interface cursor-theme
```

## Modifying the theme

Pop uses the meson build system, and can be built using:

```sh
meson build
ninja -C build install
```

Icons and cursors are shipped pre-rendered in order to save time in the event of modifications to the theme as well as reducing build-load on the Pop_OS build servers. Most modifications are rendered using [`./master-render.py`](master-render.py). For making/rendering modifications:

### General Rendering
The `./master-render.py` script takes care of rendering each different type of file in the theme. Running it by default will render any missing icon files and any updated full-color icons. You can render specific parts of the theme by using the following flags:

```
  -a, --all        Render all items (Default)
  -f, --fullcolor  Render fullcolor icons
  -s, --symbolics  Render Symbolic Icons
  -x, --cursors    Render Cursors
  -l, --links      Generate Theme Symlinks
  -m, --metadata   Generate Metadata
```

Using the `-c, --clean` option will erase the currently rendered/generated files in the specified, rendering context, which is helpful in the event a source-file is not rendering when it should be. Using it will re-render all files in the specified context, which can take a long time, so use with care. Using the `-c` flag with `-a, --all` or without another context **will erase all files in the theme and require re-rendering all of them**, so be extra careful. 

Multiple contexts can be combined to render/clean multiple context in one pass, except that any contexts other than `-a, --all` will disable `--all` so keep that in mind.

##### Rendering Dependencies
The following packages are required to render all of the files within the theme:
```
python # Running main, full-color, and cursor render scripts
ruby # Running symbolic icons render script
bash # Running symlink script
inkscape # Renders source files to output
python3-pil # Renders cursors
x11-apps # Rendering cursors
```

Additionally, the following are optional, but will improve the output of the rendering:
```
scour # Cleaning up unused definitions from full-color/symbolic SVGs
svgo # Optimizing full-color and symbolic SVGs
symlinks # Remove empty symlinks
```


### Full-color icons

The full-color icons are stored within the `src/fullcolor` folder, and are organized into subdirectories for each category of icon. After making a modification to a source icon, the changes will automatically be rendered into the required icon files by `./master-render.py`; if the script is not rendering your icon, double-check that the file timestamp has been updated and that the source file follows the related formatting requirements in [`src/fullcolor/README.md`](src/fullcolor/README.md). 

### Symbolic Icons

The symbolic/single-color icons are stored within the `src/scalable/source-symbolic.svg` file. The file has separate layer for each different category of icon within the theme. Ensure when you modify the file, that your icon is located within the correct layer for it to end up in the correct output directory. 

Symbolic icons require that you remove the corresponding output icon from the `Pop/scalable` folder in order for the `master-render.py` script to re-render. The reason for this is that because there is only a single symbolic source-file, we can't re-render a single icon automatically. If you prefer to let the icons re-render automatically and don't mind waiting for all of the symbolics to render, you can do so using `./master-render.py -cls`

Additional information about the symbolic icons can be found in [`src/scalable/README.md`}(src/scalable/README.md)

### Cursors

Cursors are stored in the `src/cursors` directory. Because cursors are somewhat complicated/difficult to render as they are often animated, and because they use a single source file, they need to be re-rendered each time using `./master-render.py -cx`. You can also manually delete the `Pop/cursors` directory. Additional information about rendering the cursors is found in `src/cursors/README.md`

### Symbolic Links

Pop_Icons uses symbolic links to save on disk space and match a larger number of icon names without needing as many unique icons. 

Symbolic link definitions are separated out into `fullcolor` for the full-color icons, and `scalable` for the symbolic icons. Each directory contains a `.list` file for each icon category. Each line in a `.list` file defines exactly one output symlink. The format for each line is `link-target link-name` similar to the `ln` command. For more information regarding symlinks, see the [`src/symlinks/README.md`](src/symlinks/README.md) file.

### Metadata

Currently theme metadata is stored in the main folder within [`index.theme.in`](index.theme.in) and [`cursor.theme.in`](cursor.theme.in). When the output files of these is generated, these are copied directly into the output folder without modification; automatic generation is a planned feature for a later release. In the meantime, modify these files directly and use `./master-render.py` to copy them to the correct locations. 


## Pull Requests

We happily consider all pull requests sent our way. When submitting a PR, be sure to abide by our [Code of Conduct](https://github.com/pop-os/code-of-conduct), as submissions in violation will be rejected.

To improve the quality of your submission and increase the chances of acceptance, please consider the following guidelines:

* Ensure that your contribution is of a generally finished quality. PRs and contributions requiring further development by the Pop_OS team may not be accepted.

* Follow existing code and design style where possible. Submissions which don't follow our code or design style may require changes to be accepted. Ensure that icons follow our design language and generally "fit in" with the other Pop Icons. When in doubt, mark your PR as a draft and request assistance from a Pop Icons maintainer.

* Ensure that your changes to icons/cursors follow our in-place development practices. Submissions which add/remove/rename icons within the [`Pop`](./Pop) folder without corresponding changes in the [`src`](./src) folder _will_ not be accepted. 

* Consider doing a full-render of the theme before you submit a PR (`./master-render.py -c`). This will erase any existing output files and ensure the theme is in a good, maintainable state and that your changes have been applied in a way which ensures that they will be carried over in the future. _Contributions where running `./master-render.py -c` creates a diff verses the git `HEAD` commit will not be accepted!_

## Missing Icons & Requests

You can file an icon request as a [GitHub issue](https://github.com/pop-os/icon-theme/issues/new). Filing an icon request or reporting a missing icon, please take care in providing the following useful information: 

 - A screenshot of your issue or an image of the original icon you are requesting to be themed
 - The file name for the missing icon or the requested icon, for example `image-adjust.svg` or `system-shutdown.svg`

Note: Pop does not supply icons for third-party applications, only those which come with Pop!_OS. 

## Donate & Support

Pop_Icons use Sam Hewitt's Paper icons as an architectural base, although the icon artwork is new. If you would like to support development by making a donation you can do so [here](https://snwh.org/donate) or by becoming a supporter on [Patreon](http://patreon.com/snwh/) or [Liberapay](http://liberapay.com/snwh/). 
