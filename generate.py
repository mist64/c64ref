#!/usr/bin/env python3

import os
import shutil
from typing import NamedTuple
from bs4 import BeautifulSoup


GLOBAL_TITLE = "Ultimate Commodore 64 Reference"
GLOBAL_SHORT_TITLE = "Ultimate C64 Reference"

### CATEGORIES

class RefCategory(NamedTuple):
	path: str
	script_name: str
	long_title: str
	short_title: str

CATEGORIES = [
	RefCategory('6502',      'generate.py', '6502 Family CPU Reference', '6502'),
	RefCategory('kernal',    'generate.py', 'C64 KERNAL API', 'KERNAL API'),
	RefCategory('c64disasm', 'combine.py',  'C64 BASIC & KERNAL ROM Disassembly', 'ROM Disassembly'),
	RefCategory('c64mem',    'combine.py',  'C64 Memory Map', 'Memory Map'),
	RefCategory('c64io',     'combine.py',  'C64 I/O Map', 'I/O Map'),
	RefCategory('charset',   'generate.py', 'Character Set · PETSCII · Keyboard', 'Character Set · PETSCII · Keyboard'),
	RefCategory('colors',    'generate.py', 'C64 Colors', 'Colors'),
]


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
		<style id="cat_css"></style>
	</head>
<body>

<header>
<div id="cat"></div>
<nav class="topnav"></nav>

<h1 id="headline"></h1>
<p id="byline"></p>
</header>

<main class="main">
</main>

</body>
</html>
"""



### MAIN METHOD

def generate_html(category):
	html_doc = BASIC_HTML
	soup = BeautifulSoup(html_doc, 'html.parser')

	add_category_title(soup, category.short_title)
	# add_favicons(soup)

	add_github_corner(soup)

	generate_navigation(soup, category)
	add_category_headline(soup, category.long_title)
	add_category_build_info(soup, category)

	# write and copy to build directory
	copy_resources(BUILD_DIR)

	out_directory = os.path.join(BUILD_DIR, category.path)
	filename = os.path.join(out_directory, TARGET_HTML_NAME)
	if not os.path.exists(out_directory):
		os.makedirs(out_directory)

	with open(filename, 'w', encoding='utf-8') as file:
		file.write(str(soup.decode(formatter="html5")))


### HELPER

def generate_navigation(soup, active_category):
	nav_tag = soup.find('nav')

	h1 = soup.new_tag('h1')
	h1.string = GLOBAL_TITLE

	nav_tag.append(h1)

	for category in CATEGORIES:
		a = soup.new_tag('a', href=f'/{category.path}/')
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

def add_category_title(soup, title):
	tag = soup.find("title")
	tag.string = f"{title} | {GLOBAL_SHORT_TITLE}"

def add_category_headline(soup, title):
	tag = soup.find(id="headline")
	tag.string = title

def add_category_build_info(soup, category):
	#TODO: get revision and date
	revision = 'Revision 7bc6e79, 2024-06-05'
	html_doc = f'<i>by <a href="http://www.pagetable.com/">Michael Steil</a>, <a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>. {revision}</i>'
	doc_soup = BeautifulSoup(html_doc, 'html.parser')

	tag = soup.find(id="byline")
	tag.append(doc_soup)


### RESOURCES

def copy_resources(out_directory):
	if not os.path.exists(out_directory):
		os.makedirs(out_directory)

	# copy globals: stylesheet
	shutil.copy(os.path.join(SOURCE_DIR, "style.css"), out_directory)



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

for category in CATEGORIES:
  generate_html(category)
