#!/usr/bin/python3

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

links = [ '', '', '', '', '', '', '', '', '', '', '']
names = filenames #[ '', '', '', '', '', '', '', '', '', '', '']
descriptions = [ '', '', '', '', '', '', '', '', '', '', '']

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
			call_lines_stripped.append(call_line[15:])
		calls[address] = (symbol, summary, call_lines_stripped)

	sources.append(calls)

print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<html>')
print('<head>')
print('<title>KERNAL API | Ultimate C64 Reference</title>')
print('')
print('<script language="javascript">')
print('    window.onload = init;')
print('    function init() {')
print('        var tbl = document.getElementById("disassembly_table");')
print('        for (var i = 0; i < ' + str(len(filenames)) + '; i++) {')
print('            var key = "com.pagetable.c64mem.column_" + i;')
print('            var element_name = "checkbox_" + i;')
print('            var checked = localStorage.getItem(key) != "hidden";')
print('            document.getElementById(element_name).checked = checked;')
print('            hideCol(i, checked);')
print('        }')
print('        var key = "com.pagetable.c64mem.column_decimal";')
print('        var element_name = "checkbox_decimal";')
print('        var visible = localStorage.getItem(key) == "visible";')
print('        document.getElementById(element_name).checked = visible;')
print('        toggleDecimal(visible);')
print('    }')
print('    function toggleDecimal(visible) {')
print('        var tbl = document.getElementById("disassembly_table");')
print('        for (var i = 0; i < tbl.rows.length; i++) {')
print('            tbl.rows[i].cells[2].style.display = visible ? "" : "none";')
print('        }')
print('        var key = "com.pagetable.c64mem.column_decimal";')
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
print('            tbl.rows[i].cells[col+3].style.display = checked ? "" : "none";') # data columns start at index 3
print('        }')
print('        var key = "com.pagetable.c64mem.column_" + col;')
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

address_width=6.4
label_width=4
decimal_width=5

print('<style type="text/css">')
print('')
print('div.disassembly_container_with_dec {')
print('    padding: 1em 0em 1em ' + str(address_width + label_width + decimal_width + 1.6) + 'em;')
print('    overflow: scroll;')
print('}')
print('')
print('div.disassembly_container_no_dec {')
print('    padding: 1em 0em 1em ' + str(address_width + label_width + 0.9) + 'em;')
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
print('    left: ' + str(address_width + 3) + 'em;')
print('    z-index: 12;')
print('    font-family: monospace;')
print('    text-align: center;')
print('    color: yellow;')
print('}')
print('')
print('table.disassembly_table th.decimal_column {')
print('    width: ' + str(decimal_width) + 'em;')
print('    left: ' + str(address_width + label_width + 1.2) + 'em;')
print('    z-index: 13;')
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
print('<a href="https://github.com/mist64/c64ref" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:var(--main-color); color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>')

print('<div class="topnav">')
print('    <h1>Ultimate Commodore 64 Reference</h1> ')
print('    <a class="active" href="../kernal/">KERNAL API</a>')
print('    <a href="../c64disasm/">ROM Disassembly</a>')
print('    <a href="../c64mem/">Memory Map</a>')
#print('    <a href="#">I/O Map</a><!-- c64io/ -->')
#print('    <a href="#">6502 CPU</a><!-- 6502/ -->')
print('</div>')

print('<div class="body">')
print('<h1>C64 KERNAL API</h1>')

print('<p><i>by <a href="http://www.pagetable.com/">Michael Steil</a>, <a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>. Revision ' + revision + ', ' + date + '</i></p>')

print('<b>This allows you to view different commentaries side-by-side. You can enable/disable individual columns:</b><br/><br/>')
print('<table class="checkbox_table">')
for i in range(0, len(filenames)):
	print('<tr><td><input type="checkbox" id="checkbox_' + str(i) + '" checked onclick="hideCol(' + str(i) + ', document.getElementById(\'checkbox_' + str(i) + '\').checked);" /></td><td style="white-space: nowrap;"><b><a href="' + links[i] + '">' + names[i] + '</a></b><td>' + descriptions[i] + '</td></tr>')
print('</table>')

print('<p>')
print('<input type="checkbox" id="checkbox_decimal" name="checkbox_decimal" onclick="toggleDecimal(document.getElementById(\'checkbox_decimal\').checked);">')
print('<label for="checkbox_decimal">Show Decimal Address</label></input>')
print('<br />')
print('<button id="toggle_details_button" onclick="closeAll()">Hide All Details</button>')
print('</p>')

print('<div class="disassembly_container_no_dec" id="disassembly_container">')
print('<table id="disassembly_table" class="disassembly_table">')

print('<tr>')
print('<th class="left_column">Address</th>')
print('<th class="label_column">Symbol</th>')
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

	print('<tr>')
	anchor = '<a name="{:04X}"/>'.format(address)
	hex_address = '${:04X}'.format(address)
	print('<th class="left_column"> ' + anchor + hex_address + ' </th>')
	if address in symbols:
		(symbol, _) = symbols[address].most_common(1)[0]
	else:
		symbol = ''
	anchor = '<a name="{}"/>'.format(symbol)
	print('<th class="label_column"> ' + anchor + symbol + ' <a name="' + symbol + '"/> </th>')
	print('<th class="decimal_column"> {} </th>'.format(address))
	for call in sources:
		if address in call:
			(symbol, summary, lines) = call[address]
			print('<td><details open><summary>' + summary + '</summary>')
			all_text = '\n'.join(lines)
			html = markdown.markdown(all_text, extensions=['tables' , 'sane_lists'])
			for replace_symbol in all_symbols:
				if replace_symbol != symbol:
					html = re.sub('\\b' + replace_symbol + '\\b', '<a href="#' + replace_symbol + '">' + replace_symbol + '</a>', html)
			print(html + '</details></td>')
		else:
			print('<td></td>')
	print('</tr>')

print('</table>')
print('</div>')
print('</div>')
print('</body>')
print('</html>')
