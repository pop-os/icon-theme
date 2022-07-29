#!/usr/bin/python3

"""
# This file is part of the Pop Icon Theme and is free software; you can 
# redistribute it and/or modify it under  the terms of the GNU Lesser General
# Public License as published by the Free Software Foundation; version 3.
#
# This file is part of the Pop Icon Theme and is distributed in the hope that 
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/lgpl-3.0.txt>
"""

import argparse
from ast import parse
import os
import shutil
import subprocess
from pathlib import Path

from importlib_metadata import sys

THEMENAME:str = 'Pop'
BINDIR = Path('/usr/bin')
BASEDIR = Path(os.getcwd())
SRCDIR = BASEDIR / 'src'
THEMEDIR = BASEDIR / THEMENAME
SIZES = (
    '8x8',
    '16x16',
    '24x24',
    '32x32',
    '48x48',
    '64x64',
    '128x128',
    '256x256',
    '512x512'
)

def render_bitmaps() -> None:
    print('  -- Rendering bitmap icons...')
    os.chdir(SRCDIR / 'bitmaps')
    try:
        subprocess.run('./render-bitmaps.py', check=True)
    except subprocess.CalledProcessError:
        print('Failed to render fullcolor icons. See output above.')
        sys.exit(1)

def render_symbolics() -> None:
    print('  -- Rendering symbolic icons...')
    os.chdir(SRCDIR / 'scalable')
    try:
        subprocess.run('./extract-symbolic-icons.rb', check=True)
    except subprocess.CalledProcessError:
        print('Failed to render symbolic icons. See output above.')
        sys.exit(1)

def cleanup_unoptomized_renders() -> None:
    print('  -- Cleaning up any unoptimized output')

def generate_symlinks() -> None:
    print('  -- Generating symbolic links...')
    os.chdir(SRCDIR / 'symlinks')
    try:
        subprocess.run('./generate-symlinks.sh', check=True)
    except subprocess.CalledProcessError:
        print('Failed to generate fullcolor symlinks. See output above.')
        sys.exit(1)
    os.chdir(SRCDIR / 'scalable')
    try:
        subprocess.run('./generate-symbolic-symlinks.sh', check=True)
    except subprocess.CalledProcessError:
        print('Failed to generate sylbolic symlinks. See output above.')
        sys.exit(1)

def render_cursors() -> None:
    print('  -- Rendering cursors...')
    cursors_dir = SRCDIR / 'cursors'
    template_dir = cursors_dir / 'templates'
    output_dir = cursors_dir / 'bitmaps'

    os.chdir(cursors_dir)
    if output_dir.exists():
        print('    -- Cleaning up old render')
        shutil.rmtree(output_dir)
    shutil.copytree(template_dir, output_dir)

    print('    -- Rendering cursor bitmaps')
    subprocess.run(['./render-cursors.py', '-n 0', 'source-cursors.svg'])
    
    print('    -- Generatig cursor files')
    subprocess.run('./x11-make.sh')
    subprocess.run('./w32-make.sh')
    


def install_metadata() -> None:
    print('  -- Installing theme Metadata...')
    for file in ('index.theme', 'cursor.theme'):
        file_path = BASEDIR / f'{file}.in'
        shutil.copyfile(file_path, f'{THEMEDIR}/{file}')

def clean_dirs() -> None:
    print('Cleaning up previous renders')
    os.chdir(THEMEDIR)
    for size in SIZES:
        size_dir = THEMEDIR / size
        if size_dir.exists():
            print(f'  -- Removing {size_dir}')
            shutil.rmtree(size_dir)
        else:
            print(f'  ** Skipping {size_dir}')
    scalable_dir = THEMEDIR / 'scalable'
    if scalable_dir.exists():
        print('  -- Removing symbolic icons')
        shutil.rmtree(scalable_dir)
    else:
        print('  ** Skipping symbolic icons')

def do_render(
        clean:bool = False,
        skip_bitmaps:bool = False,
        skip_symbolics:bool = False,
        skip_cursors:bool = False,
        skip_symlinks:bool = False,
        skip_metadata:bool = False
) -> None:
    if clean:
        clean_dirs()
    if not skip_bitmaps:
        render_bitmaps()
    if not skip_symbolics:
        render_symbolics()
    if not skip_cursors:
        render_cursors()
    if not skip_symlinks:
        generate_symlinks()
    if not skip_metadata:
        install_metadata()

parser = argparse.ArgumentParser(description='Render icons for the Pop Icon Theme')

parser.add_argument(
    '-c',
    '--clean',
    action='store_true',
    help='Remove existing files before rendering (takes a long time to render)'
)
parser.add_argument(
    '-b',
    '--skip-bitmaps',
    action='store_true',
    help='Skip rendering of bitmaps'
)
parser.add_argument(
    '-s',
    '--skip-symbolics',
    action='store_true',
    help='Skip rendering of symbolic icons'
)
parser.add_argument(
    '-x',
    '--skip-cursors',
    action='store_true',
    help='Skip rendering of cursors'
)
parser.add_argument(
    '-l',
    '--skip-links',
    action='store_true',
    help='Skip symlink generation'
)
parser.add_argument(
    '-m',
    '--skip-metadata',
    action='store_true',
    help='Skip installation of metadata'
)

args = parser.parse_args()
    
do_render(
    clean=args.clean,
    skip_bitmaps=args.skip_bitmaps,
    skip_symbolics=args.skip_symbolics,
    skip_cursors=args.skip_cursors,
    skip_symlinks=args.skip_links,
    skip_metadata=args.skip_metadata
)
