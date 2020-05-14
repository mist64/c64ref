#!/usr/bin/python3

import markdown
import re

lines = [line.rstrip() for line in open("kernal.md")]

calls_raw = []
call_lines = None
for line in lines:
	if line.startswith('# '):
		if call_lines is not None:
			calls_raw.append(call_lines)
		call_lines = []

	call_lines.append(line)

calls = []
names = []
for call_lines in calls_raw:
	title = call_lines[0]
	address = title[3:7]
	rest = title[9:].split(' - ')
	name = rest[0]
	summary = rest[1]
	calls.append((address, name, summary, call_lines[1:]))
	names.append(name)

names.sort(reverse = True)
print(names)

print('<table border=1>')

for (address, name, summary, lines) in calls:
	print('<tr>')
	print('<td>' + address + '</td>')
	print('<td><a name="' + name + '">' + name + '</td>')
	print('<td><details open><summary>' + summary + '</summary>')
	all_text = '\n'.join(lines)
	html = markdown.markdown(all_text, extensions=['tables' , 'sane_lists'])
	for replace_name in names:
		if replace_name != name:
			html = re.sub('\\b' + 'KERNAL' + '\\b', '<a href="#"' + replace_name + '">' + replace_name + '</a>', html)
	print(html + '</details></td>')



	print('</tr>')

print('</table>')
