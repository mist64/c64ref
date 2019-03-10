#!/usr/bin/python

import cgi, re, os

filenames = [ "c64rom_ms.txt;c64rom_cbm.txt", "c64rom_de.txt", "c64rom_en.txt", "c64rom_sc.txt", "c64rom_mm.txt" ]
descriptions = [ "<a href=\"http://www.pagetable.com/?p=793\">Microsoft BASIC</a>/<a href=\"https://github.com/mist64/cbmsrc\">Commodore KERNAL</a> Source", "<a href=\"http://www.pagetable.com/?p=718\">64 intern (Data Becker)</a>", "<a href=\"http://www.pagetable.com/?p=726\">Lee Davison</a>", "<a href=\"http://www.pagetable.com/?p=728\">Bob Sander-Cederlof (Apple II)</a>", "<a href=\"http://www.unusedino.de/ec64/technical/misc/c64/romlisting.html\">Marko M&auml;kel&auml;</a>" ]
asm_donor_index = 1
source_index = 0 # we treat the Microsoft source differently

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


print '<meta http-equiv="Content-type" content="text/html; charset=utf-8" />'
print '<style type="text/css">table{border-collapse:collapse;} tr {border: none;} td{border-right: solid 1px; border-left: solid 1px;} tr:nth-child(even) {background-color: #f0f0f0;} </style>'
print '<title>Comparative C64 ROM Disassembly Study Guide</title>'
print '<script language="javascript">'
print '    function hideCol(col, checked) {'
print '        var tbl = document.getElementById("disassembly_table");'
print '        for (var i = 0; i < tbl.rows.length; i++) {'
print '            tbl.rows[i].cells[col].style.display = checked ? "" : "none";'
print '        }'
print '    }'
print '</script>'



print '<h1>Comparative C64 ROM Disassembly Study Guide</h1>'
f = os.popen("git log -1 --pretty=format:%h .")
revision = f.read()
print '<p>revision ' + revision + '</p>'
print '<p>By <a href="http://www.pagetable.com/">Michael Steil</a>. See <a href="https://github.com/mist64/c64rom">github.com/mist64/c64rom</a> for information on how this was created and how to contribute.</p><hr>'

i = 1
for description in descriptions:
	print '<input type="checkbox" id="checkbox_' + str(i) + '" checked onclick="hideCol(' + str(i) + ', document.getElementById(\'checkbox_' + str(i) + '\').checked);" />' + description + '<br/>'
	i += 1
print '<hr>'

print '<table border="0" id="disassembly_table">'

print '<tr>'
print '<th>Disassembly</th>'
for i in range(0, files):
	print '<th>' + descriptions[i] + '</th>'

print '</tr>'

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

			if line.startswith('.'):
				address[i] = int(line[2:6], 16)
			if address[i] > asmaddress:
				break
			comment = line[32:]
			comment = cgi.escape(comment)

			hex_numbers = re.findall(r'\$[0-9A-F][0-9A-F][0-9A-F][0-9A-F]', comment)
			for hex_number in hex_numbers:
				if (hex_number[1] == 'A' or hex_number[1] == 'B' or hex_number[1] == 'E' or hex_number[1] == 'F'):
					comment = comment.replace(hex_number, "<a href=\"#" + hex_number[1:] + "\">" + hex_number + "</a>")

			if comment.startswith('***'):
				comment = '<h2>' + comment[3:] + '</h2>'
			elif comment.startswith('SUBTTL'):
				comment = '<h2>' + comment[6:] + '</h2>'
			elif comment.startswith('.LIB '):
				comment = '<h2>' + comment + '</h2>'
			else:
				scomment = comment.lstrip()

				if scomment.startswith(';'):
					comment = '<b>' + comment + '</b>'

				comment = comment.replace(' ', '&nbsp;')
				comment = '<tt>' + comment + '</tt><br/>'


			print comment
			linenumber[i] = linenumber[i] + 1
		print "</td>"
	
	print "</td>"
