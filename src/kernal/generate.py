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
print('<meta http-equiv="Content-type" content="text/html; charset=utf-8">')
print('<title>KERNAL API | Ultimate C64 Reference</title>')
print('')
print('<script>')
print('const pageConfiguration = {')
print('    storage_prefix: "com.pagetable.kernal.",')
print('    number_of_entries:' + str(len(filenames)) + ',')
print('    number_of_header_columns: 4,')
print('    has_decimal_column: true,')
print('    decimal_column: 3') # 0 1 2 3
print('};')
print('</script>')
print('<script src="../commentaries.js"></script>')
print('')

print('<link rel="stylesheet" href="../style.css">')
print('<link rel="stylesheet" href="../commentaries.css">')

print('<style>')

address_width=4
label_width=4
cat_width=4.6
decimal_width=5

widths=0
for css_name, width, offset in [
		("left_column",    address_width, 0),
		("label_column",   label_width,   1.6),
		("cat_column",     cat_width,     2),
		("decimal_column", decimal_width, 0.1)
	]:

	print(f'table.disassembly_table th.{css_name}' + '{')
	print(f'	left: {offset + widths}em;')
	print(f'	width: {width}em;')
	print(f'	min-width: {width}em;')
	print(f'	max-width: {width}em;')
	print( '}')
	print('')
	widths += width

print('</style>')
print('</head>')

print('<body>')
print('<main>')
print('<div>')

print('<b>This allows you to view different commentaries side-by-side. You can enable/disable individual columns:</b><br><br>')
print('<table class="checkbox_table">')
for i in range(0, len(filenames)):
	print('<tr><td><input type="checkbox" id="checkbox_' + str(i) + '" checked onclick="hideCol(' + str(i) + ', document.getElementById(\'checkbox_' + str(i) + '\').checked);"></td><td style="white-space: nowrap;"><b><a href="' + links[i] + '">' + names[i] + '</a></b></td><td>' + descriptions[i] + '</td></tr>')
print('</table>')

print('<p>')
print('<input type="checkbox" id="checkbox_decimal" name="checkbox_decimal" onclick="toggleDecimal(document.getElementById(\'checkbox_decimal\').checked);">')
print('<label for="checkbox_decimal">Show Decimal Address</label>')
print('<br>')
print('<button id="toggle_details_button" onclick="closeAll()">Hide All Details</button>')
print('</p>')

print('<div id="disassembly_container">')
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

print('</div>')

print('<footer>')
print('<h2>Footnotes</h2>')
print('<div>')
print('<p><sup>1)</sup> intended to be called from a cartridge ROM<br>')
print('<sup>2)</sup> intended to be called from a replacement IRQ handler</p>')
print('</div>')
print('</footer>')

print('</main>')
print('</body>')
print('</html>')
