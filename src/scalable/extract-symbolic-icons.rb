#!/usr/bin/env ruby
#
# Legal Stuff:
#
# This file is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free Software
# Foundation; version 3.
#
# This file is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/lgpl-3.0.txt>
#
#
# Thanks to the GNOME icon developers for the original version of this script


require "rexml/document"
require "fileutils"

include REXML

VERBOSE = false

# INKSCAPE = 'flatpak run org.inkscape.Inkscape'
INKSCAPE = '/usr/bin/inkscape'
SRC = "./source-symbolic.svg"
PREFIX = "../../Pop/scalable"
SVGO_CONFIG = "../../svgo.config.js"

# install with `sudo npm install -g svgo`
SVGO = '/usr/local/bin/svgo'
SCOUR = '/usr/bin/scour'

def chopSVG(icon)
	FileUtils.mkdir_p(icon[:dir]) unless File.exists?(icon[:dir])
	unless (File.exists?(icon[:file]) && !icon[:forcerender])
		FileUtils.cp(SRC,icon[:file]) 
		puts " >> #{icon[:name]} from #{icon[:file]} as #{icon[:id]}"
		# cmd = "#{INKSCAPE} #{icon[:file]} --select #{icon[:id]} "
		# cmd += '--verb="FitCanvasToSelection;EditCopy;EditSelectAllInAllLayers;'\
		#   'EditDelete;EditPasteInPlace;EditSelectAll;FileVacuum;FileSave;FileQuit"'
		cmd = "#{INKSCAPE} -i #{icon[:id]} -o #{icon[:file]} --export-id-only #{SRC}"
	  cmd += " > /dev/null 2>&1" unless VERBOSE
	  puts " Running '#{cmd}'" if VERBOSE
		system(cmd)
		#saving as plain SVG gets rid of the classes :/
		cmd = "#{INKSCAPE} --vacuum-defs -z #{icon[:file]} --export-plain-svg=#{icon[:file]}"
		cmd += " > /dev/null 2>&1" unless VERBOSE
		system(cmd)
		# #completely vaccuum with svgo
		# cmd = "#{SVGO} --pretty -i  #{icon[:file]} -o  #{icon[:file]}"
		
		if (File.exist?(SCOUR)) #clean up SVGs with scour
			puts " !! #{icon[:name]} in #{icon[:file]}"
			FileUtils.copy(icon[:file], "#{icon[:file]}-unop") 

			cmd = "#{SCOUR} -i #{icon[:file]}-unop -o #{icon[:file]} "
			cmd += "--enable-viewboxing --enable-id-stripping --enable-comment-stripping --shorten-ids --indent=none"
			cmd += " > /dev/null 2>&1" unless VERBOSE
			puts " Running '#{cmd}'" if VERBOSE
			system(cmd)
			FileUtils.remove("#{icon[:file]}-unop")
		end

		if (File.exists?(SVGO)) #optimize SVGs
			puts " !! #{icon[:name]} in #{icon[:file]}"
			FileUtils.copy(icon[:file], "#{icon[:file]}-unop") 

			cmd = "#{SVGO} --config=#{SVGO_CONFIG} --input=#{icon[:file]} --output=#{icon[:file]}"
			cmd += " > /dev/null 2>&1" unless VERBOSE
			puts " Running '#{cmd}'" if VERBOSE
			system(cmd)
			FileUtils.remove("#{icon[:file]}-unop")
		end

		# crop
		svgcrop = Document.new(File.new(icon[:file], 'r'))
		svgcrop.root.each_element("//rect") do |rect| 
			w = ((rect.attributes["width"].to_f * 10).round / 10.0).to_i #get rid of 16 vs 15.99999 
			h = ((rect.attributes["width"].to_f * 10).round / 10.0).to_i #Inkscape bugs
			if w == 16 && h == 16
				rect.remove
			end
		end
		icon_f = File.new(icon[:file],'w+')
		icon_f.puts svgcrop
		icon_f.close
	else
		puts " -- #{icon[:name]} already exists"
	end
end #end of function

def get_output_filename(d,n)
	if (/rtl$/.match(n))
		outfile = "#{d}/#{n.chomp('-rtl')}-symbolic-rtl.svg"
	else
		outfile = "#{d}/#{n}-symbolic.svg"
	end
	return outfile
end

#main
# Open SVG file.
svg = Document.new(File.new(SRC, 'r'))

if (ARGV[0].nil?) #render all SVGs
	puts "Rendering from icons in #{SRC}"
	# Go through every layer.
	svg.root.each_element("/svg/g[@inkscape:groupmode='layer']") do |context| 
		context_name = context.attributes.get_attribute("inkscape:label").value  
		puts "Going through layer '" + context_name + "'"
		context.each_element("g") do |icon|
			#puts "DEBUG #{icon.attributes.get_attribute('id')}"
			dir = "#{PREFIX}/#{context_name}"
			icon_name = icon.attributes.get_attribute("inkscape:label").value
			if icon_name.end_with?("-alt")
				puts " >> skipping icon '" + icon_name + "'"
			else
				chopSVG({ :name => icon_name,
						:id => icon.attributes.get_attribute("id"),
						:dir => dir,
						:file => get_output_filename(dir, icon_name)})
			end
		end
	end
	puts "\nrendered all SVGs"
else #only render the icons passed
	icons = ARGV
	ARGV.each do |icon_name|
		icon = svg.root.elements["//g[@inkscape:label='#{icon_name}']"]
		dir = "#{PREFIX}/#{icon.parent.attributes['inkscape:label']}"
		chopSVG({ :name => icon_name,
				:id => icon.attributes["id"],
				:dir => dir,
				:file => get_output_filename(dir, icon_name),
				:forcerender => true})
	end
	puts "\nrendered #{ARGV.length} icons"
end

#EOF
