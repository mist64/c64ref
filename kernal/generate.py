#!/usr/bin/env python3

import markdown
import re
import collections
import os

filenames = [
	'kernal_prg.txt',
	'kernal_dh.txt',
	'kernal_mlr.txt',
	'kernal_mapc64.txt',
	'kernal_128intern.txt',
	'kernal_ld.txt',
	'kernal_pm.txt',
	'kernal_ct.txt',
	'kernal_sta.txt',
	'kernal_fk.txt',
	'kernal_64intern.txt',
]

names = [
	'Programmer\'s Reference Guide',
	'Tool Kit',
	'Machine Language Routines',
	'Mapping the Commodore 64',
	'Commodore 128 intern [German]',
	'Lee Davison',
	'Cracking The Kernal',
	'Craig Taylor',
	'Joe Forster/STA',
	'Frank Kontros',
	'64 intern [German]',
]

links = [
	'https://github.com/Project-64/reloaded/blob/master/c64/c64prg/C64PRG11.TXT',
	'https://archive.org/details/COMPUTEs_VIC-20_and_Commodore_64_Tool_Kit_Kernal_1985_COMPUTE_Publications_a',
	'https://archive.org/details/Compute_s_Machine_Language_Routines_for_the_Commodore_64_and_128',
	'https://github.com/Project-64/reloaded/blob/master/c64/mapc64/MAPC6412.TXT',
	'https://www.retrozone.ch/docs/c128/Commodore128Intern.pdf',
	'https://github.com/Project-64/reloaded/blob/master/c64/firmware/C64LD11.S',
	'https://www.atarimagazines.com/compute/issue40/cracking_the_kernal.php',
	'http://csbruce.com/cbm/hacking/hacking03.txt',
	'https://sta.c64.org/cbm64krnfunc.html',
	'http://www.zimmers.net/anonftp/pub/cbm/c64/programming/documents/c64-kernal.txt',
	'https://www.pagetable.com/?p=1015',
]

descriptions = [
	'<i>Commodore 64 Programmer\'s Reference Guide</i>, ISBN 0-672-22056-3',
	'<i>COMPUTE!\'s VIC-20 and Commodore 64 Tool Kit: Kernal</i> by Dan Heeb, ISBN 0942386337',
	'<i>Machine Language Routines for the Commodore 64 and 128</i> by Todd D Heimarck and Patrick Parrish, ISBN 0874550858',
	'<i>Mapping the Commodore 64</i> by Sheldon Leemon, ISBN 0-942386-23-X',
	'<i>Commodore 128 intern</i> by Jörg Schieb, Frank Thrun and Heinz Wrobel, ISBN 3-89011-098-3',
	'<i>The almost completely commented C64 ROM disassembly</i> by Lee Davison',
	'<i>Cracking The Kernal</i> by Peter Marcotty in COMPUTE! #40, September 1983, pp. 268-274',
	'<i>Kernal 64 / 128</i> by Craig Taylor in C= Hacking, Volume 1, Issue 3; July 15, 1992',
	'<i>Commodore 64 standard KERNAL functions</i> by Joe Forster/STA',
	'<i>C64 KERNAL jump table</i> by Frank Kontros',
	'<i>Das neue Commodore-64-intern-Buch</i> by Baloui, Brückmann, Englisch, Felt, Gelfand, Gerits and Krsnik, ISBN 3890113079',
]

categories = {
	0xFF81: 'EDITOR',
	0xFF84: 'SYS',
	0xFF87: 'MEM',
	0xFF8A: 'SYS',
	0xFF8D: 'SYS',
	0xFF90: 'IO',
	0xFF93: 'IEEE',
	0xFF96: 'IEEE',
	0xFF99: 'MEM',
	0xFF9C: 'MEM',
	0xFF9F: 'KBD',
	0xFFA2: 'IEEE',
	0xFFA5: 'IEEE',
	0xFFA8: 'IEEE',
	0xFFAB: 'IEEE',
	0xFFAE: 'IEEE',
	0xFFB1: 'IEEE',
	0xFFB4: 'IEEE',
	0xFFB7: 'IO',
	0xFFBA: 'IO',
	0xFFBD: 'IO',
	0xFFC0: 'IO',
	0xFFC3: 'IO',
	0xFFC6: 'IO',
	0xFFC9: 'IO',
	0xFFCC: 'IO',
	0xFFCF: 'IO',
	0xFFD2: 'IO',
	0xFFD5: 'IO',
	0xFFD8: 'IO',
	0xFFDB: 'TIME',
	0xFFDE: 'TIME',
	0xFFE1: 'KBD',
	0xFFE4: 'KBD',
	0xFFE7: 'IO',
	0xFFEA: 'TIME',
	0xFFED: 'EDITOR',
	0xFFF0: 'EDITOR',
	0xFFF3: 'MEM',
}

# APIs that are intended to be called from a cartridge
rom_calls = [
	0xFF81,
	0xFF84,
	0xFF87,
]

# APIs that are intended to be called from a replacement IRQ handler
irq_calls = [
	0xFF9F,
	0xFFEA,
]

def cross_reference(string):
	hex_numbers = list(set(re.findall(r'\$[0-9A-F][0-9A-F][0-9A-F][0-9A-F]', string)))
	for hex_number in hex_numbers:
		dec_number = int(hex_number[1:], 16)
		if dec_number < 0x0400:
			if dec_number < 0x100:
				formatted_hex_number = '${:02X}'.format(dec_number)
			else:
				formatted_hex_number = '${:04X}'.format(dec_number)
			string = string.replace(hex_number, '<a href="../c64mem/#' + '{:04X}'.format(dec_number) + '">' + formatted_hex_number + '</a>')
		elif (dec_number >= 0xa000 and dec_number <= 0xbfff) or (dec_number >= 0xe000 and dec_number <= 0xffff):
			string = string.replace(hex_number, '<a href="../c64disasm/#' + '{:04X}'.format(dec_number) + '">' + hex_number + '</a>')
	return string

def smart_join(lines):
	s = ''
	while len(lines) > 0:
		if s == '':
			s = lines[0]
		elif s[-1] == '-':
			if len(lines[0]) > 0 and lines[0][0].islower():
				s = s[:-1] + lines[0]
			else:
				s += lines[0]
		else:
			s += '\n' + lines[0]
		lines = lines[1:]
	return s

files = len(filenames)

f = os.popen('git log -1 --pretty=format:%h .')
revision = f.read()
f = os.popen('git log -1 --date=short --pretty=format:%cd .')
date = f.read()

sources = []
for filename in filenames:
	lines = [line.rstrip() for line in open(filename)]

	calls_raw = []
	call_lines = None
	for line in lines:
		if line.startswith('#') or line.startswith('-'):
			continue
		if line.startswith('$'):
			if call_lines is not None:
				calls_raw.append(call_lines)
			call_lines = []

		if call_lines is not None:
			call_lines.append(line)
	calls_raw.append(call_lines)

	calls = {}
	for call_lines in calls_raw:
		title = call_lines[0]
		address = int(title[1:5], 16)
		symbol = title[7:13].rstrip()
		summary = title[15:]
		call_lines_stripped = []
		for call_line in call_lines[1:]:
			call_lines_stripped.append(call_line[15:].rstrip())
		while len(call_lines_stripped) > 0 and call_lines_stripped[0] == '':
			call_lines_stripped = call_lines_stripped[1:]
		while len(call_lines_stripped) > 0 and call_lines_stripped[-1] == '':
			call_lines_stripped = call_lines_stripped[:-1]
		calls[address] = (symbol, summary, call_lines_stripped)

	sources.append(calls)

print('<!DOCTYPE html>')
print('<html lang="en-US">')
print('<head>')
print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<title>KERNAL API | Ultimate C64 Reference</title>')
print('')
print('<script>')
print('    window.onload = init;')
print('    function init() {')
print('        var tbl = document.getElementById("disassembly_table");')
print('        for (var i = 0; i < ' + str(len(filenames)) + '; i++) {')
print('            var key = "com.pagetable.kernal.column_" + i;')
print('            var element_name = "checkbox_" + i;')
print('            var checked = localStorage.getItem(key) != "hidden";')
print('            document.getElementById(element_name).checked = checked;')
print('            hideCol(i, checked);')
print('        }')
print('        var key = "com.pagetable.kernal.column_decimal";')
print('        var element_name = "checkbox_decimal";')
print('        var visible = localStorage.getItem(key) == "visible";')
print('        document.getElementById(element_name).checked = visible;')
print('        toggleDecimal(visible);')
print('    }')
print('    function toggleDecimal(visible) {')
print('        var tbl = document.getElementById("disassembly_table");')
print('        for (var i = 0; i < tbl.rows.length; i++) {')
print('            tbl.rows[i].cells[3].style.display = visible ? "" : "none";')
print('        }')
print('        var key = "com.pagetable.kernal.column_decimal";')
print('        var cnt = document.getElementById("disassembly_container");')
print('        if (visible) {')
print('            cnt.className = "disassembly_container_with_dec";')
print('            localStorage.setItem(key, "visible");')
print('        } else {')
print('            cnt.className = "disassembly_container_no_dec";')
print('            localStorage.removeItem(key);')
print('        }')
print('    }')
print('    function hideCol(col, checked) {')
print('        var tbl = document.getElementById("disassembly_table");')
print('        for (var i = 0; i < tbl.rows.length; i++) {')
print('            tbl.rows[i].cells[col+4].style.display = checked ? "" : "none";') # data columns start at index 4
print('        }')
print('        var key = "com.pagetable.kernal.column_" + col;')
print('        if (checked) {')
print('            localStorage.removeItem(key);')
print('        } else {')
print('            localStorage.setItem(key, "hidden");')
print('        }')
print('    }')
print('    function openAll() {')
print('        var elems = document.getElementsByTagName("details");')
print('        document.getElementById("toggle_details_button").innerHTML = "Hide All Details";')
print('        document.getElementById("toggle_details_button").setAttribute("onClick", "javascript: closeAll();");')
print('')
print('        for (let item of elems) {')
print('            item.setAttribute("open", true);')
print('        }')
print('    }')
print('')
print('    function closeAll() {   ')
print('        var elems = document.getElementsByTagName("details");')
print('        document.getElementById("toggle_details_button").setAttribute("onClick", "javascript: openAll();" );')
print('        document.getElementById("toggle_details_button").innerHTML = "Expand All Details";    ')
print('        ')
print('        for (let item of elems) {')
print('           item.removeAttribute("open");')
print('        }')
print('    }')
print('</script>')
print('')

print('<link rel="stylesheet" href="../style.css">')

address_width=4
label_width=4
cat_width=4.6
decimal_width=5

print('<style>')
print('')
print('div.disassembly_container_with_dec {')
print('    padding: 1em 0em 1em ' + str(address_width + label_width + cat_width + decimal_width + 2) + 'em;')
print('    overflow: scroll;')
print('}')
print('')
print('div.disassembly_container_no_dec {')
print('    padding: 1em 0em 1em ' + str(address_width + label_width + cat_width + 1.1) + 'em;')
print('    overflow: scroll;')
print('}')
print('')
print('table.disassembly_table>tbody>tr>td, table.disassembly_table>tbody>tr>th.top_row {')
print('    min-width: 30em;')
print('    max-width: 40em;')
print('}')
print('')
print('table.disassembly_table th.left_column {')
print('    width: '+ str(address_width) +'em;')
print('}')
print('')
print('table.disassembly_table th.label_column {')
print('    width: ' + str(label_width) +'em;')
print('    left: ' + str(address_width + 2.6) + 'em;')
print('    z-index: 12;')
print('    font-family: monospace;')
print('    text-align: center;')
print('    color: yellow;')
print('}')
print('')
print('table.disassembly_table tr:nth-of-type(1) th:nth-child(1 of .cat_column) {')
print('    color: var(--main-background);')
print('}')
print('')
print('table.disassembly_table th.cat_column {')
print('    width: ' + str(cat_width) + 'em;')
print('    left: ' + str(address_width + label_width + 3.4) + 'em;')
print('    z-index: 13;')
print('    font-size: smaller;')
print('    text-align: center;')
print('    color: var(--main-color);')
print('}')
print('')
print('table.disassembly_table th.decimal_column {')
print('    width: ' + str(decimal_width) + 'em;')
print('    left: ' + str(address_width + label_width + cat_width + 1.6) + 'em;')
print('    z-index: 14;')
print('}')
print('')
print('details {')
print('    font-family: serif;')
print('}')
print('summary {')
print('    font-family: Helvetica;')
print('}')
print('')
print('</style>')
print('</head>')
print('<body>')

# http://tholman.com/github-corners/
print('<a href="https://github.com/mist64/c64ref" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:var(--main-color); color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a>')

print('<div class="topnav">')
print('    <h1>Ultimate Commodore 64 Reference</h1> ')
print('    <a href="../6502/">6502</a>')
print('    <a class="active" href="#">KERNAL API</a>')
print('    <a href="../c64disasm/">ROM Disassembly</a>')
print('    <a href="../c64mem/">Memory Map</a>')
print('    <a href="../charset/">Charset · PETSCII · Keyboard</a>')
#print('    <a href="../c64io/">I/O Map</a>')
print('    <a class="home" href="https://www.pagetable.com/">pagetable.com</a>')
print('</div>')

print('<div class="main">')
print('<h1>C64 KERNAL API</h1>')

print('<p><i>by <a href="http://www.pagetable.com/">Michael Steil</a>, <a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>. Revision ' + revision + ', ' + date + '</i></p>')

print('<b>This allows you to view different commentaries side-by-side. You can enable/disable individual columns:</b><br/><br/>')
print('<table class="checkbox_table">')
for i in range(0, len(filenames)):
	print('<tr><td><input type="checkbox" id="checkbox_' + str(i) + '" checked onclick="hideCol(' + str(i) + ', document.getElementById(\'checkbox_' + str(i) + '\').checked);" /></td><td style="white-space: nowrap;"><b><a href="' + links[i] + '">' + names[i] + '</a></b><td>' + descriptions[i] + '</td></tr>')
print('</table>')

print('<p>')
print('<input type="checkbox" id="checkbox_decimal" name="checkbox_decimal" onclick="toggleDecimal(document.getElementById(\'checkbox_decimal\').checked);" />')
print('<label for="checkbox_decimal">Show Decimal Address</label>')
print('<br />')
print('<button id="toggle_details_button" onclick="closeAll()">Hide All Details</button>')
print('</p>')

print('<div class="disassembly_container_no_dec" id="disassembly_container">')
print('<table id="disassembly_table" class="disassembly_table">')

print('<tr>')
print('<th class="left_column">Address</th>')
print('<th class="label_column">Symbol</th>')
print('<th class="cat_column">Category</th>')
print('<th class="decimal_column">Decimal</th>')
for i in range(0, files):
	print('<th class="top_row">' + names[i] + '</th>')
print('</tr>')


all_addresses = []
for calls in sources:
	all_addresses.extend(calls.keys())
all_addresses = list(set(all_addresses))
all_addresses.sort()

symbols = {}
all_symbols = []
for calls in sources:
	for address in calls.keys():
		(symbol, _, _) = calls[address]
		if symbol == '':
			continue
		all_symbols.append(symbol)
		if address in symbols:
			symbols[address].append(symbol)
		else:
			symbols[address] = [symbol]

all_symbols = set(all_symbols)

for address in symbols.keys():
	ctr = collections.Counter(symbols[address])
	symbols[address] = ctr

for address in all_addresses:
	if address < 0xff81:
		continue

	if address in symbols:
		(symbol, _) = symbols[address].most_common(1)[0]
	else:
		symbol = ''

	border_color = '--cat-color-' + categories[address].lower();
	print('<tr>')
	anchor = '<a id="{:04X}"></a>'.format(address)
	anchor += '<a id="{}"></a>'.format(symbol)
	hex_address = '${:04X}'.format(address)
	print('<th class="left_column"> ' + anchor + hex_address + '</th>')
	print('<th class="label_column"> ' + symbol + '</th>')
	category = categories[address]
	if address in rom_calls:
		category += '<sup>1)</sup>'
	if address in irq_calls:
		category += '<sup>2)</sup>'
	print('<th class="cat_column" style="background-color: var(' + border_color + ');"> {} </th>'.format(category))
	print('<th class="decimal_column"> {} </th>'.format(address))
	for call in sources:
		if address in call:
			print('<td>')
			(symbol, summary, lines) = call[address]

			is_collapsible = len(lines) > 0

			if is_collapsible:
				print('<details open><summary>')
				if summary == '':
					summary = '…'
			print('<b>' + summary + '</b>')
			if is_collapsible:
				print('</summary>')

			all_text = smart_join(lines)
			html = markdown.markdown(all_text, extensions=['tables' , 'sane_lists'])
			for replace_symbol in all_symbols:
				if replace_symbol != symbol:
					html = re.sub('\\b' + replace_symbol + '\\b', '<a href="#' + replace_symbol + '">' + replace_symbol + '</a>', html)
			html = cross_reference(html)
			print(html)
			if is_collapsible:
				print('</details>')
			print('</td>')
		else:
			print('<td></td>')
	print('</tr>')

print('</table>')
print('</div>')
print('<p><sup>1)</sup> intended to be called from a cartridge ROM<br/>')
print('<sup>2)</sup> intended to be called from a replacement IRQ handler</p>')
print('</div>')
print('</body>')
print('</html>')
