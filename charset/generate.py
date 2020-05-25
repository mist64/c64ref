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


def c64_modifiers_and_scancodes_from_petscii(petscii):
	c64_modifiers_and_scancodes = []
	for modifier in range(0, 4):
		for scancode in range(0, 64):
			 # skip l.shift, r.shift, ctrl, c=
			if scancode == 15 or scancode == 52 or scancode == 58 or scancode == 61:
				continue
			p2 = petscii_from_scancode[modifier][scancode]
			if p2 != 0xff and p2 == petscii:
				c64_modifiers_and_scancodes.append((modifier, scancode))
	return c64_modifiers_and_scancodes

def c64_modifiers_and_scancodes_html_from_petscii(petscii):
	c64_modifiers_and_scancodes_html = []
	c64_modifiers_and_scancodes = c64_modifiers_and_scancodes_from_petscii(petscii)
	other_petscii = None
	if len(c64_modifiers_and_scancodes) == 0 and scrcode is not None:
		for check_petscii in petscii_from_scrcode[scrcode & 0x7f]:
			if check_petscii != petscii:
				other_petscii = check_petscii
				break
		if other_petscii:
			c64_modifiers_and_scancodes = c64_modifiers_and_scancodes_from_petscii(other_petscii)

	if len(c64_modifiers_and_scancodes) > 0:
		for (modifier, scancode) in c64_modifiers_and_scancodes:
			m = description_from_modifier[modifier]
			d = description_from_scancode[scancode]

			if m:
				m = '<span class="key-box">{}</span> + '.format(m)
			else:
				m = ''
			c64_modifiers_and_scancodes_html.append('{}<span class="key-box">{}</span>'.format(m, d))

	return (c64_modifiers_and_scancodes_html, other_petscii)

def pixel_char_html_from_scrcode(scrcode):
	scrcode7 = scrcode & 0x7f
	if scrcode >= 0x80:
		inverted = 'inverted'
	else:
		inverted = ''
	return '<span class="container {}"><span class="character char-{}"></span></span>'.format(inverted, hex(scrcode7))

# generate petscii_from_scrcode mapping
petscii_from_scrcode = []
for c in range(0, 128):
	result = []
	for d in range(0, 256):
		if scrcode_from_petscii[d] == c:
			result.append(d)
	petscii_from_scrcode.append(result)

# read control code descriptions
description_from_control_code = {}
for line in open('petscii_control_codes.txt'):
	line = line.rstrip()
	if len(line) != 0:
		description_from_control_code[int(line[0:2], 16)] = line[3:]

# read PETSCII -> Unicode
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

# scancode to PETSCII tables
petscii_from_scancode = []
petscii_from_scancode.append([ # no modifiers
	0x14, 0x0D, 0x1D, 0x88, 0x85, 0x86, 0x87, 0x11,
	0x33, 0x57, 0x41, 0x34, 0x5A, 0x53, 0x45, 0x01,
	0x35, 0x52, 0x44, 0x36, 0x43, 0x46, 0x54, 0x58,
	0x37, 0x59, 0x47, 0x38, 0x42, 0x48, 0x55, 0x56,
	0x39, 0x49, 0x4A, 0x30, 0x4D, 0x4B, 0x4F, 0x4E,
	0x2B, 0x50, 0x4C, 0x2D, 0x2E, 0x3A, 0x40, 0x2C,
	0x5C, 0x2A, 0x3B, 0x13, 0x01, 0x3D, 0x5E, 0x2F,
	0x31, 0x5F, 0x04, 0x32, 0x20, 0x02, 0x51, 0x03,
])
petscii_from_scancode.append([ # shift
	0x94, 0x8D, 0x9D, 0x8C, 0x89, 0x8A, 0x8B, 0x91,
	0x23, 0xD7, 0xC1, 0x24, 0xDA, 0xD3, 0xC5, 0x01,
	0x25, 0xD2, 0xC4, 0x26, 0xC3, 0xC6, 0xD4, 0xD8,
	0x27, 0xD9, 0xC7, 0x28, 0xC2, 0xC8, 0xD5, 0xD6,
	0x29, 0xC9, 0xCA, 0x30, 0xCD, 0xCB, 0xCF, 0xCE,
	0xDB, 0xD0, 0xCC, 0xDD, 0x3E, 0x5B, 0xBA, 0x3C,
	0xA9, 0xC0, 0x5D, 0x93, 0x01, 0x3D, 0xDE, 0x3F,
	0x21, 0x5F, 0x04, 0x22, 0xA0, 0x02, 0xD1, 0x83,
])
petscii_from_scancode.append([ # cbm
	0x94, 0x8D, 0x9D, 0x8C, 0x89, 0x8A, 0x8B, 0x91,
	0x96, 0xB3, 0xB0, 0x97, 0xAD, 0xAE, 0xB1, 0x01,
	0x98, 0xB2, 0xAC, 0x99, 0xBC, 0xBB, 0xA3, 0xBD,
	0x9A, 0xB7, 0xA5, 0x9B, 0xBF, 0xB4, 0xB8, 0xBE,
	0x29, 0xA2, 0xB5, 0x30, 0xA7, 0xA1, 0xB9, 0xAA,
	0xA6, 0xAF, 0xB6, 0xDC, 0x3E, 0x5B, 0xA4, 0x3C,
	0xA8, 0xDF, 0x5D, 0x93, 0x01, 0x3D, 0xDE, 0x3F,
	0x81, 0x5F, 0x04, 0x95, 0xA0, 0x02, 0xAB, 0x83,
])
petscii_from_scancode.append([ # ctrl
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
	0x1C, 0x17, 0x01, 0x9F, 0x1A, 0x13, 0x05, 0xFF,
	0x9C, 0x12, 0x04, 0x1E, 0x03, 0x06, 0x14, 0x18,
	0x1F, 0x19, 0x07, 0x9E, 0x02, 0x08, 0x15, 0x16,
	0x12, 0x09, 0x0A, 0x92, 0x0D, 0x0B, 0x0F, 0x0E,
	0xFF, 0x10, 0x0C, 0xFF, 0xFF, 0x1B, 0x00, 0xFF,
	0x1C, 0xFF, 0x1D, 0xFF, 0xFF, 0x1F, 0x1E, 0xFF,
	0x90, 0x06, 0xFF, 0x05, 0xFF, 0xFF, 0x11, 0xFF,
])

description_from_modifier = [
	None,
	'SHIFT',
	'C=',
	'CTRL',
]

description_from_scancode = [
	'DEL','RETURN','←CRSR→','F4','F1','F2','F3','↑CRSR↓',
	'3','W','A','4','Z','S','E','L.SHIFT',
	'5','R','D','6','C','F','T','X',
	'7','Y','G','8','B','H','U','V',
	'9','I','J','0','M','K','O','N',
	'+','P','L','-','.',':','@',',',
	'£','*',';','HOME','R.SHIFT','=','↑','/',
	'1','←','CTRL','2','SPACE','C=','Q','STOP',
]

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

for c in range(0, 128):
	print('<span id="{}" type="button" class="container" onclick="test(\'{}\')"><span class="character char-{}"></span></span>'.format(hex(c), hex(c), hex(c)))
	if c & 15 == 15:
		print('<br />')

for c in range(0, 128):
	print('<span id="{}" type="button" class="container inverted" onclick="test(\'{}\')"><span class="character char-{}"></span></span>'.format(hex(c + 128), hex(c + 128), hex(c)))
	if c & 15 == 15:
		print('<br />')

print('<br />')
print('<br />')
print('<br />')
print('<br />')
print('<br />')

# Interchange => Video
# $00 - $1F => (control characters)
# $20 - $3F => $20 - $3F
# $40 - $5F => $00 - $1F
# $60 - $7F => $40 - $5F
# $80 - $9F => (control characters)
# $A0 - $BF => $60 - $7F
# $C0 - $DF => $40 - $5F
# $E0 - $FF => $60 - $7F


for c1 in range(0, 256):
	c = scrcode_from_petscii[c1]
	if c is None:
		print('<span class="container">{}</span>'.format(description_from_control_code[c1]))
	else:
		print('<span class="container"><span class="character char-{}"></span></span>'.format(hex(c)))
	if c1 & 15 == 15:
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
#			d = description_from_scancode[scancode]
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
	if is_petscii_printable(petscii):
		print('<li><span class="container"><span class="character char-{}"></span></span></li>'.format(hex(scrcode)))
	else:
		print('<li><span class="container">{}</span></li>'.format(description_from_control_code[petscii]))

	print('<li>PETSCII hex: ${:02X}</li>'.format(petscii))
	print('<li>PETSCII dec: {}</li>'.format(petscii))


	(c64_modifiers_and_scancodes_html, other_petscii) = c64_modifiers_and_scancodes_html_from_petscii(petscii)

	if len(c64_modifiers_and_scancodes_html) > 0:
		alt_text = ''
		if other_petscii:
			alt_text = ' (alt code ${:02X})'.format(other_petscii)
		print('<li>Keyboard{}:<ul>'.format(alt_text))
		for html in c64_modifiers_and_scancodes_html:
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
print('<tr><th>PETSCII</th><th>Keyboard</th><th>Screencode</th><th>Character</th><th colspan="3">Unicode Upper</th><th colspan="3">Unicode Lower</th></tr>')
for petscii in range(0, 256):
	print('<tr>')

	print('<td>${:02X}</td>'.format(petscii))

	scrcode = scrcode_from_petscii[petscii]

	(c64_modifiers_and_scancodes_html, other_petscii) = c64_modifiers_and_scancodes_html_from_petscii(petscii)

	print('<td>')
	if len(c64_modifiers_and_scancodes_html) > 0:
		if not other_petscii:
			for html in c64_modifiers_and_scancodes_html:
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

