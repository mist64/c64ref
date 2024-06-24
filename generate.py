#!/usr/bin/env python3

import os
import shutil
import subprocess
import fnmatch
import argparse
import re
from dataclasses import dataclass, field

GLOBAL_TITLE = "Ultimate Commodore 64 Reference"


### CONFIG Class

@dataclass
class BuildConfig():
	source_dir: str = "src" # where to look for files
	build_dir: str = "out" # where to put the output
	base_dir: str = "c64ref" # base directory

	server_path: str = "local@pagetable.com:/var/www/html/" # where to put the files so others can see

	deploy: bool = False # set via cli argument "upload": upload to server
	build_wips: bool = False # set via cli flag "--wip": helper for disabling unfinished categories
	enabled_paths: list = None # set via cli flag "--only": helper for building only selected categories

	git_has_changes: bool = True # set in setup
	git_branch_name: str = "main" # set in setup

	categories: list = None # set in setup


def parse_cli_into_config():

	# supported command line arguments
	parser = argparse.ArgumentParser(description=f"Generate the {GLOBAL_TITLE}")
	parser.add_argument("deploy_mode", choices=["upload", "local"], nargs='?', default="local",
						help="the deploy mode (default: %(default)s)")
	parser.add_argument("--wip", action='store_true',
						help="also build the categories marked as wips (ignored if uploading to main)")
	parser.add_argument("--only", nargs='+',
						help="building all following categories using their path (ignored if uploading to main)")

	# parsing command line arguments
	args = parser.parse_args()

	config = BuildConfig()
	config.deploy = args.deploy_mode == "upload"
	config.build_wips = args.wip
	if args.only:
		config.enabled_paths = args.only

	if config.deploy and config.enabled_paths:
		print("Uploading and building only a few categories at the same time is not supported.")
		exit()

	# get git status
	f = os.popen(f'git ls-files -m | wc -l')
	if int(f.read()) <= 0:
		config.git_has_changes = False

	git_branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip()
	config.git_branch_name = git_branch_name

	return config


### DATA Classses

# collected 'outside', header and build information for a category
@dataclass
class RefCategory():
	path: str # folder name
	long_title: str # title for the html title and the headline
	short_title: str # title for the menu item
	authors: list # authors and their urls
	is_wip: bool = False # is this still a work in progress?


### CATEGORIES/TOPICS/SUBDIRECTORIES

DEFAULT_AUTHOR = '<a href="http://www.pagetable.com/">Michael Steil</a>'

CATEGORIES = [
	RefCategory( '6502',
		'6502 Family CPU Reference', '6502',
		[DEFAULT_AUTHOR],
	),
	RefCategory( 'kernal',
		'C64 KERNAL API', 'KERNAL API',
		[DEFAULT_AUTHOR],
	),
	RefCategory('c64disasm',
		'C64 BASIC & KERNAL ROM Disassembly', 'ROM Disassembly',
		[DEFAULT_AUTHOR],
	),
	RefCategory('c64mem',
		'C64 Memory Map', 'Memory Map',
		[DEFAULT_AUTHOR],
	),
	RefCategory('c64io',
		'C64 I/O Map', 'I/O Map',
		[DEFAULT_AUTHOR],
		is_wip=True
	),
	RefCategory('charset',
		'Character Set · PETSCII · Keyboard', 'Charset · PETSCII · Keyboard',
		[DEFAULT_AUTHOR, "Lisa Brodner"],
	),
	RefCategory('colors',
		'C64 Colors', 'Colors',
		[DEFAULT_AUTHOR],
		is_wip=True
	),
]


### FUNCTIONS for things that are longer

def get_header_str(current_category, categories, source_path, base_path, git_has_changes):
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

	# > title
	nav_string = f'<div>{GLOBAL_TITLE}</div>\n'

	# > links for each topic
	for category in categories:
		if category == current_category:
			a_menu = f'<a class="active" href="#">{category.short_title}</a>'
		else:
			a_menu = f'<a href="/{base_path}/{category.path}/">{category.short_title}</a>'
		nav_string += f"      {a_menu}\n"

	# > link to pagetable
	a_home = f'<a class="home" href="https://www.pagetable.com/">pagetable.com</a>'
	nav_string += f"      {a_home}"

	# byline information

	# > git revision hash with marker if there are uncommitted changes
	revision = os.popen(f'git log -1 --pretty=format:%h {source_path}').read()
	# > add a + to mark that the working copy had changes at build time
	if git_has_changes:
		revision += "+"

	# > date of git commit
	date = os.popen(f'git log -1 --date=short --pretty=format:%cd {source_path}').read()

	authors = ', '.join(current_category.authors)
	revision_info = f'<a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>, rev {revision}, {date}'
	byline_string = f'by <em>{authors}.</em> [<small>{revision_info}</small>]'

	return f"""
  <header>
    <div id="cat">{octocat_string}
	</div>

    <nav class="topnav">
      {nav_string}
    </nav>

    <h1 id="headline">{current_category.long_title}</h1>
    <p id="byline">{byline_string}</p>
  </header>
  """


### PATH HELPER

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

config = parse_cli_into_config()

# filter categories with build settings
if config.enabled_paths:
	config.categories = [category for category in CATEGORIES if category.path in config.enabled_paths]
else:
	if not config.build_wips:
		config.categories = [category for category in CATEGORIES if not category.is_wip]
	else:
		 config.categories = CATEGORIES

print(f"  > branch '{config.git_branch_name}' ->  <{'> <'.join([category.path for category in config.categories])}>")

# if the current build should be uploaded: do some sanity checking
if config.deploy:

	if config.git_has_changes:
		print("Generating and upload failed:")
		print("There are uncommited changes in the working copy.")
		exit()

	# this test only makes sense, if the base dir is adjusted for branches
	# TODO: XXX adjust base dir for branches or take this out
	if config.git_branch_name == "main":
		config.build_wips = False # reset for uploading to main

		response = input("Deploy to production? [Y/N]: ").strip()
		if response.lower() != 'y':
			print("Exiting.")
			exit()

else:
	if config.git_branch_name != "main":
		config.base_dir = "test/" + config.git_branch_name + "/" + config.base_dir


# clean build directories
if os.path.exists(config.build_dir):
	shutil.rmtree(config.build_dir)

##
## GENERATE HTML in build_dir
##
print("*** Generating:")

# copy global resources:

build_path = ensured_path(config.build_dir, config.base_dir, is_dir=True)

# > write index.html for root directory redirect
default_category="c64disasm"
if not default_category in [category.path for category in config.categories]:
	default_category = config.categories[0].path

root_redirect=f'<meta http-equiv="refresh" content="0; URL=/{config.base_dir}/{default_category}/">'
root_path = os.path.join(build_path, "index.html")
with open(root_path, 'w', encoding='utf-8') as file:
	file.write(root_redirect)

# > stylesheet
shutil.copy(os.path.join(config.source_dir, "style.css"), build_path)
shutil.copy(os.path.join(config.source_dir, "commentaries.css"), build_path)
# > commentaries.js  - shared java script for the original commentary htmls
shutil.copy(os.path.join(config.source_dir, "commentaries.js"), build_path)

# > favicons TODO: XXX favicons


# for each category/subdirectory/topic:
#     generate title and header including navigation, title, github
#     run the out.sh to copy (and maybe generate) all needed resources
#     add title and header into the index.html
for category in config.categories:
	print(f"\t> {category.path}")

	source_path = os.path.join(config.source_dir, category.path)
	destination_path = ensured_path(build_path, category.path, is_dir=True)
	filename = os.path.join(destination_path, "index.html")

	# run python script to copy resources and generate index.html if needed
	subprocess.run(['sh', 'out.sh', "../../" + destination_path], cwd=source_path)

	# get 'original' index.html for current category:
	with open(filename, 'r', encoding='utf-8') as file:
		output_str = file.read()

	# modify the original index.html output
	# by replacing some strings with generated versions:
	# > adding the generated title instead of the local title
	pattern = r"<title>.*?</title>"
	replacement = f"<title>{category.short_title} | {GLOBAL_TITLE}</title>"
	output_str = re.sub(pattern, replacement, output_str, count=1)

	# > create the header information
	header_str = get_header_str(category, config.categories, source_path, config.base_dir, config.git_has_changes)
	# > adding the header at the top of the body
	old = r"<body>"
	replacement = f"<body>\n{header_str}"
	output_str = output_str.replace(old, replacement, 1)

	# write index.html back to build dir including the changes
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(output_str)

##
## DEPLOY
##
if config.deploy:
	print("*** Uploading")
	command = f"rsync -Pa {config.build_dir}/* {config.server_path}/"
	print("    " + command)
	ret = subprocess.run(command, check=True, text=True, shell=True)
else:
	port = "6464"
	url = f"http://localhost:{port}/{config.base_dir}"
	print(url)
	subprocess.run(f"open {url}", check=True, text=True, shell=True)



