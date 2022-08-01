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


## Rendering Functions
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
        print('    -- Output dir exists, use --clean to re-render')
        return
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


## Artifact Cleanup/Removal Functions
def clean_bitmaps() -> None:
    print('  -- Removing Fullcolor Icons')
    for size in SIZES:
        size_dir = THEMEDIR / size
        if size_dir.exists():
            print(f'    -- Removing {size_dir}')
            shutil.rmtree(size_dir)
        else:
            print(f'    ** Skipping {size_dir}')

def clean_symbolics() -> None:
    scalable_dir = THEMEDIR / 'scalable'
    if scalable_dir.exists():
        print('  -- Removing symbolic icons')
        shutil.rmtree(scalable_dir)

def clean_cursors() -> None:
    cursor_dir = THEMEDIR / 'cursors'
    cursors_dir = SRCDIR / 'cursors'
    template_dir = cursors_dir / 'templates'
    output_dir = cursors_dir / 'bitmaps'
    if cursor_dir.exists():
        print('  -- Removing cursors')
        shutil.rmtree(cursor_dir)
    if output_dir.exists():
        print('    -- Cleaning up old render')
        shutil.rmtree(output_dir)

def clean_metadata() -> None:
    print('  -- Removing Metadata')
    for file in ('index.theme', 'cursor.theme'):
        file_path = THEMEDIR / file
        try:
            file_path.unlink()
            print(f'    -- Removed {file}')
        except FileNotFoundError:
            print(f'    ** Skipping {file}')

def clean_dirs(**kwargs) -> None:
    print('-- Cleaning up previous renders')
    os.chdir(THEMEDIR)

    if kwargs['everything']:
        print('  -- Performing Full Cleanup')
        clean_bitmaps()
        clean_symbolics()
        clean_cursors()
        clean_metadata()
        return

    # Cleanup Fullcolors
    if kwargs['bitmaps']:
        clean_bitmaps()
    else:
        print('  ** Skipping removing bitmaps')
    
    # Cleanup Symbolics
    if kwargs['symbolics']:
        clean_symbolics()
    else:
        print('  ** Skipping removing symbolic icons')
    
    # Cleanup Cursors
    if kwargs['cursors']:
        clean_cursors()
    else:
        print('  ** Skipping removing Cursors')

    # Cleanup Metadata
    if kwargs['metadata']:
        clean_metadata()
    else:
        print('  ** Skipping removing Metadata')

def do_render(args) -> None:
    if args.clean:
        clean_dirs(
            everything=args.all,
            bitmaps=args.bitmaps,
            symbolics=args.symbolics,
            cursors=args.cursors,
            metadata=args.metadata
        )
    if args.all:
        render_bitmaps()
        render_symbolics()
        render_cursors()
        generate_symlinks()
        install_metadata()
        return

    if args.bitmaps:
        render_bitmaps()
    if args.symbolics:
        render_symbolics()
    if args.cursors:
        render_cursors()
    if args.links:
        generate_symlinks()
    if args.metadata:
        install_metadata()

parser = argparse.ArgumentParser(description='Render icons for the Pop Icon Theme')

parser.add_argument(
    '-c',
    '--clean',
    action='store_true',
    help='Remove existing files before rendering (takes a long time to render)'
)

parser.add_argument(
    '-a',
    '--all',
    action='store_true',
    help='Render all items (Default)'
)
parser.add_argument(
    '-b',
    '--bitmaps',
    action='store_true',
    help='Render bitmap (fullcolor) icons'
)
parser.add_argument(
    '-s',
    '--symbolics',
    action='store_true',
    help='Render Symbolic Icons'
)
parser.add_argument(
    '-x',
    '--cursors',
    action='store_true',
    help='Render Cursors'
)
parser.add_argument(
    '-l',
    '--links',
    action='store_true',
    help='Generate Theme Symlinks'
)
parser.add_argument(
    '-m',
    '--metadata',
    action='store_true',
    help='Generate Metadata'
)

args = parser.parse_args()

if not True in (args.bitmaps,
                args.symbolics,
                args.cursors,
                args.links,
                args.metadata):
    args.all = True
else:
    args.all = False
    
do_render(args)
