#!/usr/bin/env python3

"""Restore the cursor alias symlinks that `install_subdir` dereferences.

Meson copies symlinked directories by value.
"""

import os
import shutil
import sys

THEME = "Pop"
SUBDIR = "cursors_scalable"


def install_prefix() -> str:
    # MESON_INSTALL_DESTDIR_PREFIX needs meson 0.57; fall back for older.
    prefix = os.environ.get("MESON_INSTALL_DESTDIR_PREFIX")
    if prefix:
        return prefix
    prefix = os.environ.get("MESON_INSTALL_PREFIX", "/usr")
    destdir = os.environ.get("DESTDIR", "")
    if destdir:
        return os.path.join(destdir, prefix.lstrip("/"))
    return prefix


def main() -> int:
    source_root = os.environ.get("MESON_SOURCE_ROOT", os.getcwd())
    source = os.path.join(source_root, THEME, SUBDIR)
    target = os.path.join(install_prefix(), "share", "icons", THEME, SUBDIR)

    if not os.path.isdir(source) or not os.path.isdir(target):
        return 0

    linked = 0
    for entry in sorted(os.listdir(source)):
        path = os.path.join(source, entry)
        if not os.path.islink(path):
            continue
        installed = os.path.join(target, entry)
        if os.path.islink(installed):
            continue
        if os.path.isdir(installed):
            shutil.rmtree(installed)
        elif os.path.exists(installed):
            os.unlink(installed)
        os.symlink(os.readlink(path), installed)
        linked += 1

    if linked:
        print(f"Relinked {linked} cursor aliases in {SUBDIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
