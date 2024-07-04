#!/usr/bin/env python3

import re, os
import pprint
import markdown

filenames = [
	'c64mem_mapc64.txt',
	'c64mem_64er.txt',
	'c64mem_64intern.txt',
	'c64mem_sta.txt',
	'c64mem_src.txt',
	'c64mem_prg.txt',
	'c64mem_64map.txt',
	'c64mem_jb.txt',
]
names = [
	'Mapping the Commodore 64',
	'64\'er [German]',
	'64 intern [German]',
	'Joe Forster/STA',
	'Microsoft/Commodore Source',
	'Programmer\'s Reference Guide',
	'64map',
	'Jim Butterfield',
]
links = [
	'https://github.com/Project-64/reloaded/blob/master/c64/mapc64/MAPC6412.TXT',
	'https://archive.org/details/64er_sonderheft_1986_07/page/n6/mode/2up',
	'https://www.pagetable.com/?p=1015',
	'http://www.awsm.de/mem64/',
	'https://github.com/mist64/cbmsrc',
	'https://github.com/Project-64/reloaded/blob/master/c64/c64prg/C64PRG11.TXT',
	'https://github.com/Project-64/reloaded/blob/master/c64/64MAP11.TXT',
	'https://www.atarimagazines.com/compute/issue29/394_1_COMMODORE_64_MEMORY_MAP.php',
]
descriptions = [
	'Reference from <i>Mapping the Commodore 64</i> by Sheldon Leemon, ISBN 0-942386-23-X.',
	'German-language reference from <i>Memory Map mit Wandervorschl&auml;gen</i> by Dr. H. Hauck, in 64\'er Sonderheft 1986/07.',
	'German-language reference from <i>Das neue Commodore-64-intern-Buch</i> by Data Becker, ISBN 3890113079.',
	'Reference by Joe Forster/STA, with awsm\'s changes applied.',
	'Comments from the original M6502 BASIC source by Microsoft and the original C64 KERNAL source by Commodore',
	'Reference from <i>Commodore 64 Programmer\'s Reference Guide</i>.',
	'Reference as found in "Commodore_64_Memory_Maps.txt" by anonymous.',
	'Reference by Jim Butterfield in COMPUTE! #29 (October 1982).',
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
			string = string.replace(hex_number, '<a href="#' + '{:04X}'.format(dec_number) + '">' + formatted_hex_number + '</a>')
		elif (dec_number >= 0xa000 and dec_number <= 0xbfff) or (dec_number >= 0xe000 and dec_number <= 0xffff):
			string = string.replace(hex_number, '<a href="../c64disasm/#' + '{:04X}'.format(dec_number) + '">' + hex_number + '</a>')
	return string


data = []
linenumber = []
address = []
for filename in filenames:
	d = []
	for f in filename.split(';'):
		d += [line.rstrip() for line in open(f)]
	data.append(d)
	linenumber.append(0)
	address.append(0)
files = len(filenames)

for i in range(0, files):
	while True:
		line = data[i][linenumber[i]]
		if len(line) > 0 and line[0] == '$':
			break
		linenumber[i] = linenumber[i] + 1

print('<!DOCTYPE html>')
print('<html lang="en-US">')
print('<head>')
print('<meta http-equiv="Content-type" content="text/html; charset=utf-8">')
print('<title>Memory Map | Ultimate C64 Reference</title>')
print('')

print('<script>')
print('const pageConfiguration = {')
print('    storage_prefix: "com.pagetable.c64mem.",')
print('    number_of_entries:' + str(len(filenames)) + ',')
print('    number_of_header_columns: 3,')
print('    has_decimal_column: true,')
print('    decimal_column: 2')
print('};')
print('</script>')
print('<script src="../commentaries.js"></script>')
print('')

print('<link rel="stylesheet" href="../style.css">')
print('<link rel="stylesheet" href="../commentaries.css">')

print('<style>')

address_width=6.4
label_width=4
decimal_width=5

widths=0
for css_name, width, offset in [
		("left_column",    address_width, 0),
		("label_column",   label_width,   2.1),
		("decimal_column", decimal_width, 0.3)
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
print('<th class="decimal_column">Decimal</th>')
for i in range(0, files):
	print('<th class="top_row">' + names[i] + '</th>')
print('</tr>')

count = 0
last_address1 = None
last_address2 = None
while(True):
	count += 1
#	if count > 80:
#		break

	#  make linenumber[] point to next line for all files
	for i in range(0, files):
		if linenumber[i] >= len(data[i]):
			continue
		while len(data[i][linenumber[i]]) > 0 and (data[i][linenumber[i]][0] == '-' or data[i][linenumber[i]][0] == '#'):
			linenumber[i] = linenumber[i] + 1

	list_address1 = []
	list_address2 = []
	list_symbol = []
	for i in range(0, files):
		if linenumber[i] >= len(data[i]):
			continue
		line = data[i][linenumber[i]]
		address1 = line[1:5]
		address1 = int(address1, 16)
		address2 = line[7:11]
		if len(address2.rstrip()) != 0:
			address2 = int(address2, 16)
		else:
			address2 = None
		symbol = line[13:19].rstrip()
		list_address1.append(address1)
		list_address2.append(address2)
		list_symbol.append(symbol)

	# reached end of all files?
	if len(list_address1) == 0:
		break

	# the next address is the lowest one from all source
	address1 = min(list_address1)

	# the longest range wins
	address2 = None
	symbol = None
	good_symbols = []
	for i in range(0, len(list_address1)):
		if list_address1[i] == address1 and (address2 == None or (list_address2[i] != None and list_address2[i] > address2)):
				address2 = list_address2[i]

	# get symbols of longest range
	for i in range(0, len(list_address1)):
		if list_address1[i] == address1 and list_address2[i] == address2 and list_symbol[i] != '':
			good_symbols.append(list_symbol[i])
	#print('xxx', address1, address2, good_symbols)

	if len(good_symbols) != 0:
		symbol = good_symbols[0]
	else:
		symbol = ''

	print('<tr>')

	# print address
	anchors = ''
	if address2 is not None:
		r = range(address1, address2 + 1)
	else:
		r = range(address1, address1 + 1)
	for address in r:
		anchors += '<a id="{:04X}"></a>'.format(address)
	if address1 == last_address1 and address2 == last_address2:
		print('<th class="left_column empty"> ' + anchors + ' </th>')
	else:
		hex_range = '${:04X}'.format(address1)
		if address2 != None:
			hex_range += '-${:04X}'.format(address2)
		print('<th class="left_column"> ' + anchors + hex_range + ' </th>')

	# print symbol
	if len(symbol) == 0:
		print('<th class="label_column empty"> </th>')
	else:
		print('<th class="label_column">' + symbol + ' <a id="' + symbol + '"></a></th>')

	# print decimal
	if address1 == last_address1 and address2 == last_address2:
		print('<th class="decimal_column empty"> </th>')
	else:
		dec_range = str(address1)
		if address2 != None:
			dec_range += '-' + str(address2)
		print('<th class="decimal_column"> ' + dec_range + ' </th>')

	last_address1 = address1
	last_address2 = address2

	for i in range(0, files):
		print('<td>')
		headings = []
		comments = []
		has_seen_blank_line = False
		is_first_line = True
		while True:
			if linenumber[i] >= len(data[i]):
				break

			line = data[i][linenumber[i]]

			if line.startswith('$'):
				if not is_first_line:
					# next address; stop here
					break

				# compare whether this address matches
				cmp_address1 = line[1:5]
				cmp_address1 = int(cmp_address1, 16)
				cmp_address2 = line[7:11]
				if len(cmp_address2.rstrip()) != 0:
					cmp_address2 = int(cmp_address2, 16)
				else:
					cmp_address2 = None
				cmp_symbol = line[13:19].rstrip()
				if cmp_address1 != address1 or cmp_address2 != address2 or (cmp_symbol != symbol and cmp_symbol != ''):
					break

			is_first_line = False
			comment = line[21:]
#			print(comment)

			if not has_seen_blank_line:
				if len(comment.lstrip()) == 0:
					has_seen_blank_line = True
				else:
					headings.append(comment)
			else:
				scomment = comment.lstrip()
				comment = comment + '\n'
				comments.append(comment)

			linenumber[i] += 1

		while len(comments) > 0 and comments[-1] == '\n':
			comments = comments[0:-1]

		#print('xxx',headings,comments)

		is_collapsible = len(comments) and not (len(comments) == 1 and comments[0].isspace())
		if is_collapsible:
			print('<details open>')

		if len(headings) or is_collapsible:
			all_text = ''
			if is_collapsible:
				print('<summary>')
				print('<b>')
				if not len(headings):
					print('…')
			else:
				print('<b>')

			previous_heading = ''
			for heading in headings:
				if previous_heading.endswith('.'):
					heading = '<br>' + heading
				html_heading = markdown.markdown(heading)
				html_heading.replace('<p>', '')
				html_heading.replace('</p>', '')
				all_text += heading + ' '
				previous_heading = heading
			all_text = cross_reference(all_text)
			print(all_text)
			print('</b>')
			if is_collapsible:
				print('</summary>')
		else:
			print('&nbsp;')

		if len(comments):
			all_text = ''
			for comment in comments:
				all_text += comment
			all_text = markdown.markdown(all_text, extensions=['tables', 'sane_lists'])
			all_text = cross_reference(all_text)
			print(all_text)
		else:
			print('&nbsp;')

		if is_collapsible:
			print('</details>')

		print('</td>')
	print('</tr>')

print('</table>')
print('</div>')

print('</div>')
print('</main>')
print('</body>')
print('</html>')
