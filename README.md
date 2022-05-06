Pop_Icons
================

Pop_Icons is the icon theme for Pop!_OS. It uses a semi-flat design with raised 3D motifs to help give depth to icons. 

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

By default it installs to `/usr/`, but you can specify a different directory with a prefix like `/usr/local` or `$HOME/.local`, for example:

```sh
meson -Dprefix=$HOME/.local build
ninja -C "build" install
```

After which you should be able to pick Pop as your icon or cursor theme in GNOME Tweaks, or you can set either from a terminal with:

```bash
# set the icon theme
gsettings set org.gnome.desktop.interface icon-theme "Pop"
# or the cursor theme
gsettings set org.gnome.desktop.interface cursor-theme "Pop"
```

### Uninstalling Pop

To uninstall Pop, simply run the following. (If you installed it without superuser priveleges just omit the  `sudo`.)

```bash
sudo ninja -C "build" uninstall
```

Once uninstalled you can reset your icon and cursor theme to the default setting by running the following.

```bash
# reset icon theme to default
gsettings reset org.gnome.desktop.interface icon-theme
# reset cursor theme to default
gsettings reset org.gnome.desktop.interface cursor-theme
```

## Modifying the theme

For information on modifications and contributing to the theme, see the 
README.md in the `src` folder.

## Missing Icons & Requests

You can file an icon request as a [GitHub issue](https://github.com/pop-os/icon-theme/issues/new). Filing an icon request or reporting a missing icon, please take care in providing the following useful information: 

 - A screenshot of your issue or an image of the original icon you are requesting to be themed
 - The file name for the missing icon or the requested icon, for example `image-adjust.svg` or `system-shutdown.svg`

Note: Pop does not supply icons for third-party applications, only those which come with Pop!_OS. 

## Donate & Support

Pop_Icons use Sam Hewitt's Paper icons as an arcitechtural base, although the icon artwork is new. If you would like to support development by making a donation you can do so [here](https://snwh.org/donate) or by becoming a supporter on [Patreon](http://patreon.com/snwh/) or [Liberapay](http://liberapay.com/snwh/). &#x1F60A;
