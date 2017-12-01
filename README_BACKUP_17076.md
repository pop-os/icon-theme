<p align="center">
  <img src="https://github.com/system76/pop-icon-theme/raw/master/Pop_icons-logo.png" alt="preview"/>
</p>

-------------------

Pop is a free and open source SVG icon theme for Linux, based on [Paper Icon Set](https://github.com/snwh/paper-icon-theme) and [Papirus](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme).
<p align="center">
<<<<<<< HEAD
<img src="https://github.com/system76/pop-icon-theme/raw/master/preview.png"/>
=======
  <img alt="apps" src="https://img.shields.io/badge/apps_icons-3200%2B-5294e2.svg?style=flat-square"/>
  <img alt="actions" src="https://img.shields.io/badge/actions_icons-1800%2B-5294e2.svg?style=flat-square"/>
  <img alt="panel" src="https://img.shields.io/badge/panel_icons-1700%2B-5294e2.svg?style=flat-square"/>
  <img alt="places" src="https://img.shields.io/badge/places_icons-690%2B-5294e2.svg?style=flat-square"/>
>>>>>>> upstream/master
</p>


-------------------

<<<<<<< HEAD
=======
 - Papirus (for Arc / Arc Darker)
 - Papirus Dark (for Arc Dark)
 - Papirus Light (light theme with Breeze colors)
 - Papirus Adapta (for Adapta)
 - Papirus Adapta Nokto (for Adapta Nokto)
 - ePapirus (for elementary OS and Pantheon Desktop)
>>>>>>> upstream/master

## Installation
You can install Pop from our official [PPA](https://launchpad.net/~system76-dev/+archive/ubuntu/stable):

```
sudo add-apt-repository ppa:system76/pop
sudo apt-get update
sudo apt-get install pop-theme
```

This will install the complete look; individual components can be installed separately:
```
sudo apt install pop-icon-theme
```
#### HOME directory for GTK


You can also install the Pop icon set from git by cloning the repository, and using these commands:
```
sudo make install
sudo make post-install
```
Note that an initial `./configure` or `make` is not required. 


#### Remove
Pop has [Folder colors](http://foldercolor.tuxfamily.org/) support that allows you to change a global color of folders or just one of them.


### Unofficial packages
- For GTK, use icons alongside [Pop GTK Theme](https://github.com/system76/pop-gtk-theme)
 > Window Titles: Fira Sans SemiBold 10

<<<<<<< HEAD
 > Interface: Fira Sans Book 10
=======
Packages in this section are not part of the official repositories. If you have a problem or a question, please contact the package maintainer.

| **Distro** | **Maintainer**    | **Package**                              |
| :--------- | :---------------- | :--------------------------------------- |
| Arch Linux | Felix Yan         | `sudo pacman -S papirus-icon-theme` <sup>[[link](https://www.archlinux.org/packages/community/any/papirus-icon-theme/)]</sup> |
| Arch Linux | Edgard Castro     | [papirus-icon-theme-git](https://aur.archlinux.org/packages/papirus-icon-theme-git/) <sup>AUR</sup> |
| Fedora     | Dirk Davidis      | [papirus-icon-theme](https://copr.fedorainfracloud.org/coprs/dirkdavidis/papirus-icon-theme/) <sup>copr</sup> |
| Manjaro    | Nikola Yanev      | [papirus-icon-theme](http://download.tuxfamily.org/gericom/README.html) |
| openSUSE   | Konstantin Voinov | [papirus-icon-theme](https://software.opensuse.org/download.html?project=home:kill_it&package=papirus-icon-theme) <sup>OBS [[link](https://build.opensuse.org/package/show/home:kill_it/papirus-icon-theme)]</sub> |
| Solus      | Joshua Strobl     | `sudo eopkg install papirus-icon-theme`  |

**NOTE:** If you are a maintainer and want to be in the list, please create an issue or make a pull request.

## Hardcoded icons

Some software uses an absolute path instead of the icon name in a .desktop file or in the source code which makes them unthemable.

### Hardcoded application icons

To deal with hardcoded application icons we recommend using [hardcode-fixer](https://github.com/Foggalong/hardcode-fixer). Papirus supports most of the applications in the [list](https://github.com/Foggalong/hardcode-fixer/blob/master/tofix.csv). If [hardcode-fixer](https://github.com/Foggalong/hardcode-fixer) doesn't support your favorite app yet, please open an issue [here](https://github.com/Foggalong/hardcode-fixer/issues) or edit your .desktop file manually.

### Hardcoded tray icons

To fix hardcoded tray icons Papirus supports [Hardcode-Tray](https://github.com/bil-elmoussaoui/Hardcode-Tray) script. A list of supported applications is available [here](https://github.com/bil-elmoussaoui/Hardcode-Tray/tree/master/data/database).

**NOTE:** To get Papirus to work right with Hardcode-Tray, use the hardcode-tray option `--conversion-tool RSVGConvert`:

```
sudo -E hardcode-tray --conversion-tool RSVGConvert --size 22 --theme Papirus
```

**Size recommendations:**
- Unity 22px
- KDE 22px
- GNOME 16px ([see](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme#manual-fixes) for more info)
- XFCE 22px ([see](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme#manual-fixes) for more info)
- Pantheon 24px
- Cinnamon 16px


![hardcode-tray](http://i.imgur.com/6hFm6aj.png)

**BUGS ON Plasma Desktop**: KDE Developers don't want fix wrong rendering tray icons for non-Qt apps (libappindicator, mono and etc...). After applying hardcode-tray - icons will be blurred!

See more info [here](https://bugs.kde.org/show_bug.cgi?id=366062) and please vote for this bug.

## KDE colorscheme

Support for monochrome icons for KDE colorscheme is now available:
- Papirus - for dark plasma theme & light color scheme
- Papirus Dark - for dark plasma theme & color scheme
- Papirus Light - for light plasma theme & color scheme

![kde-color-scheme](http://i.imgur.com/oM1qhQH.png)

**NOTE:** Non-KDE apps don't support KDE colorscheme on the system tray, but you can replace color manually.
>>>>>>> upstream/master

 > Documents: Roboto Slab Regular 11

 > Monospace: Fira Mono Regular 11

<<<<<<< HEAD
=======
Available colors:

![Folder Color Preview](https://i.imgur.com/erG808D.png)

For KDE, colors of individual folders can be changed using [dolphin-folder-color](https://github.com/audoban/dolphin-folder-color).

Also, you can use our [papirus-folders](https://github.com/PapirusDevelopmentTeam/papirus-folders) script to apply the color of folders system-wide.

## Extras

- [Papirus theme for LibreOffice](https://github.com/PapirusDevelopmentTeam/papirus-libreoffice-theme)
- [Papirus themes for FileZilla](https://github.com/PapirusDevelopmentTeam/papirus-filezilla-themes)
- [Papirus theme for SMPlayer](https://github.com/PapirusDevelopmentTeam/papirus-smplayer-theme)
- [Papirus themes for Claws Mail](https://github.com/PapirusDevelopmentTeam/papirus-claws-mail-theme)
- [Papirus theme for aMule](https://github.com/PapirusDevelopmentTeam/papirus-amule-theme)

## Recommendations

- For GTK, better use icons alongside GTK theme [Arc Themes](https://github.com/horst3180/arc-theme) or [Adapta Themes](https://github.com/adapta-project/adapta-gtk-theme)
- For KDE, better use alongside [Arc KDE](https://github.com/PapirusDevelopmentTeam/arc-kde) or [Adapta KDE](https://github.com/PapirusDevelopmentTeam/adapta-kde)

## Manual fixes

<details>
<summary>For Cinnamon users</summary>

For Cinnamon users who want to use Papirus icon theme with [arc-theme](https://github.com/horst3180/arc-theme) we recommend fix color icons on panel:

```
sudo sed -i.orig 's/white/#d3dae3/g' /usr/share/themes/Arc-Dark/cinnamon/cinnamon.css
```

![Cinnamon Arc-Dark theme fix](http://i.imgur.com/XXejgtD.png)

To deal with blurred panel icons, increase the panel size up to 30px in `Systems Settings` → `Panel` (see [screenshot](https://i.imgur.com/oToRBYv.png)).
</details>

<details>
<summary>For GNOME 3 users</summary>

For GNOME users who want use Papirus icon theme with [arc-theme](https://github.com/horst3180/arc-theme), we recommend change icons color for panel:
```
sudo sed -i.orig 's/white/#d3dae3/g' /usr/share/themes/Arc-Dark/gnome-shell/gnome-shell.css
```
![GNOME Arc-Dark theme fix](http://i.imgur.com/5Mb2HRs.png)

Also, we recommend using [AppIndicator/KStatusNotifierItem Support](https://extensions.gnome.org/extension/615/appindicator-support/) extension for appindicator-apps, because patched version of sni-qt for hardcode-tray doesn't work without that on gnome-shell.

</details>
>>>>>>> upstream/master

<details>
<summary>For Unity users</summary>

For Unity users, we recommend installing patched [Notify-OSD](https://launchpad.net/~leolik/+archive/ubuntu/leolik) and change an icon size to 33px.

*~/.notify-osd* file:

```
slot-allocation = dynamic
bubble-expire-timeout = 10sec
bubble-vertical-gap = 10px
bubble-horizontal-gap = 10px
bubble-corner-radius = 24px
bubble-icon-size = 33px
bubble-gauge-size = 6px
bubble-width = 240px
bubble-background-color = 2f343f
bubble-background-opacity = 95%
text-margin-size = 10px
text-title-size = 100%
text-title-weight = bold
text-title-color = adb7bf
text-title-opacity = 100%
text-body-size = 90%
text-body-weight = normal
text-body-color = eaeaea
text-body-opacity = 100%
text-shadow-opacity = 50%
location = 1
bubble-prevent-fade = 1
bubble-close-on-click = 1
bubble-as-desktop-bg = 0
```

![notify-fix](notify-fix.png)

Also, you can change [Unity launcher icon](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/tree/master/Papirus/extra/unity) and [unity-tweak-tool icons](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/tree/master/Papirus/extra/unity-tweak-tool). Look into the extra folder in the icon theme.
</details>

<<<<<<< HEAD
=======
<details>
<summary>For Xfce users</summary>

Here are a few recommendations for Xfce users.

#### Thunar File Manager

Go to `Edit` → `Preferences...`. Click on `Side Pane` tab. Under `Side Pane`, look for `Icon Size` and set to `Very Small`.

![thunar-prefecences](http://i.imgur.com/Iu1TIEa.png)

#### Notification Area

Go to `Settings Manager` → `Panel` → `Items` tab. Select `Notification Area` item and click on `Edit currently selected item` button. Under `Appearance` set the following options:

- Set `Maximum icon size (px)` to `24`
- Uncheck `Show frame`

![xfce4-notification-area](http://i.imgur.com/MopCZBZ.png)
</details>

<details>
<summary>For elementary/Pantheon users</summary>
- With light wallpaper we recommend use non-transparency wingpanel:

```
gsettings set org.pantheon.desktop.wingpanel use-transparency false
```

</details>

>>>>>>> upstream/master
## Icon request

- Application name
- Icon name (see desktop-file option **Icon** on `/usr/share/applications`)
- Original icon image

## Contribute

We welcome user contributions. If you don't know where to start, we've compiled a list of things they would like to see in your pull request:

- new icons for missing applications
- symbolic links to an existing icon
- resolving open issues
- spelling, grammar, phrasing
- improvements to our scripts

Inside [tools/work](tools/work) you find a step-by-step guide, an environment, and tools that help you:

- [create a new icon](tools/work#create-a-new-icon) from template
- [make a symlink to an existing icon](tools/work#make-symlinks-to-an-existing-icon)
- [edit an existing icon](tools/work#edit-an-existing-icon)
- convert your icon to all variants the theme

We are waiting for your pull requests and would love to see this icon theme become as complete as possible.

## Donate


Feel free to donate to the Papirus set to support the great work that goes into these icons!
<span class="paypal"><a href="https://www.paypal.me/varlesh" title="Donate to this project using Paypal"><img src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal donate button" /></a></span>

BTC: `1HwE62Zb8PyyY1XAR6Ykweix2ht8NAjvf5`

## License

GNU LGPL v3.0
