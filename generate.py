#!/usr/bin/env python3

import os
import shutil
import subprocess
import fnmatch
import argparse

from dataclasses import dataclass
from typing import NamedTuple
from bs4 import BeautifulSoup


GLOBAL_TITLE = "Ultimate Commodore 64 Reference"
GLOBAL_SHORT_TITLE = "Ultimate C64 Reference"


### CONFIG

@dataclass
class BuildConfig():
	source_dir: str = "src"
	build_dir: str = "out"
	build_dir_tmp: str = "out_unmodified"

	server: str = "www.pagetable.com/c64ref"
	deploy: bool = False

	git_has_changes: bool = True
	git_branch_name: str = "main"

	fast_build: bool = False
	build_wips: bool = False


CONFIG = BuildConfig()
#CONFIG = BuildConfig(build_wips=True)
#CONFIG = BuildConfig(fast_build=True)


### CATEGORIES

class Author(NamedTuple):
	name: str
	url: str

DEFAULT_AUTHOR = Author("Michael Steil", "http://www.pagetable.com/")


class RefCategory(NamedTuple):
	path: str
	long_title: str
	short_title: str
	authors: list
	generator_type: str = 'HTML'
	generator_name: str = 'index.html'
	generator_patterns: list = []
	enabled: bool = True


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
		'Character Set · PETSCII · Keyboard', 'Charset Set · PETSCII · Keyboard',
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


@dataclass
class CurrentCategory:
	category: RefCategory
	soup: BeautifulSoup


### HTML GLOBALS

TARGET_HTML_NAME = "index.html"

BASIC_HTML = """
<!DOCTYPE html>
	<html lang="en-US">
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<title>Ultimate C64 Reference</title>
		<link rel="stylesheet" href="/style.css">
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




###

def generate_navigation(cc):
	soup = cc.soup
	active_category = cc.category

	nav_tag = soup.find('nav')

	h1 = soup.new_tag('h1')
	h1.string = GLOBAL_TITLE

	nav_tag.append(h1)

	for category in CATEGORIES:
		if category.enabled:
			href = f'/{category.path}/'
			a = soup.new_tag('a', href=href)
			a.string = category.short_title
			if category == active_category:
				a['href'] = '#'
				a['class'] = 'active'
			nav_tag.append(a)

	a_home = soup.new_tag('a', href='https://www.pagetable.com/')
	a_home.string = 'pagetable.com'
	a_home['class'] = 'home'
	nav_tag.append(a_home)

#def add_favicons(soup):
	# TODO: favicons
	#<link href="/favicon.ico" rel="icon" sizes="32x32">
	#<link href="/fav/icon.svg" rel="icon" type="image/svg+xml">
	#<link href="/fav/apple-touch-icon.png" rel="apple-touch-icon">


def add_category_build_info(cc):
	path = os.path.join(CONFIG.source_dir, cc.category.path)

	f = os.popen(f'git log -1 --pretty=format:%h {path}')
	revision = f.read()
	if CONFIG.git_has_changes:
		revision += "+"

	f = os.popen(f'git log -1 --date=short --pretty=format:%cd {path}')
	date = f.read()

	author_strings = []
	for author in cc.category.authors:
		if author.url:
			author_string = f'<a href="{author.url}">{author.name}</a>'
		else:
			author_string = f'{author.name}'
		author_strings.append(author_string)
	authors = ', '.join(author_strings)

	html_doc = f'by <em>{authors}.</em> [<small><a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>, rev {revision}, {date}</small>]'
	doc_soup = BeautifulSoup(html_doc, 'html.parser')

	tag = cc.soup.find(id="byline")
	tag.append(doc_soup)

def add_main(cc):
	soup = cc.soup
	category = cc.category

	dir = os.path.join(CONFIG.source_dir, category.path)
	filename = category.generator_name

	file_soup = BeautifulSoup("", 'html.parser')
	file_unmodified = ""
	if category.generator_type == 'SCRIPT':
		result = subprocess.run(['python3', filename], capture_output=True, text=True, cwd=dir)
		file_soup = BeautifulSoup(result.stdout, 'html.parser')
		file_unmodified = result.stdout

	elif category.generator_type == 'HTML':
		path = 	os.path.join(dir, filename)
		with open(path, 'r') as file:
			file_soup = BeautifulSoup(file, 'html.parser')
			file.seek(0)
			file_unmodified = file.read()

	else:
		print("Missing generator")

	# for debugging: write the original HTML to tmp
	dir_path = ensured_path(CONFIG.build_dir_tmp, category.path, is_dir=True)
	filename = os.path.join(dir_path, "index_soup.html")
	filename_unmodified = os.path.join(dir_path, "index_orig.html")

	with open(filename, 'w', encoding='utf-8') as file:
		file.write(str(file_soup.decode(formatter="html5")))

	with open(filename_unmodified, 'w', encoding='utf-8') as file:
		file.write(file_unmodified)

	# extracting the relevant infos from the generated HTMLs
	tag = soup.find("main")
	new_tag = file_soup.find("div", class_="content")
	tag.append(new_tag)

	# position in <head> tag at which to insert the additional files:
	tag = soup.find("link")

	for new_tag in file_soup.find_all('style'):
		tag.insert_after(new_tag)

	for new_tag in file_soup.find_all('script'):
		tag.insert_after(new_tag)

	for new_tag in file_soup.find_all('link'):
		tag.insert_after(new_tag)


### RESOURCES

def copy_resources_and_html(cc):
	category_path = cc.category.path

	source_path = os.path.join(CONFIG.source_dir, category_path)
	dest_path = ensured_path(CONFIG.build_dir, category_path, is_dir=True)

	# write index.html
	filename = os.path.join(dest_path, TARGET_HTML_NAME)
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(str(cc.soup.decode(formatter="html5")))

	# get files for generator_patterns and copy those
	patterns = cc.category.generator_patterns

	unfiltered_files = []
	leftover_files = unfiltered_files

	for root, dirs, files in os.walk(source_path):
		for file in files:
			filename = os.path.join(root, file)
			filename = os.path.relpath(filename, source_path)
			unfiltered_files.append(filename) # just the 'local' path

	if patterns:
		filtered_files = []
		for pattern in patterns:
			for filename in fnmatch.filter(unfiltered_files, pattern):
				filtered_files.append(filename)

		for file in filtered_files:
			file_in = os.path.join(source_path, file)
			file_out = ensured_path(dest_path, file, is_dir=False)
			shutil.copy2(file_in, file_out)

		leftover_files = [file for file in unfiltered_files if file not in filtered_files]

	# for debugging
	filename = ensured_path(CONFIG.build_dir_tmp, category_path, "files_no_copy.txt", is_dir=False)
	with open(filename, 'w', encoding='utf-8') as file:
		for leftover_file in leftover_files:
			if leftover_file != "index.html" and leftover_file != ".DS_Store":
				file.write(f"{leftover_file}\n")


### OCTOCAT

def add_github_corner(soup):
	# via: http://tholman.com/github-corners/
	html_doc = """
<a href="https://github.com/mist64/c64ref" class="github-corner" aria-label="View source on GitHub">
  <svg width="80" height="80" viewBox="0 0 250 250" style="fill:var(--main-color); color:#fff; position: absolute; top: 0; border: 0; right: 0; clip-path: polygon(0 0, 100% 0, 100% 100%);" aria-hidden="true">
    <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
    <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
    <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path>
  </svg>
</a>"""
	doc_soup = BeautifulSoup(html_doc, 'html.parser')
	tag = soup.find(id="cat")
	tag.append(doc_soup)


### HELPER

def ensured_path(path, *paths, is_dir):
	result = os.path.join(path, *paths)

	dir_name = result
	if not is_dir:
		dir_name = os.path.dirname(result)

	if not os.path.exists(dir_name):
		os.makedirs(dir_name)

	return result



### MAIN

##
## SETUP
##

#
# parsing command line arguments
#
parser = argparse.ArgumentParser(description=f"Generate the {GLOBAL_TITLE}")
parser.add_argument("deploy_mode", choices=["upload", "local"], nargs='?', default="local",
					help="the deploy mode (default: %(default)s)")
args = parser.parse_args()

# TODO: add options for local
CONFIG.deploy = args.deploy_mode == "upload"


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
		print("Generate and upload failed:")
		print("There are uncommited changes in the working copy.")
		exit()

	if branch_name == "main":
		print(f"{CONFIG.git_branch_name}:")
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

# copy global resources: stylesheet
shutil.copy(os.path.join(CONFIG.source_dir, "style.css"), CONFIG.build_dir)

#
# for each category/subdirectory/topic:
#     take the basic HTML, extract the relevant info from
#     the script results or HTMLs from the subdirectories
#     and add them into the basic HTML
#
# TODO: make it the other way around, let the scripts generate templates with placeholders for TITLE, NAV etc.
#
for category in CATEGORIES:
	if category.enabled:

		soup = BeautifulSoup(BASIC_HTML, 'html.parser')
		cc = CurrentCategory(category, soup)

		# html (tab/document) title
		tag = cc.soup.find("title")
		tag.string = f"{cc.category.short_title} | {GLOBAL_SHORT_TITLE}"

		# main document headline in header
		tag = cc.soup.find(id="headline")
		tag.string = cc.category.long_title

		generate_navigation(cc)
		# add_favicons(cc.soup) # TODO XXX
		add_category_build_info(cc)
		add_github_corner(cc.soup)


		add_main(cc)

		# write and copy to build directory
		copy_resources_and_html(cc)

##
## DEPLOY
##
if CONFIG.deploy:
	print("*** Uploading")
	command = f"rsync -Pa {CONFIG.build_dir}/* local@{CONFIG.server}:/var/www/html/"
	print("    " + command)
	ret = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
