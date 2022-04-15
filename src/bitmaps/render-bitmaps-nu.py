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

import os
import sys
import xml.sax
import subprocess
import argparse
from pathlib import Path

BINDIR = Path('/usr/bin')
BASEDIR = Path('../../')
THEMENAME:str = 'Pop'
INKSCAPE = BINDIR / 'inkscape'
THEMEDIR = BASEDIR / THEMENAME
CONTEXTS = (
	'actions',
	'apps',
	'categories',
	'devices',
	'emblems',
	'logos',
	'mimetypes',
	'places',
	'preferences',
	'status',
)

DPI_DIRECT = 96

def main(args, src):
	
	def render_icon(src_file, rect, dpi, output_file) -> None:
		cmd = [
			INKSCAPE, 
			'-d', str(dpi), # --export-dpi
			'-i', rect, # --export-id
			'-o', output_file, # --export-filename
			src_file # input file
		]

		print(f'...Rendering {output_file}')
		subprocess.run(cmd)
	
	class IconHandler(xml.sax.ContentHandler):
		ROOT = 0
		SVG = 1
		LAYER = 2
		OTHER = 3
		TEXT = 4

		def __init__(self, path, force=False, filter=None) -> None:
			self.stack = [self.ROOT]
			self.inside = [self.ROOT]
			self.path = path
			self.rects = []
			self.state = self.ROOT
			self.chars = ""
			self.force = force
			self.filter = filter
		
		def endDocument(self):
			pass

		def startElement(self, name, attrs) -> None:
			# Putting these conditionals here for better cleanliness.
			# Otherwise the conditionals later in the code are long and gross.
			name_is_g:bool = name == 'g'
			name_is_text:bool = name == 'text'
			is_groupmode: bool = 'inkscape:groupmode' in attrs
			is_label:bool = 'inkscape:label' in attrs
			groupmode_is_layer:bool = attrs['inkscape:groupmode'] == 'layer'
			layer_is_baseplate:bool = attrs['inkscape:label'].startswith('Baseplate')
			is_context:bool = attrs['inkscape:label'] == 'context'
			is_icon_name = attrs['inkscape:label'] == 'icon-name'
			
			if self.inside[-1] == self.ROOT:
				if name == 'svg':
					self.stack.append(self.SVG)
					self.inside.append(self.SVG)
					return
			
			elif self.inside[-1] == self.SVG:
				if name_is_g and is_groupmode and is_label:
					if groupmode_is_layer and layer_is_baseplate:
						self.stack.append(self.LAYER)
						self.inside.append(self.LAYER)
						self.context = None
						self.icon_name = None
						self.rects = []
						return
			
			elif self.inside[-1] == self.LAYER:
				if name_is_text and is_label and is_context:
					self.stack.append(self.TEXT)
					self.inside.append(self.TEXT)
					self.text='context'
					self.chars = ""
					return
				elif name_is_text and is_label and is_icon_name:
					self.stack.append(self.TEXT)
					self.inside.append(self.TEXT)
					self.text='icon-name'
					self.chars = ""
					return
				
				elif name == 'rect':
					self.rects.append(attrs)
			
			self.stack.append(self.OTHER)
		
		def endElement(self, name):
			stacked = self.stack.pop()
			if self.inside[-1] == stacked:
				self.inside.pop()

			if stacked == self.TEXT and self.text is not None:
				assert self.text in ['context', 'icon-name']
				if self.text == 'context':
					self.context = self.chars
				elif self.text == 'icon-name':
					self.icon_name = self.chars
				self.text = None
			elif stacked == self.LAYER:
				assert self.icon_name
				assert self.context

				if self.filter is not None and not self.icon_name in self.filter:
					return

				print (self.context, self.icon_name)
				for rect in self.rects:
					for dpi_factor in DPIS:
						width = rect['width']
						height = rect['height']
						id = rect['id']
						dpi = DPI_1_TO_1 * dpi_factor

						size_str = "%sx%s" % (width, height)
						if dpi_factor != 1:
							size_str += "@%sx" % dpi_factor

						dir = os.path.join(THEMEDIR, size_str, self.context)
						outfile = os.path.join(dir, self.icon_name+'.svg')
						if not os.path.exists(dir):
							os.makedirs(dir)
						# Do a time based check!
						if self.force or not os.path.exists(outfile):
							inkscape_render_rect(self.path, id, dpi, outfile)
							sys.stdout.write('.')
						else:
							stat_in = os.stat(self.path)
							stat_out = os.stat(outfile)
							if stat_in.st_mtime > stat_out.st_mtime:
								inkscape_render_rect(self.path, id, dpi, outfile)
								sys.stdout.write('.')
							else:
								sys.stdout.write('-')
						sys.stdout.flush()
				sys.stdout.write('\n')
				sys.stdout.flush()

		def characters(self, chars):
			self.chars += chars.strip()

	if not args.svg:
		if not os.path.exists(THEMEDIR):
			os.mkdir(THEMEDIR)
		print ('')
		print ('Rendering from SVGs in', SRC)
		print ('')
		for file in os.listdir(SRC):
			if file[-4:] == '.svg':
				file = os.path.join(SRC, file)
				handler = IconHandler(file)
				xml.sax.parse(open(file), handler)
		print ('')
	else:
		file = os.path.join(SRC, args.svg + '.svg')

		if os.path.exists(os.path.join(file)):
			handler = ContentHandler(file, True, filter=args.filter)
			xml.sax.parse(open(file), handler)
		else:
			# icon not in this directory, try the next one
			pass

parser = argparse.ArgumentParser(description='Render icons from SVG to PNG')

parser.add_argument('svg', type=str, nargs='?', metavar='SVG',
					help="Optional SVG names (without extensions) to render. If not given, render all icons")
parser.add_argument('filter', type=str, nargs='?', metavar='FILTER',
					help="Optional filter for the SVG file")

args = parser.parse_args()

for ctx in CONTEXTS:
	SRC = os.path.join('.', ctx)
	main(args, SRC)
