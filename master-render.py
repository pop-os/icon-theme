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
    subprocess.run('./render-bitmaps.py')

def render_symbolics() -> None:
    print('  -- Rendering symbolic icons...')
    os.chdir(SRCDIR / 'scalable')
    subprocess.run('./extract-symbolic-icons.rb')

def generate_symlinks() -> None:
    print('  -- Generating symbolic links...')
    os.chdir(SRCDIR / 'symlinks')
    subprocess.run('./generate-symlinks.sh')
    os.chdir(SRCDIR / 'scalable')
    subprocess.run('./generate-symbolic-symlinks.sh')

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

def do_render(clean:bool = False) -> None:
    if clean:
        clean_dirs()
    render_bitmaps()
    render_symbolics()
    generate_symlinks()
    install_metadata()

parser = argparse.ArgumentParser(description='Render icons for the Pop Icon Theme')

parser.add_argument(
    '-c',
    '--clean',
    action='store_true',
    help='Remove existing files before rendering (takes a long time to render)'
)

args = parser.parse_args()
    
do_render(clean=args.clean)
