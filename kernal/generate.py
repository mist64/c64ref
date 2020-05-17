#!/usr/bin/python3

import markdown
import re
import collections

filenames = [
	'kernal_prg.txt',
	'kernal_64intern.txt',
	'kernal_128intern.txt',
	'kernal_ct.txt',
	'kernal_dh.txt',
	'kernal_fk.txt',
	'kernal_ld.txt',
	'kernal_mapc64.txt',
	'kernal_mlr.txt',
	'kernal_pm.txt',
	'kernal_sta.txt',
]

sources = []
names = set()
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
		name = title[7:13].rstrip()
		summary = title[15:]
		call_lines_stripped = []
		for call_line in call_lines[1:]:
			call_lines_stripped.append(call_line[15:])
		calls[address] = (name, summary, call_lines_stripped)
		names.add(name)

	sources.append(calls)

print('<table border=1>')

all_addresses = []
for calls in sources:
	all_addresses.extend(calls.keys())
all_addresses = list(set(all_addresses))
all_addresses.sort()

symbols = {}
for calls in sources:
	for address in calls.keys():
		(name, _, _) = calls[address]
		if name == '':
			continue
		if address in symbols:
			symbols[address].append(name)
		else:
			symbols[address] = [name]
#print(symbols)
for address in symbols.keys():
	ctr = collections.Counter(symbols[address])
	symbols[address] = ctr

for address in all_addresses:
	print('<tr>')
	print('<td>${:02X}</td>'.format(address))
	if address in symbols:
		(name, _) = symbols[address].most_common(1)[0]
	else:
		name = ''
	print('<td><a name="' + name + '">' + name + '</td>')
	for call in sources:
		if address in call:
			(name, summary, lines) = call[address]
			print('<td><details open><summary>' + summary + '</summary>')
			all_text = '\n'.join(lines)
			html = markdown.markdown(all_text, extensions=['tables' , 'sane_lists'])
			#for replace_name in names:
			#	if replace_name != name:
			#		html = re.sub('\\b' + replace_name + '\\b', '<a href="#"' + replace_name + '">' + replace_name + '</a>', html)
			print(html + '</details></td>')
		else:
			print('<td></td>')
	print('</tr>')

print('</table>')
