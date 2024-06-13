#!/usr/bin/env python3

import os
import shutil
import subprocess
import fnmatch
import argparse
import re

from dataclasses import dataclass
from typing import NamedTuple
from bs4 import BeautifulSoup
from bs4.formatter import Formatter
from bs4.dammit import EntitySubstitution


GLOBAL_TITLE = "Ultimate Commodore 64 Reference"
GLOBAL_SHORT_TITLE = "Ultimate C64 Reference"



#
### CONFIG Class
#
@dataclass
class BuildConfig():
	source_dir: str = "src" # where to look for files
	build_dir: str = "out" # where to put the output
	build_dir_tmp: str = "out_unmodified" # where to put the debug output

	server: str = "www.pagetable.com/c64ref" # where to put the files so others can see

	deploy: bool = False # set via cli argument "upload": upload to server
	debug: bool = False # set via cli argument "debug": write debug information

	build_wips: bool = False # set via cli flag "--build_wips": helper for disabling unfinished categories
	fast_build: bool = False # set via cli flag "--fast_build": helper for disabling slow build steps

	git_has_changes: bool = True # set in setup
	git_branch_name: str = "main" # set in setup


def parse_cli_into_config():
	#
	# parsing command line arguments
	#
	parser = argparse.ArgumentParser(description=f"Generate the {GLOBAL_TITLE}")
	parser.add_argument("deploy_mode", choices=["upload", "local", "debug"], nargs='?', default="local",
						help="the deploy mode (default: %(default)s)")
	parser.add_argument("--wip", action='store_true',
						help="also build the categories marked as wips (ignored if uploading to main)")
	parser.add_argument("--fast", action='store_true',
						help="disables building steps marked with !fast_build (ignored if uploading)")
	args = parser.parse_args()

	# TODO: add options for local
	config = BuildConfig()
	config.deploy = args.deploy_mode == "upload"
	config.debug = args.deploy_mode == "debug"
	config.build_wips = args.wip
	config.fast_build = args.fast
	return config



### DATA Classses

#
# small helper for authors
#
class Author(NamedTuple):
	name: str # who?
	url: str # where to visit them?

#
# collected 'outside' and header and build info for a category
#
class RefCategory(NamedTuple):
	path: str # folder name
	long_title: str # title for the html title and the headline
	short_title: str # title for the menu item
	authors: list # authors and their urls
	generator_type: str = 'HTML' # does this need a python script?
	generator_name: str = 'index.html' # if so: what name?
	generator_patterns: list = [] # what other files do we need to work?
	enabled: bool = True # should this show up in the menu and be generated?

#
# used for the category for which the html is currently generated
#
@dataclass
class CurrentCategory:
	category: RefCategory # current category
	header_soup: BeautifulSoup # soup into which the header information is added
	source_path: str # where are the source files? (incl. category.path)
	dest_path: str # where should the build go? (incl. category.path)
	dest_path_tmp: str # where should the debug files go? (incl. category.path)



### CATEGORIES/TOPICS/SUBDIRECTORIES

CONFIG = parse_cli_into_config()


DEFAULT_AUTHOR = Author("Michael Steil", "http://www.pagetable.com/")


CATEGORIES = [
	RefCategory( '6502',
		'6502 Family CPU Reference', '6502',
		[DEFAULT_AUTHOR],
		generator_patterns=["cpu_*.txt", "*.js"]
	),
	RefCategory( 'kernal',
		'C64 KERNAL API', 'KERNAL API',
		[DEFAULT_AUTHOR],
		'SCRIPT', 'generate.py'
	),
	RefCategory('c64disasm',
		'C64 BASIC & KERNAL ROM Disassembly', 'ROM Disassembly',
		[DEFAULT_AUTHOR],
		'SCRIPT', 'combine.py',
		enabled=(not CONFIG.fast_build)
	),
	RefCategory('c64mem',
		'C64 Memory Map', 'Memory Map',
		[DEFAULT_AUTHOR],
		'SCRIPT', 'combine.py'
	),
	RefCategory('c64io',
		'C64 I/O Map', 'I/O Map',
		[DEFAULT_AUTHOR],
		'SCRIPT', 'combine.py',
		enabled=CONFIG.build_wips
	),
	RefCategory('charset',
		'Character Set · PETSCII · Keyboard', 'Charset · PETSCII · Keyboard',
		[DEFAULT_AUTHOR, Author("Lisa Brodner", None)],
		'SCRIPT',  'generate.py',
		generator_patterns=["*.js", "*.css", "bin/*.bin"]
	),
	RefCategory('colors',
		'C64 Colors', 'Colors',
		[DEFAULT_AUTHOR],
		generator_patterns=["*.js"],
		enabled=CONFIG.build_wips
	),
]



### HTML GLOBAL

#
# this is the basic outline of the index.html
# - just used for generating the header
#
BASIC_HTML = """
<!DOCTYPE html>
	<html lang="en-US">
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<title>Ultimate C64 Reference</title>
	</head>
<body>

<header>
<div id="cat"></div>
<nav class="topnav"></nav>

<h1 id="headline"></h1>
<p id="byline"></p>
</header>

<main>
</main>

</body>
</html>
"""



### FUNCTIONS for things that are longer

def add_github_corner(header_soup):

	#
	# add a "github corner" with a waving octocat to the top right
	# html source via: http://tholman.com/github-corners/
	#
	html_doc = """
<a href="https://github.com/mist64/c64ref" class="github-corner" aria-label="View source on GitHub">
  <svg width="80" height="80" viewBox="0 0 250 250" style="fill:var(--main-color); color:#fff; position: absolute; top: 0; border: 0; right: 0; clip-path: polygon(0 0, 100% 0, 100% 100%);" aria-hidden="true">
	<path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
	<path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
	<path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path>
  </svg>
</a>"""
	tag = header_soup.find(id="cat")
	tag_append_tag(tag, html_doc)


def add_navigation(cc):

	nav_tag = cc.header_soup.find('nav')

	#
	# title
	h1 = f'<h1>{GLOBAL_TITLE}</h1>'
	tag_append_tag(nav_tag, h1)

	#
	# links for each topic
	for category in CATEGORIES:
		if category.enabled:
			if category == cc.category:
				a_menu = f'<a class="active" href="#">{category.short_title}</a>'
			else:
				a_menu = f'<a href="/{category.path}/">{category.short_title}</a>'
			tag_append_tag(nav_tag, a_menu)

	#
	# link to pagetable
	a_home = f'<a class="home" href="https://www.pagetable.com/">pagetable.com</a>'
	tag_append_tag(nav_tag, a_home)


def add_byline_and_build_info(cc):

	#
	# git revision hash with marker if there are uncommited changes
	f = os.popen(f'git log -1 --pretty=format:%h {cc.source_path}')
	revision = f.read()
	if CONFIG.git_has_changes:
		revision += "+"

	#
	# date of that git commit
	f = os.popen(f'git log -1 --date=short --pretty=format:%cd {cc.source_path}')
	date = f.read()

	#
	# authors for the byline
	author_strings = []
	for author in cc.category.authors:
		if author.url:
			author_string = f'<a href="{author.url}">{author.name}</a>'
		else:
			author_string = f'{author.name}'
		author_strings.append(author_string)
	authors = ', '.join(author_strings)

	html_doc = f'by <em>{authors}.</em> [<small><a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>, rev {revision}, {date}</small>]'

	tag = cc.header_soup.find(id="byline")
	tag_append_tag(tag, html_doc)


def get_main_content_from_subdirectories(cc):

	#
	# get 'original' index.html for current category
	#
	# run python script to generate:
	if cc.category.generator_type == 'SCRIPT':
		result = subprocess.run(['python3', cc.category.generator_name], capture_output=True, text=True, cwd=cc.source_path)
		output_str = result.stdout
	#
	# or copy file directly:
	elif cc.category.generator_type == 'HTML':
		path = 	os.path.join(cc.source_path, cc.category.generator_name)
		with open(path, 'r') as file:
			output_str = file.read()
	#
	# or exit
	else:
		output_str = ""
		print("Missing generator.")
		exit()

	if CONFIG.debug:
		#
		# for debugging: write the original HTML to tmp
		#
		# -> in unmodified version (direct output)
		filename = os.path.join(cc.dest_path_tmp, "index_orig.html")
		with open(filename, 'w', encoding='utf-8') as file:
			file.write(output_str)
		#
		# -> and version that has been through beautiful soup
		#    for comparing possible changes made to the resulting files through bs4
		filename = os.path.join(cc.dest_path_tmp, "index_soup.html")
		src_soup = BeautifulSoup(output_str, 'html.parser')
		with open(filename, 'w', encoding='utf-8') as file:
			file.write(str(src_soup.decode(formatter=UnsortedAttributes())))

	return output_str



### RESOURCES

def copy_resources_to_build_dir(cc):

	#
	# make a list of all files in the directory of the current category
	# remove the category folder name prefix (eg. c64disasm) from the paths
	#
	all_files = []
	for root, dirs, files in os.walk(cc.source_path):
		for file in files:
			filename = os.path.join(root, file)
			filename = os.path.relpath(filename, cc.source_path)
			all_files.append(filename) # just the 'local' path

	#
	# make list of files matching the categories generator_patterns
	patterns = cc.category.generator_patterns
	if patterns:
		filtered_files = []
		for pattern in patterns:
			for filename in fnmatch.filter(all_files, pattern):
				filtered_files.append(filename)

		#
		# copy the matched files to the build folder
		for file_path in filtered_files:
			file_in = os.path.join(cc.source_path, file_path)
			file_out = ensured_path(cc.dest_path, file_path, is_dir=False) # ensure because file_path might contain directories
			shutil.copy(file_in, file_out)
		#
		# and track the unmatched files
		unmatched_files = [file for file in all_files if file not in filtered_files]

	else:
		unmatched_files = all_files


	if CONFIG.debug:
		#
		# for debugging:
		#     write a .txt containing a list of the unmatched files
		filename = os.path.join(cc.dest_path_tmp, "files_no_copy.txt")
		with open(filename, 'w', encoding='utf-8') as file:
			for unmatched_file in unmatched_files:
				# ignore .DS_Store and the index.html
				if unmatched_file != "index.html" and unmatched_file != ".DS_Store":
					file.write(f"{unmatched_file}\n")



### HELPER

def tag_append_tag(tag, string):
	new_tag = BeautifulSoup(string, 'html.parser')
	tag.append(new_tag)


def ensured_path(path, *paths, is_dir):
	result = os.path.join(path, *paths)

	dir_name = result
	if not is_dir:
		dir_name = os.path.dirname(result)

	if not os.path.exists(dir_name):
		os.makedirs(dir_name)

	return result



class UnsortedAttributes(Formatter):

	def __init__(
			self, language=Formatter.HTML, entity_substitution=EntitySubstitution.substitute_xml,
			void_element_close_prefix=None, cdata_containing_tags=None,
	):
		super().__init__()

	def attributes(self, tag):
		for k, v in tag.attrs.items():
			if k == 'open' or k == 'checked' or k == 'selected':
				if v:
					print(f"v: {v}")
				v = None
			yield k, v



##################### MAIN #####################

##
## SETUP
##
print("*** Setup")


#
# get git status
#
f = os.popen(f'git ls-files -m | wc -l')
if int(f.read()) <= 0:
	CONFIG.git_has_changes = False

branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip()
CONFIG.git_branch_name = branch_name

#
# if the current build should be uploaded: do some sanity checking
#
if CONFIG.deploy:

	if CONFIG.git_has_changes:
		print("Generating and upload failed:")
		print("There are uncommited changes in the working copy.")
		exit()

	CONFIG.fast_build = False # reset for uploading

	print(f"    branch '{CONFIG.git_branch_name}' ->  <{'> <'.join([category.path for category in CATEGORIES])}>")

	if branch_name == "main":
		CONFIG.build_wips = False # reset for uploading to main

		response = input("Deploy to production? [Y/N]: ").strip()
		if response.lower() != 'y':
			print("Exiting.")
			exit()

#
# clean and ensure build directories
#
if os.path.exists(CONFIG.build_dir):
	shutil.rmtree(CONFIG.build_dir)
if os.path.exists(CONFIG.build_dir_tmp):
	shutil.rmtree(CONFIG.build_dir_tmp)

ensured_path(CONFIG.build_dir, is_dir=True)
ensured_path(CONFIG.build_dir_tmp, is_dir=True)


##
## GENERATE HTML in build_dir
##
print("*** Generating")

#
# copy global resources: stylesheet
shutil.copy(os.path.join(CONFIG.source_dir, "style.css"), CONFIG.build_dir)

#
# for each category/subdirectory/topic:
#     generate title and header including navigation, title, github
#     get the script results or HTMLs from the subdirectories
#     and add the generated title and header into them
#     copy all necessary files
#     output the updated index.htmls
#
for category in CATEGORIES:
	if category.enabled:
		# ensuring category paths
		source_path = os.path.join(CONFIG.source_dir, category.path)
		dest_path = ensured_path(CONFIG.build_dir, category.path, is_dir=True)
		dest_path_tmp = ensured_path(CONFIG.build_dir_tmp, category.path, is_dir=True)

		#
		# create the header information
		header_soup = BeautifulSoup(BASIC_HTML, 'html.parser')
		cc = CurrentCategory(category, header_soup, source_path, dest_path, dest_path_tmp)
		#
		# main document headline in header
		tag = header_soup.find(id="headline")
		tag.string = category.long_title
		#
		add_github_corner(header_soup)
		add_navigation(cc)
		add_byline_and_build_info(cc)

		#
		# copy resources to the build directory using the generator_patterns
		copy_resources_to_build_dir(cc)

		# get the index.html data via script or copying
		output_str = get_main_content_from_subdirectories(cc)

		#
		# modify the generated/original output
		# by replacing some strings with generated versions
		#
		# adding the generated title instead of the local title
		pattern = r"<title>.*?</title>"
		replacement = f"<title>{category.short_title} | {GLOBAL_SHORT_TITLE}</title>"
		output_str = re.sub(pattern, replacement, output_str, count=1)
		#
		# adding the soup generated header at the placeholder
		tag = cc.header_soup.find("header")
		header_str = str(tag.decode(formatter=UnsortedAttributes()))
		#
		old = r"<body>"
		replacement = f"<body>\n{header_str}"
		output_str = output_str.replace(old, replacement, 1)


		#
		# write index.html to build dir
		filename = os.path.join(dest_path, "index.html")
		with open(filename, 'w', encoding='utf-8') as file:
			file.write(output_str)


##
## DEPLOY
##
if CONFIG.deploy:
	print("*** Uploading")

	print(">> !!!! >>Please check the rsync command and the server before actually trying to upload with this") # then delete
	exit()	# these two lines

	command = f"rsync -Pa {CONFIG.build_dir}/* local@{CONFIG.server}:/var/www/html/"
	print("    " + command)
	ret = subprocess.run(command, check=True, text=True, shell=True)
