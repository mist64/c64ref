#!/usr/bin/python

import cgi, re

filenames = [ "c64rom_ms.txt", "c64rom_de.txt", "c64rom_en.txt", "c64rom_sc.txt" ]
asm_donor_index = 1

data = []
linenumber = []
address = []
for filename in filenames:
	data.append([line.rstrip() for line in open(filename)])
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


print '<meta http-equiv="Content-type" content="text/html; charset=utf-8" />'
print '<style type="text/css">table{border-collapse:collapse;} tr {border: none;} td{border-right: solid 1px; border-left: solid 1px;} tr:nth-child(even) {background-color: #f0f0f0;} </style>'
print '<table border="0">'

while(True):
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

	asm = asm.replace(' ', '&nbsp;')

	hex_numbers = re.findall(r'\$[0-9A-F][0-9A-F][0-9A-F][0-9A-F]', asm)
	for hex_number in hex_numbers:
		if (hex_number[1] == 'A' or hex_number[1] == 'B' or hex_number[1] == 'E' or hex_number[1] == 'F'):
			asm = asm.replace(hex_number, "<a href=\"#" + hex_number[1:] + "\">" + hex_number + "</a>")

	print '<tr valign="top">'
	print '<td>'
	if has_address:
		print "<a name=\"" + hexaddress + "\"/>"
	print '<tt><b>' + asm + '</b></tt></td>'
	

	for i in range(0, files):
		print '<td>'
		while True:
			if linenumber[i] >= len(data[i]):
				break

			line = data[i][linenumber[i]]

			if len(line) > 0 and line[0] == '.':
				address[i] = int(line[2:6], 16)
			if address[i] > asmaddress:
				break
			comment = line[32:]
			comment = cgi.escape(comment)

			hex_numbers = re.findall(r'\$[0-9A-F][0-9A-F][0-9A-F][0-9A-F]', comment)
			for hex_number in hex_numbers:
				if (hex_number[1] == 'A' or hex_number[1] == 'B' or hex_number[1] == 'E' or hex_number[1] == 'F'):
					comment = comment.replace(hex_number, "<a href=\"#" + hex_number[1:] + "\">" + hex_number + "</a>")

			index = comment.find(';')
			if index >= 0:
				if not (len(comment) >= 9 and comment[0:9] == '        ;'):
					comment_left = comment[:index]
					comment_right = comment[index:]
					comment_left = comment_left.replace(' ', '&nbsp;')
					comment = comment_left + comment_right
			elif not (len(comment) >= 6 and comment[0:6] == 'SUBTTL'):
				comment = comment.replace(' ', '&nbsp;')

			if len(comment) >= 3 and comment[0:3] == '***':
				comment = '<h2>' + comment[3:] + '</h2>'
			elif len(comment) >= 6 and comment[0:6] == 'SUBTTL':
				comment = '<h2>' + comment[6:] + '</h2>'
			elif len(comment) >= 1 and comment[0] == ';':
				comment = '<tt><b>' + comment + '</b></tt><br/>'
			elif len(comment) >= 9 and comment[0:9] == '        ;':
				comment = '<tt><b>' + comment + '</b></tt><br/>'
			else:
				comment = '<tt>' + comment + '</tt><br/>'
			print comment
			linenumber[i] = linenumber[i] + 1
		print "</td>"
	
	print "</td>"
