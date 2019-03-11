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
print '<title>Comparative C64 ROM Disassembly Study Guide</title>'
print ''
print '<script language="javascript">'
print '    function hideCol(col, checked) {'
print '        var tbl = document.getElementById("disassembly_table");'
print '        for (var i = 0; i < tbl.rows.length; i++) {'
print '            tbl.rows[i].cells[col].style.display = checked ? "" : "none";'
print '        }'
print '    }'
print '</script>'
print ''
print '<style type="text/css">'
print ''
print 'table {'
print '  border-collapse: collapse;'
print '}'
print ''
print 'td, th {'
print '  margin: 0px;'
print '  padding: 2px 4px;'
print '  border: solid grey;'
print '  border-width:0px 1px 0px 1px;'
print '  text-align:left;'
print '  vertical-align: text-top;'
print '  font-family: monospace;'
print '}'
print ''
print 'h3 {'
print '  font-family: serif;'
print '}'
print ''
print '.com {'
print '  white-space: pre;'
print '}'
print ''
print 'th.com {'
print '  font-weight: bold;'
print '}'
print ''
print 'div {'
print '  padding: 1em;'
print '}'
print ''
#print '.sticky {'
#print '  position: -webkit-sticky;'
#print '  position: -moz-sticky;'
#print '  position: -ms-sticky;'
#print '  position: -o-sticky;'
#print '  position: sticky;'
#print '  outline: 1px solid green;'
#print '  outline-offset: -1px;'
#print '}'
print ''
print '.top_row {'
print '  top: 0em;'
print '  z-index: 10;'
#print '  background-color:yellow;'
print '  border-bottom: 1px solid grey;'
print '}'
print ''
print '.left_column {'
print '  left: 0em;'
print '  z-index: 11;'
#print '  background-color:red;'
print '}'
print ''
print '.top_left_corner {'
print '  top: 0em;'
print '  left: 0em;'
print '  z-index: 12;'
#print '  background-color:orange;'
print '  border-bottom: 1px solid grey;'
print '}'
print ''
print 'tr:nth-child(even) {'
print '  background: #f0f0f0;'
print '}'
print ''
print '</style>'


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

print '<div>'
print '<table id="disassembly_table">'

print '<tr>'
print '<th class="sticky top_left_corner">Disassembly</th>'
for i in range(0, files):
	print '<th class="sticky top_row">' + descriptions[i] + '</th>'
print '</tr>'

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

	hex_numbers = re.findall(r'\$[0-9A-F][0-9A-F][0-9A-F][0-9A-F]', asm)
	for hex_number in hex_numbers:
		if (hex_number[1] == 'A' or hex_number[1] == 'B' or hex_number[1] == 'E' or hex_number[1] == 'F'):
			asm = asm.replace(hex_number, "<a href=\"#" + hex_number[1:] + "\">" + hex_number + "</a>")

	print '<tr>'
	print '<th class="sticky left_column">'
	if has_address:
		print "<a name=\"" + hexaddress + "\"/>"
	print '<span class="com">' + asm + '</span></th>'

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
					comment = '<span class="com">' + comment + '</span><br />'

			print comment
			linenumber[i] = linenumber[i] + 1
		print "</td>"
	print "</tr>"

print '</table>'
print '</div>'
