#!/usr/bin/env python3

import os
import shutil
import subprocess
import fnmatch

from dataclasses import dataclass
from typing import NamedTuple
from bs4 import BeautifulSoup

REGULAR_BUILD=True
#REGULAR_BUILD=False #debug

GLOBAL_TITLE = "Ultimate Commodore 64 Reference"
GLOBAL_SHORT_TITLE = "Ultimate C64 Reference"

### CATEGORIES

class RefCategory(NamedTuple):
	path: str
	long_title: str
	short_title: str
	generator_type: str = 'HTML'
	generator_name: str = 'index.html'
	generator_patterns: list = []
	enabled: bool = True

CATEGORIES = [
	RefCategory('6502',      '6502 Family CPU Reference', '6502', generator_patterns=["cpu_*.txt", "*.js"]),
	RefCategory('kernal',    'C64 KERNAL API', 'KERNAL API', 'SCRIPT', 'generate.py'),
	RefCategory('c64disasm', 'C64 BASIC & KERNAL ROM Disassembly', 'ROM Disassembly', 'SCRIPT', 'combine.py', enabled=REGULAR_BUILD),
	RefCategory('c64mem',    'C64 Memory Map', 'Memory Map', 'SCRIPT', 'combine.py'),
	RefCategory('c64io',     'C64 I/O Map', 'I/O Map', 'SCRIPT', 'combine.py', enabled=False),
	RefCategory('charset',   'Character Set · PETSCII · Keyboard', 'Charset Set · PETSCII · Keyboard', 'SCRIPT',  'generate.py', generator_patterns=["*.js", "*.css", "bin/*.bin"]),
	RefCategory('colors',    'C64 Colors', 'Colors', generator_patterns=["*.js"], enabled=False),
]


@dataclass
class CurrentCategory:
	category: RefCategory
	soup: BeautifulSoup
	resources: set

### CONFIG

SOURCE_DIR = "Source"
BUILD_DIR = "out"


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



### MAIN METHOD

def generate_html(category, revision, date):
	html_doc = BASIC_HTML
	soup = BeautifulSoup(html_doc, 'html.parser')

	cc = CurrentCategory(category, soup, set())

	add_category_title(cc)
	# add_favicons(cc.soup)

	add_github_corner(cc.soup)

	generate_navigation(cc)
	add_category_headline(cc)
	add_category_build_info(cc, revision, date)

	add_main(cc)

	# write and copy to build directory
	copy_resources_and_html(cc)


### HELPER

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

def add_category_title(cc):
	tag = cc.soup.find("title")
	tag.string = f"{cc.category.short_title} | {GLOBAL_SHORT_TITLE}"

def add_category_headline(cc):
	tag = cc.soup.find(id="headline")
	tag.string = cc.category.long_title

def add_category_build_info(cc, revision, date):

	html_doc = f'by <i><a href="http://www.pagetable.com/">Michael Steil</a></i> [<small><a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>, Revision {revision}, {date}</small>]'
	doc_soup = BeautifulSoup(html_doc, 'html.parser')

	tag = cc.soup.find(id="byline")
	tag.append(doc_soup)

def add_main(cc):
	soup = cc.soup
	category = cc.category

	dir = os.path.join(SOURCE_DIR, category.path)
	filename = category.generator_name

	file_soup = BeautifulSoup("", 'html.parser')
	if category.generator_type == 'SCRIPT':
		result = subprocess.run(['python3', filename], capture_output=True, text=True, cwd=dir)
		file_soup = BeautifulSoup(result.stdout, 'html.parser')

	elif category.generator_type == 'HTML':
		path = 	os.path.join(dir, filename)
		with open(path, 'r') as file:
			file_soup = BeautifulSoup(file, 'html.parser')

	else:
		print("Missing generator")

	# extracting the relevant infos from the generated HTMLs
	tag = soup.find("main")
	new_tag = file_soup.find("div", class_="content")
	tag.append(new_tag)

	# position in <head> tag at which to insert the additional files:
	tag = soup.find("link")
	files = cc.resources

	for new_tag in file_soup.find_all('style'):
		tag.insert_after(new_tag)

	# check for tags that reference additional files

	for new_tag in file_soup.find_all('script'):
		tag.insert_after(new_tag)
		if new_tag.has_attr('src'):
			files.add(new_tag['src'])

	for new_tag in file_soup.find_all('link'):
		tag.insert_after(new_tag)
		if new_tag.has_attr('href'):
			files.add(new_tag['href'])

	for new_tag in file_soup.find_all('img'):
			tag.insert_after(new_tag)
			if new_tag.has_attr('src'):
				files.add(new_tag['src'])


### RESOURCES

def copy_resources_and_html(cc):
	category_path = cc.category.path
	files = cc.resources

	source_path = os.path.join(SOURCE_DIR, category_path)
	dest_path = os.path.join(BUILD_DIR, category_path)

	if not os.path.exists(dest_path):
		os.makedirs(dest_path)


# TODO: remove and make the needed things happen via pattern?
# 	# copy other resources:
# 	for file in cc.resources:
# 		file_in = os.path.join(source_path, file)
# 		file_out = os.path.join(dest_path, file)
#
# 		if not os.path.exists(file_out):
# 			print(f'{file_in} > {file_out}')
# 			shutil.copy2(file_in, file_out)
# 		else:
# 			print(f'{file_out} already exists')

	# write index.html
	filename = os.path.join(dest_path, TARGET_HTML_NAME)
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(str(cc.soup.decode(formatter="html5")))

	# get files for generator_patterns and copy those
	patterns = cc.category.generator_patterns
	if patterns:
		unfiltered_files = []
		for root, dirs, files in os.walk(source_path):
			for file in files:
				filename = os.path.join(root, file)
				filename = os.path.relpath(filename, source_path)
				unfiltered_files.append(filename) # just the 'local' path

		filtered_files = []
		for pattern in patterns:
			for filename in fnmatch.filter(unfiltered_files, pattern):
				filtered_files.append(filename)

		for file in filtered_files:
			file_in = os.path.join(source_path, file)
			file_out = os.path.join(dest_path, file)
			os.makedirs(os.path.dirname(file_out), exist_ok=True)
			shutil.copy2(file_in, file_out)

		# # for debugging
		# leftover_files = [file for file in unfiltered_files if file not in filtered_files]
		# print(f">>> : {source_path}")
		# for file in leftover_files:
		# 	print(file)
		# print("<<<")

def copy_global_resources():
	# copy globals: stylesheet
	shutil.copy(os.path.join(SOURCE_DIR, "style.css"), BUILD_DIR)



### OCTOCAT

# via: http://tholman.com/github-corners/
# TODO: put into an SVG file and the CSS file for everything (see files in colors/ and the global CSS)

def add_github_corner(soup):
	html_doc = """
<a href="https://github.com/mist64/c64ref" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:var(--main-color); color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a>"""
	doc_soup = BeautifulSoup(html_doc, 'html.parser')
	tag = soup.find(id="cat")
	tag.append(doc_soup)



### MAIN

def generate():
	if not os.path.exists(BUILD_DIR):
		os.makedirs(BUILD_DIR)

	copy_global_resources()

	f = os.popen('git log -1 --pretty=format:%h .')
	revision = f.read()

	f = os.popen('git log -1 --date=short --pretty=format:%cd .')
	date = f.read()

	for category in CATEGORIES:
		if category.enabled:
			generate_html(category, revision, date)


generate()
