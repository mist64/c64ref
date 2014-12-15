#!/usr/bin/python
#
# txt2html.py - converts a "c64rom" commented disassembly txt file
# into cross-referenced HTML.
#
# Michael Steil
# https://github.com/mist64/c64rom
#
import sys, re, cgi, os

if len(sys.argv) < 2:
	print"Usage: " + sys.argv[0] + " <filename>"
	sys.exit(1)

filename = sys.argv[1]

lines = [line.rstrip() for line in open(filename)]

print "<meta http-equiv=\"Content-type\" content=\"text/html; charset=utf-8\" />"

print "<h1>" + lines[0][2:] + "</h1>"

f = os.popen("git log -1 --pretty=format:%h " + filename)
revision = f.read()
print "revision " + revision

print "<pre>"

previous_line = ''
previous_line_was_heading = False;
cached_header = ''

for line in lines[1:]:
	if len(line) != 0 and line[0] == '#':
		continue

	if len(line) != 0 and line[0] == '-':
		if len(line) > 1 and line[1] == '-':
			print "<hr/>"
		else:
			comment = cgi.escape(line[1:])
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', comment)
			for url in urls:
				comment = comment.replace(url, "<a href=\"" + url + "\">" + url + "</a>")
			print comment
		continue

	left = line[:32]
	right = cgi.escape(line[32:])
	
	if left.rstrip() == '' and (previous_line == '' or previous_line_was_heading):
		if cached_header == '':
			cached_header = right
		else:
			cached_header = cached_header + " " + right
		previous_line_was_heading = True
		continue

	previous_line_was_heading = False
	
	address = line[2:6]
	if len(address) and address != '    ':
		sys.stdout.write("<a name=\"" + address + "\"/>")

	if cached_header != '':
		print "</pre><h2>" + cgi.escape(cached_header) + "</h2><pre>"
		cached_header = ''

	hex_numbers = re.findall(r'\$[0-9A-F][0-9A-F][0-9A-F][0-9A-F]', line)
	for hex_number in hex_numbers:
		if (hex_number[1] == 'A' or hex_number[1] == 'B' or hex_number[1] == 'E' or hex_number[1] == 'F'):
			line = line.replace(hex_number, "<a href=\"#" + hex_number[1:] + "\">" + hex_number + "</a>")
	print line
	previous_line = line


print "</pre>"
