#!/usr/bin/env python3

import os
import shutil
import subprocess
import fnmatch
import argparse
import re
from dataclasses import dataclass
from typing import NamedTuple

GLOBAL_TITLE = "Ultimate Commodore 64 Reference"

### CONFIG Class

@dataclass
class BuildConfig():
	source_dir: str = "src" # where to look for files
	build_dir: str = "out" # where to put the output
	build_dir_tmp: str = "out_debug" # where to put the debug output
	base_dir: str = "c64ref"

	server_path: str = "local@pagetable.com:/var/www/html/" # where to put the files so others can see

	deploy: bool = False # set via cli argument "upload": upload to server
	debug: bool = False # set via cli argument "debug": write debug information

	build_wips: bool = False # set via cli flag "--build_wips": helper for disabling unfinished categories
	fast_build: bool = False # set via cli flag "--fast_build": helper for disabling slow build steps

	git_has_changes: bool = True # set in setup
	git_branch_name: str = "main" # set in setup


def parse_cli_into_config():

	# supported command line arguments
	parser = argparse.ArgumentParser(description=f"Generate the {GLOBAL_TITLE}")
	parser.add_argument("deploy_mode", choices=["upload", "local", "debug"], nargs='?', default="local",
						help="the deploy mode (default: %(default)s)")
	parser.add_argument("--wip", action='store_true',
						help="also build the categories marked as wips (ignored if uploading to main)")
	parser.add_argument("--fast", action='store_true',
						help="disables building steps marked with !fast_build (ignored if uploading)")

	# parsing command line arguments
	args = parser.parse_args()

	config = BuildConfig()
	config.deploy = args.deploy_mode == "upload"
	config.debug = args.deploy_mode == "debug"
	config.build_wips = args.wip
	config.fast_build = args.fast

	if config.deploy and config.fast_build:
		print("Uploading and building fast at the same time is not supported.")
		exit()

	return config


### DATA Classses

# collected 'outside' and header and build info for a category
class RefCategory(NamedTuple):
	path: str # folder name
	long_title: str # title for the html title and the headline
	short_title: str # title for the menu item
	authors: list # authors and their urls
	generator_type: str = 'HTML' # does this need a python script?
	generator_patterns: list = [] # what other files do we need to work?
	enabled: bool = True # should this show up in the menu and be generated?


### CATEGORIES/TOPICS/SUBDIRECTORIES

CONFIG = parse_cli_into_config()

DEFAULT_AUTHOR = '<a href="http://www.pagetable.com/">Michael Steil</a>'

CATEGORIES = [
	RefCategory( '6502',
		'6502 Family CPU Reference', '6502',
		[DEFAULT_AUTHOR],
		generator_patterns=["cpu_*.txt", "*.js"]
	),
	RefCategory( 'kernal',
		'C64 KERNAL API', 'KERNAL API',
		[DEFAULT_AUTHOR],
		'SCRIPT',
	),
	RefCategory('c64disasm',
		'C64 BASIC & KERNAL ROM Disassembly', 'ROM Disassembly',
		[DEFAULT_AUTHOR],
		'SCRIPT',
		enabled=(not CONFIG.fast_build)
	),
	RefCategory('c64mem',
		'C64 Memory Map', 'Memory Map',
		[DEFAULT_AUTHOR],
		'SCRIPT',
	),
	RefCategory('c64io',
		'C64 I/O Map', 'I/O Map',
		[DEFAULT_AUTHOR],
		'SCRIPT',
		enabled=CONFIG.build_wips
	),
	RefCategory('charset',
		'Character Set · PETSCII · Keyboard', 'Charset · PETSCII · Keyboard',
		[DEFAULT_AUTHOR, "Lisa Brodner"],
		'SCRIPT',
		generator_patterns=["*.js", "*.css", "bin/*.bin"]
	),
	RefCategory('colors',
		'C64 Colors', 'Colors',
		[DEFAULT_AUTHOR],
		generator_patterns=["*.js"],
		enabled=CONFIG.build_wips
	),
]


### FUNCTIONS for things that are longer

def get_header_str(current_category):

	# add a "github corner" with a waving octocat to the top right
	# html source via: http://tholman.com/github-corners/

	octocat_string = """
<a href="https://github.com/mist64/c64ref" class="github-corner" aria-label="View source on GitHub">
  <svg width="80" height="80" viewBox="0 0 250 250" style="fill:var(--main-color); color:#fff; position: absolute; top: 0; border: 0; right: 0; clip-path: polygon(0 0, 100% 0, 100% 100%);" aria-hidden="true">
	<path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
	<path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
	<path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path>
  </svg>
</a>"""

	# add nav tag containing all categories
	# with the current category marked as active

	# title
	nav_string = f'<h1>{GLOBAL_TITLE}</h1>\n'

	# links for each topic
	for category in CATEGORIES:
		if not category.enabled:
			continue

		if category == current_category:
			a_menu = f'<a class="active" href="#">{category.short_title}</a>'
		else:
			a_menu = f'<a href="/{CONFIG.base_dir}/{category.path}/">{category.short_title}</a>'
		nav_string += f"{a_menu}\n"

	# link to pagetable
	a_home = f'<a class="home" href="https://www.pagetable.com/">pagetable.com</a>'
	nav_string += f"{a_home}\n"

	# byline information

	source_path = source_path_for_category(current_category)
	# git revision hash with marker if there are uncommitted changes
	revision = os.popen(f'git log -1 --pretty=format:%h {source_path}').read()
	# add a + to mark that the working copy had changes at build time
	if CONFIG.git_has_changes:
		revision += "+"

	# date of git commit
	date = os.popen(f'git log -1 --date=short --pretty=format:%cd {source_path}').read()

	authors = ', '.join(current_category.authors)
	revision_info = f'<a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>, rev {revision}, {date}'
	byline_string = f'by <em>{authors}.</em> [<small>{revision_info}</small>]'

	return f"""
	<header>
	<div id="cat">{octocat_string}</div>
	<nav class="topnav">
	{nav_string}
	</nav>

	<h1 id="headline">{category.long_title}</h1>
	<p id="byline">{byline_string}</p>
	</header>
	"""


def get_main_content_from_subdirectories(current_category):

	source_path = source_path_for_category(current_category)

	# get 'original' index.html for current category:
	# run python script to generate:
	if current_category.generator_type == 'SCRIPT':
		result = subprocess.run(['python3', "generate.py"], capture_output=True, text=True, cwd=source_path)
		output_str = result.stdout

	# or copy file directly:
	elif current_category.generator_type == 'HTML':
		path = os.path.join(source_path, "index.html")
		with open(path, 'r') as file:
			output_str = file.read()

	return output_str


### RESOURCES

def copy_resources_to_build_dir(current_category):

	source_path = source_path_for_category(current_category)
	destination_path = destination_path_for_category(current_category)

	# make a list of all files in the directory of the current category
	# remove the category folder name prefix (eg. c64disasm) from the paths
	all_files = []
	for root, dirs, files in os.walk(source_path):
		for file in files:
			filename = os.path.join(root, file)
			filename = os.path.relpath(filename, source_path)
			all_files.append(filename) # just the 'local' path

	# make list of files matching the categories generator_patterns
	patterns = current_category.generator_patterns
	if patterns:
		filtered_files = []
		for pattern in patterns:
			for filename in fnmatch.filter(all_files, pattern):
				filtered_files.append(filename)

		# copy the matched files to the build folder
		for file_path in filtered_files:
			file_in = os.path.join(source_path, file_path)
			file_out = ensured_path(destination_path, file_path, is_dir=False) # ensure because file_path might contain directories
			shutil.copy(file_in, file_out)

		# and track the unmatched files
		unmatched_files = [file for file in all_files if file not in filtered_files]
	else:
		unmatched_files = all_files

	if CONFIG.debug:
		debug_path = debug_path_for_category(current_category)

		# write a .txt containing a list of the unmatched files
		filename = os.path.join(debug_path, "files_no_copy.txt")
		with open(filename, 'w', encoding='utf-8') as file:
			for unmatched_file in unmatched_files:
				# ignore .DS_Store and the index.html
				if unmatched_file != "index.html" and unmatched_file != ".DS_Store":
					file.write(f"{unmatched_file}\n")


### HELPER

def source_path_for_category(category):
	return os.path.join(CONFIG.source_dir, category.path)

def destination_path_for_category(category):
	return ensured_path(CONFIG.build_dir, CONFIG.base_dir, category.path, is_dir=True)

def debug_path_for_category(category):
	return ensured_path(CONFIG.build_dir_tmp, CONFIG.base_dir, category.path, is_dir=True)

def ensured_path(path, *paths, is_dir):
	result = os.path.join(path, *paths)

	dir_name = result
	if not is_dir:
		dir_name = os.path.dirname(result)
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)

	return result


##################### MAIN #####################

##
## SETUP
##
print("*** Setup")

# get git status
f = os.popen(f'git ls-files -m | wc -l')
if int(f.read()) <= 0:
	CONFIG.git_has_changes = False

git_branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip()
CONFIG.git_branch_name = git_branch_name

# if the current build should be uploaded: do some sanity checking
if CONFIG.deploy:

	if CONFIG.git_has_changes:
		print("Generating and upload failed:")
		print("There are uncommited changes in the working copy.")
		exit()

	CONFIG.fast_build = False # reset for uploading

	print(f"    branch '{CONFIG.git_branch_name}' ->  <{'> <'.join([category.path for category in CATEGORIES])}>")

	if git_branch_name == "main":
		CONFIG.build_wips = False # reset for uploading to main

		response = input("Deploy to production? [Y/N]: ").strip()
		if response.lower() != 'y':
			print("Exiting.")
			exit()


# clean and ensure build directories
if os.path.exists(CONFIG.build_dir):
	shutil.rmtree(CONFIG.build_dir)
if os.path.exists(CONFIG.build_dir_tmp):
	shutil.rmtree(CONFIG.build_dir_tmp)

##
## GENERATE HTML in build_dir
##
print("*** Generating")

# copy global resources: stylesheet
shutil.copy(os.path.join(CONFIG.source_dir, "style.css"),
			ensured_path(CONFIG.build_dir, CONFIG.base_dir, is_dir=True))

# for each category/subdirectory/topic:
#     generate title and header including navigation, title, github
#     get the script results or HTMLs from the subdirectories
#     and add the generated title and header into them
#     copy all necessary files
#     output the updated index.html
for category in CATEGORIES:
	if not category.enabled:
		continue

	# create the header information
	header_str = get_header_str(category)

	# copy resources to the build directory using the generator_patterns
	copy_resources_to_build_dir(category)

	# get the index.html data via script or copying
	output_str = get_main_content_from_subdirectories(category)

	# modify the generated/original output
	# by replacing some strings with generated versions

	# adding the generated title instead of the local title
	pattern = r"<title>.*?</title>"
	replacement = f"<title>{category.short_title} | {GLOBAL_TITLE}</title>"
	output_str = re.sub(pattern, replacement, output_str, count=1)

	# adding the header at the top of the body
	old = r"<body>"
	replacement = f"<body>\n{header_str}"
	output_str = output_str.replace(old, replacement, 1)

	# write index.html to build dir
	filename = os.path.join(destination_path_for_category(category), "index.html")
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(output_str)

##
## DEPLOY
##
if CONFIG.deploy:
	print("*** Uploading")
	command = f"rsync -Pa {CONFIG.build_dir}/* {CONFIG.server_path}/"
	print("    " + command)
	ret = subprocess.run(command, check=True, text=True, shell=True)
