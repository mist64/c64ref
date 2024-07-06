#!/usr/bin/env python3

import html, re, os

filenames = [
	"c64disasm_ms.txt;c64disasm_cbm.txt",
	"c64disasm_de.txt",
	"c64disasm_en.txt",
	"c64disasm_sc.txt",
	"c64disasm_mn.txt",
	"c64disasm_mm.txt"
]
names = [
	"Microsoft/Commodore Source",
	"Data Becker [German]",
	"Lee Davison",
	"Bob Sander-Cederlof [BASIC only]",
	"Magnus Nyman [KERNAL only]",
	"Marko M&auml;kel&auml;"
]
links = [
	"https://github.com/mist64/cbmsrc",
	"https://www.pagetable.com/?p=1015",
	"https://github.com/Project-64/reloaded/blob/master/c64/firmware/C64LD11.S",
	"https://www.pagetable.com/?p=728",
	"https://www.telecomm.at/documents/Jiffydos_Romlisting.doc",
	"https://github.com/Project-64/reloaded/blob/master/c64/C64DIS11.TXT"
]
descriptions = [
	"The original M6502 BASIC source by Microsoft (KIM-1 version, not everything lines up, Commodore extensions are missing, but lots of comments by the original authors)<br>and the original C64 KERNAL source by Commodore (lots of comments by the original authors)",
	"German-language comments from <i>Das neue Commodore-64-intern-Buch</i> by Data Becker, ISBN 3890113079. Some minor corrections have been made.",
	"Comments from <i>The almost completely commented C64 ROM disassembly V1.01</i> by Lee Davison. Some minor corrections have been made.",
	"Comments adapted from <i>S-C DocuMentor for Applesoft</i> by Bob Sander-Cederlof, for the version of Microsoft BASIC that shipped with the Apple II.",
	"Comments from <i>JIFFYDOS version 6.01/version 6.02</i> by Magnus Nyman (Harlekin/FairLight), which were written for the JiffyDOS KERNAL, so some serial code and all tape code is missing comments.",
	"Comments from the <i>Commodore 64 BASIC/KERNAL ROM Disassembly Version 1.0 (June 1994)</i> by Marko M&auml;kel&auml;."
]

def cross_reference(string, symbols):
	hex_numbers = list(set(re.findall(r'(?<!#)\$[0-9A-Fa-f][0-9A-Fa-f]+', string)))
	for hex_number in hex_numbers:
		dec_number = int(hex_number[1:], 16)
		if dec_number < 0x0400:
			string = string.replace(hex_number, "<a href=\"../c64mem/#" + '{:04X}'.format(dec_number) + "\">" + hex_number + "</a>")
		elif (dec_number >= 0xa000 and dec_number <= 0xbfff) or (dec_number >= 0xe000 and dec_number <= 0xffff):
			string = string.replace(hex_number, "<a href=\"#" + hex_number[1:] + "\">" + hex_number + "</a>")

	for symbol in symbols:
		string = re.sub('\\b' + symbol + '\\b', '<a href="../c64mem/#' + symbol + '">' + symbol + '</a>', string)

	return string

asm_donor_index = 1
source_index = 0 # we treat the Microsoft/Commodore source differently

symbols = []
symbol_lines = [line.rstrip() for line in open('../c64mem/c64mem_src.txt')]
for line in symbol_lines:
	if line.startswith('#') or line.startswith('-'):
		continue
	symbol = line[13:19].rstrip()
	if symbol != '':
		symbols.append(symbol)
symbols = set(symbols)

data = []
linenumber = []
address = []
for filename in filenames:
	d = []
	for f in filename.split(";"):
		d += [line.rstrip() for line in open(f)]
	data.append(d)
	linenumber.append(0)
	address.append(0)
files = len(filenames)

asmaddress = 0
asmlinenumber = 0

for i in range(0, files):
	while True:
		line = data[i][linenumber[i]]
		if len(line) > 0 and line[0] == '.':
			break
		linenumber[i] = linenumber[i] + 1


print('<!DOCTYPE html>')
print('<html lang="en-US">')
print('<head>')
print('<meta http-equiv="Content-type" content="text/html; charset=utf-8">')
print('<title>BASIC & KERNAL ROM Disassembly | Ultimate C64 Reference</title>')
print('')

print('<script>')
print('const pageConfiguration = {')
print('    storage_prefix: "com.pagetable.c64disasm.",')
print('    number_of_entries:' + str(len(filenames)) + ',')
print('    number_of_header_columns: 1,')
print('    has_decimal_column: false,')
print('    decimal_column: 2') # 0 1 2
print('};')
print('</script>')
print('<script src="../commentaries.js"></script>')
print('')

print('<link rel="stylesheet" href="../style.css">')
print('<link rel="stylesheet" href="../commentaries.css">')

print('<style>')
print('')
print('h3 {')
print('    font-family: serif;')
print('}')

print('.com {')
print('    white-space: pre;')
print('}')

print('table.disassembly_table td,')
print('table.disassembly_table th {')
print('    font-family: monospace;')
print('}')
print('')

for css_name, width, left in [("left_column", 18, 0)]:

	print(f'table.disassembly_table th.{css_name}' + '{')
	print(f'	left: {left}em;')
	print(f'	width: {width}em;')
	print(f'	min-width: {width}em;')
	print(f'	max-width: {width}em;')
	print( '}')
	print('')

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

print('<div class="disassembly_container">')
print('<table id="disassembly_table" class="disassembly_table">')

print('<tr>')
print('<th class="left_column">Disassembly</th>')
for i in range(0, files):
	print('<th class="top_row">' + names[i] + '</th>')
print('</tr>')

count = 0
while(True):
	count += 1
#	if count > 80:
#		break

	for i in range(0, files):
		if linenumber[i] >= len(data[i]):
			continue
		while len(data[i][linenumber[i]]) > 0 and (data[i][linenumber[i]][0] == '-' or data[i][linenumber[i]][0] == '#'):
			linenumber[i] = linenumber[i] + 1

	if asmlinenumber >= len(data[asm_donor_index]):
		break

	asm = data[asm_donor_index][asmlinenumber][0:32].rstrip()
	asmlinenumber = asmlinenumber + 1

	if len(asm) == 0:
		continue
	if asm[0] == '#' or asm[0] == '-':
		continue

	has_address = False
	if asm[0] == '.':
		hexaddress = asm[2:6]
		asmaddress = int(hexaddress, 16)
		has_address = True

	asm = cross_reference(asm, [])

	print('<tr>')
	print('<th class="left_column">')
	if has_address:
		print('<a id="' + hexaddress + '"></a>')
	print('<span class="com">' + asm + '</span></th>')

	for i in range(0, files):
		print('<td>')
		comments = []
		while True:
			if linenumber[i] >= len(data[i]):
				break

			line = data[i][linenumber[i]]

			if line.startswith('.'):
				address[i] = int(line[2:6], 16)
			if address[i] > asmaddress:
				break
			comment = line[32:]
			comment = html.escape(comment)

			comment = cross_reference(comment, symbols)

			if comment.startswith('***'):
				comment = '<h3>' + comment[3:] + '</h3>'
			elif comment.startswith('SUBTTL'):
				comment = '<h3>' + comment[6:] + '</h3>'
			elif comment.startswith('.LIB '):
				comment = '<h3>' + comment + '</h3>'
			else:
				scomment = comment.lstrip()

				if scomment.startswith(';'):
					comment = '<b>' + comment + '</b>'

				if len(comment) != 0:
					comment = '<span class="com">' + comment + '</span><br>'

			if len(comment) != 0:
				comments.append(comment)

			linenumber[i] = linenumber[i] + 1

		if len(comments):
			for comment in comments:
				print(comment)
		else:
			print('&nbsp;')

		print('</td>')
	print('</tr>')

print('</table>')
print('</div>')

print('</div>')
print('</main>')
print('</body>')
print('</html>')

