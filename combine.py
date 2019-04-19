#!/usr/bin/python

import cgi, re, os

filenames = [ "c64rom_ms.txt;c64rom_cbm.txt", "c64rom_de.txt", "c64rom_en.txt", "c64rom_sc.txt", "c64rom_mn.txt", "c64rom_mm.txt" ]
descriptions = [ "<a href=\"http://www.pagetable.com/?p=793\">Microsoft BASIC</a>/<a href=\"https://github.com/mist64/cbmsrc\">Commodore KERNAL</a> Source", "<a href=\"http://www.pagetable.com/?p=718\">64 intern (Data Becker)</a>", "<a href=\"http://www.pagetable.com/?p=726\">Lee Davison</a>", "<a href=\"http://www.pagetable.com/?p=728\">Bob Sander-Cederlof (Apple II)</a>", "<a href=\"https://www.telecomm.at/documents/Jiffydos_Romlisting.doc\">Magnus Nyman</a>", "<a href=\"http://www.unusedino.de/ec64/technical/misc/c64/romlisting.html\">Marko M&auml;kel&auml;</a>" ]
asm_donor_index = 1
source_index = 0 # we treat the Microsoft/Commodore source differently

f = os.popen("git log -1 --pretty=format:%h .")
revision = f.read()

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
print '<title>Commodore 64 BASIC & KERNAL ROM Disassembly</title>'
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
# http://tholman.com/github-corners/
print '<a href="https://github.com/mist64/c64rom" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:#004080; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>'
print '<style type="text/css">'
print ''
print 'body {'
print '    color: #004080;'
print '    font-family: Helvetica'
print '}'
print ''
print 'a {'
print '    color: #0060a0;'
print '}'
print ''
print 'table {'
print '    border-collapse: collapse;'
print '    color: black;'
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
print 'tr {'
print '  background: #f0f0f0;'
print '}'
print ''
print 'tr:nth-child(even) {'
print '  background: #ffffff;'
print '}'
print ''
print '</style>'
print '<body bgcolor="#e0f0ff">'

print '<h1>Commodore 64 BASIC & KERNAL ROM Disassembly</h1>'

print '<p><i>by <a href="http://www.pagetable.com/">Michael Steil</a>. See <a href="https://github.com/mist64/c64rom">github.com/mist64/c64rom</a> for information on how this was created and how to contribute. Revision ' + revision + '</i></p>'

print '<div style="border-style: solid; display: inline-block">'
print 'This allows you to view different commentaries side-by-side.<br/>You can enable/disable the display of individual ones:<br/><br/>'
i = 1
for description in descriptions:
	print '<input type="checkbox" id="checkbox_' + str(i) + '" checked onclick="hideCol(' + str(i) + ', document.getElementById(\'checkbox_' + str(i) + '\').checked);" />' + description + '<br/>'
	i += 1
print '</div>'

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
print '</body>'
