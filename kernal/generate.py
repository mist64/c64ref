#!/usr/bin/python3

import markdown
import re

#lines = [line.rstrip() for line in open("kernal_prg.txt")]
lines = [line.rstrip() for line in open("kernal_128intern.txt")]

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

calls = []
names = []
for call_lines in calls_raw:
	title = call_lines[0]
	address = title[1:5]
	name = title[7:13].rstrip()
	summary = title[15:]
	call_lines_stripped = []
	for call_line in call_lines[1:]:
		call_lines_stripped.append(call_line[15:])
	calls.append((address, name, summary, call_lines_stripped))
	names.append(name)

print('<table border=1>')

for (address, name, summary, lines) in calls:
	print('<tr>')
	print('<td>$' + address + '</td>')
	print('<td><a name="' + name + '">' + name + '</td>')
	print('<td><details open><summary>' + summary + '</summary>')
	all_text = '\n'.join(lines)
	html = markdown.markdown(all_text, extensions=['tables' , 'sane_lists'])
	for replace_name in names:
		if replace_name != name:
			html = re.sub('\\b' + replace_name + '\\b', '<a href="#"' + replace_name + '">' + replace_name + '</a>', html)
	print(html + '</details></td>')



	print('</tr>')

print('</table>')
