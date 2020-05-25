#!/usr/bin/python3


scale = 4 # character scale up factor
side = 8 # character width/height 8px

# generate scrcode_from_petscii mapping
scrcode_from_petscii = []
for c in range(0, 256):
	if c < 0x20:
		d = c + 0x80 # inverted control characters
	elif c < 0x40:
		d = c
	elif c < 0x60:
		d = c - 0x40
	elif c < 0x80:
		d = c - 0x20
	elif c < 0xa0:
		d = c + 0x40 # inverted control characters
	elif c < 0xc0:
		d = c - 0x40
	else:
		d = c - 0x80
	scrcode_from_petscii.append(d)

def is_petscii_printable(petscii):
	return not (petscii < 0x20 or (petscii >= 0x80 and petscii < 0xa0))


def modifiers_and_scancodes_from_petscii(petscii, machine):
	modifiers_and_scancodes = []
	for modifier in description_from_modifier.keys():
		for scancode in range(0, len(petscii_from_scancode[machine][modifier])):
			if scancode in excluded_scancodes[machine]:
				continue
			p2 = petscii_from_scancode[machine][modifier][scancode]
			if p2 != 0xff and p2 == petscii:
				modifiers_and_scancodes.append((modifier, scancode))
	return modifiers_and_scancodes

def modifiers_and_scancodes_html_from_petscii(petscii, machine = 'C64'):
	modifiers_and_scancodes_html = []
	modifiers_and_scancodes = modifiers_and_scancodes_from_petscii(petscii, machine)
	other_petscii = None
	if len(modifiers_and_scancodes) == 0 and scrcode is not None:
		for check_petscii in petscii_from_scrcode[scrcode & 0x7f]:
			if check_petscii != petscii:
				other_petscii = check_petscii
				break
		if other_petscii:
			modifiers_and_scancodes = modifiers_and_scancodes_from_petscii(other_petscii, machine)

	if len(modifiers_and_scancodes) > 0:
		for (modifier, scancode) in modifiers_and_scancodes:
			m = description_from_modifier[modifier]
			d = description_from_scancode[machine][scancode]
			if d is None:
				d = '${:02X}'.format(scancode)

			if m:
				m = '<span class="key-box">{}</span> + '.format(m)
			else:
				m = ''
			modifiers_and_scancodes_html.append('{}<span class="key-box">{}</span>'.format(m, d))

	return (modifiers_and_scancodes_html, other_petscii)

def pixel_char_html_from_scrcode(scrcode, description = None):
	scrcode7 = scrcode & 0x7f
	if scrcode >= 0x80:
		inverted = 'inverted'
	else:
		inverted = ''
	return '<span class="container {}">{}<span class="character char-{}"></span></span>'.format(inverted, description if description else '', hex(scrcode7))

####################################################################

#
# generate petscii_from_scrcode mapping
#
petscii_from_scrcode = []
for c in range(0, 128):
	result = []
	for d in range(0, 256):
		if scrcode_from_petscii[d] == c:
			result.append(d)
	petscii_from_scrcode.append(result)

#
# read control code descriptions
#
description_from_control_code = {}
for line in open('petscii_control_codes.txt'):
	line = line.rstrip()
	if len(line) != 0:
		description_from_control_code[int(line[0:2], 16)] = line[3:]

#
# read PETSCII -> Unicode
#
description_from_unicode = {}
unicode_from_petscii = []
unicode_from_petscii.append({})
for line in open('C64IPRI.TXT'):
	line = line.rstrip()
	if line.startswith('#') or len(line) == 0:
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:12], 16)
	unicode_from_petscii[0][petscii] = unicode
	description_from_unicode[unicode] = line[14:]
unicode_from_petscii.append({})
for line in open('C64IALT.TXT'):
	line = line.rstrip()
	if line.startswith('#') or len(line) == 0:
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:12], 16)
	unicode_from_petscii[1][petscii] = unicode
	description_from_unicode[unicode] = line[14:]

#
# Read Keyboard Tables
#

description_from_modifier = {
	'regular': None,
	'shift': 'SHIFT',
	'cbm': 'C=',
	'ctrl': 'CTRL',
}

machines = ['VIC-20', 'C64', 'C128', 'TED']

petscii_from_scancode = {}
description_from_scancode = {}
excluded_scancodes = {}
for machine in machines:
	description_from_scancode[machine] = []
	excluded_scancodes[machine] = []
	petscii_from_scancode[machine] = {}
	petscii_from_scancode[machine]['regular'] = []
	petscii_from_scancode[machine]['shift'] = []
	petscii_from_scancode[machine]['cbm'] = []
	petscii_from_scancode[machine]['ctrl'] = []
	for line in open('keyboard_{}.txt'.format(machine.lower())):
		line = line.split('#')[0].rstrip()
		if len(line) == 0:
			continue
		key = line[:8].rstrip()
		line = line[8:]
		values = line.split(' ')
		while '' in values:
			values.remove('')
		if key == 'scan':
			values = [d.replace('COMMA', ',') for d in values]
			description_from_scancode[machine].extend(values)
		elif key == 'exclude':
			values = [int(v, 16) for v in values]
			excluded_scancodes[machine].extend(values)
		else:
			values = [int(v, 16) for v in values]
			petscii_from_scancode[machine][key].extend(values)


color_index_from_color_name = {
	'{black}': 0,
	'{white}': 1,
	'{red}': 2,
	'{cyan}': 3,
	'{green}': 5,
	'{purple}': 4,
	'{blue}': 6,
	'{yellow}': 7,
	'{orange}': 8,
	'{brown}': 9,
	'{lt.red}': 10,
	'{grey 1}': 11,
	'{grey 2}': 12,
	'{lt.green}': 13,
	'{lt.blue}': 14,
	'{grey 3}': 15,
}

hex_color_from_color_index = [
	'#000000',
	'#ffffff',
	'#813338',
	'#75cec8',
	'#8e3c97',
	'#56ac4d',
	'#2e2c9b',
	'#edf171',
	'#8e5029',
	'#553800',
	'#c46c71',
	'#4a4a4a',
	'#7b7b7b',
	'#a9ff9f',
	'#706deb',
	'#b2b2b2',
]

print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<html>')
print('<head>')
print('<title>Character Set | Ultimate C64 Reference</title>')
print('')
print('<script language="javascript">')
print('function test(element) {')
print('  var char = document.getElementById(element);')
print('  char.classList.toggle("highlighted");')
print('}')
print('</script>')
print('')
print('<link rel="stylesheet" href="../style.css">')
print('<link rel="stylesheet" href="style.css">')
print('<style type="text/css">')
print('')

for c in range(0, 128):
	x = (c & 15) * -8
	y = (c >> 4) * -8
	print('.char-{} {{ background-position:    {}px    {}px; }}'.format(hex(c), x, y))

print('')
print('</style>')

print('</head>')

print('<body>')

print('<div class="body">')
print('<h1>C64 Charset</h1>')

print('<div>')
print('	<img src="43627586.png" />')
print('</div>')
print('<div>')

for scrcode in range(0, 256):
	inverted = ''
	if scrcode >= 0x80:
		inverted = 'inverted'
	print('<span id="{}" type="button" class="container {}" onclick="test(\'{}\')"><span class="character char-{}"></span></span>'.format(hex(scrcode), inverted, hex(scrcode), hex(scrcode & 0x7f)))
	if scrcode & 15 == 15:
		print('<br />')


print('<br />')
print('<br />')
print('<br />')
print('<br />')
print('<br />')

for petscii in range(0, 256):
	scrcode = scrcode_from_petscii[petscii]
	description = description_from_control_code.get(petscii)
	print(pixel_char_html_from_scrcode(scrcode, description))
	if petscii & 15 == 15:
		print('<br />')

print('</div>')
print('</div>')

## Screencode Boxes
#for c in range(0, 256):
#	print('<h2>Screencode {}</h2>'.format(hex(c)))
#	c7 = c & 0x7f
#	if c >= 0x80:
#		inverted = 'inverted'
#		print('<li>REVERSE</li>')
#	else:
#		inverted = ''
#	print('<li><span class="container {}"><span class="character char-{}"></span></span></li>'.format(inverted, hex(c7)))
#
#	print('<table><th>PETSCII<br/>hex</th><th>PETSCII<br/>dec</th><th>Keyboard</th>')
#	for petscii in petscii_from_scrcode[c7]:
#		print('<tr>')
#		print('<td>${:02X}</td><td>{}</tt></td>'.format(petscii, petscii))
#		kbd = ''
#		for (modifier, scancode) in c64_modifiers_and_scancodes_from_petscii(petscii):
#			m = description_from_modifier[modifier]
#			d = description_from_c64_scancode[scancode]
#			if m:
#				m = '<span class="key-box">{}</span> + '.format(m)
#			else:
#				m = ''
#
#			kbd += '{}<span class="key-box">{}</span><br/>'.format(m, d)
#		print('<td>{}</td>'.format(kbd))
#		print('</tr>')
#	print('</table>')
#	petscii = petscii_from_scrcode[c7][0]
#	unicode = unicode_from_petscii[0][petscii]
#	print('<li>Unicode U+{:04X} # {}</li>'.format(unicode, description_from_unicode[unicode]))
#	print('<li>Unicode \'&#x{:x};\'</li>'.format(unicode))

# PETSCII Boxes
for petscii in range(0, 256):
	print('<h2>PETSCII ${:02X}</h2>'.format(petscii))
	scrcode = scrcode_from_petscii[petscii]
	print('<li>{}</li>'.format(pixel_char_html_from_scrcode(scrcode)))
	if not is_petscii_printable(petscii):
		print('<li>Description: {}</li>'.format(description_from_control_code[petscii]))

	print('<li>PETSCII hex: ${:02X}</li>'.format(petscii))
	print('<li>PETSCII dec: {}</li>'.format(petscii))
	print('<li>Screencode: ${:02X}</li>'.format(scrcode))

	(modifiers_and_scancodes_html, other_petscii) = modifiers_and_scancodes_html_from_petscii(petscii)

	if len(modifiers_and_scancodes_html) > 0:
		alt_text = ''
		if other_petscii:
			alt_text = ' (alt code ${:02X})'.format(other_petscii)
		print('<li>Keyboard{}:<ul>'.format(alt_text))
		for html in modifiers_and_scancodes_html:
			print('<li>{}</li>'.format(html))
		print('</ul></li>')

	print('</tr>')
	print('</table>')
	if is_petscii_printable(petscii):
		print('<li>Screencode ${:02X}</li>'.format(scrcode))
		unicode = unicode_from_petscii[0][petscii]
		print('<li>Unicode U+{:04X} # {}</li>'.format(unicode, description_from_unicode[unicode]))
		print('<li>Unicode \'&#x{:x};\'</li>'.format(unicode))

# PETSCII Table
print('<table border="1">')
print('<tr><th>PETSCII</th><th>C16 Keyboard</th><th>C64 Keyboard</th><th>C128 Keyboard (Extra)</th><th>C16, Plus/4 Keyboard</th><th>Screencode</th><th>Character</th><th colspan="3">Unicode Upper</th><th colspan="3">Unicode Lower</th></tr>')
for petscii in range(0, 256):
	print('<tr>')

	print('<td>${:02X}</td>'.format(petscii))

	scrcode = scrcode_from_petscii[petscii]

	# keyboard
	for machine in machines:
		print('<td>')
		(modifiers_and_scancodes_html, other_petscii) = modifiers_and_scancodes_html_from_petscii(petscii, machine)
		if len(modifiers_and_scancodes_html) > 0:
			if not other_petscii:
				for html in modifiers_and_scancodes_html:
					print('{}<br/>'.format(html))
		print('</td>')

	print('<td>${:02X}</td>'.format(scrcode))

	print('<td>{}</td>'.format(pixel_char_html_from_scrcode(scrcode)))

	if is_petscii_printable(petscii):
		unicode = unicode_from_petscii[0][petscii]
		print('<td>\'&#x{:x};\'</td>'.format(unicode))
		print('<td>U+{:04X}</td>'.format(unicode))
		print('<td>{}</td>'.format(description_from_unicode[unicode]))

		unicode = unicode_from_petscii[1][petscii]
		print('<td>\'&#x{:x};\'</td>'.format(unicode))
		print('<td>U+{:04X}</td>'.format(unicode))
		print('<td>{}</td>'.format(description_from_unicode[unicode]))

	else:
		description = description_from_control_code[petscii]
		color_html = ''
		if description in color_index_from_color_name:
			hex_color = hex_color_from_color_index[color_index_from_color_name[description]]
			color_html = 'bgcolor="{}"'.format(hex_color)
		print('<td {} colspan="3">{}</td>'.format(color_html, description))



	print('</tr>')

print('</table>')

print('</body>')
print('</html>')

