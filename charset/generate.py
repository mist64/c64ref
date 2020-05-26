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
			modifiers_and_scancodes_html.append('<div class="key-box">{}<span class="key-box">{}</span></div>'.format(m, d))

	return (modifiers_and_scancodes_html, other_petscii)

def pixel_char_html_from_scrcode(scrcode, description = None, hex_color = None):
	scrcode7 = scrcode & 0x7f
	if scrcode >= 0x80:
		inverted = 'inverted'
	else:
		inverted = ''

	description_html = ''
	color_html = ''
		
	if description is not None:
		if hex_color is None:
			hex_color = '#0008'
		else:
			hex_color += 'E0'
		color_html = ' style="background-color: {}; border-color:{};"'.format(hex_color, hex_color)
		description_html = '<span class="char-txt"{}>{}<br /></span>'.format(color_html, description)
		#description_html = '<span class="char-txt"{}><svg viewBox="0 0 10 10"><text x="0" y="15">{}</text></svg></span>'.format(color_html, description)

	return '<div class="char-box {}" id="scrcode_{}" type="button" onclick="test(\'scrcode_{}\')"><span class="char-img char-{}"></span>{}</div>'.format(inverted, hex(scrcode), hex(scrcode), hex(scrcode7), description_html)

####################################################################

#
# generate petscii_from_scrcode mapping
#
petscii_from_scrcode = []
for c in range(0, 256):
	result = []
	for d in range(0, 256):
		if scrcode_from_petscii[d] == c:
			result.append(d)
	petscii_from_scrcode.append(result)

#
# Read Control Code Descriptions
#
description_from_control_code_symbol = {
	'CLEAR':            ('CLR', 'Clear'),
	'COL_BLACK':        ('Blk', 'Set text color to black'),
	'COL_BLUE':         ('Blu', 'Set text color to Blue'),
	'COL_BLUE_GREEN':   ('BlGrn', 'Set text color to Blue Green'),
	'COL_BROWN':        ('Brn', 'Set text color to Brown'),
	'COL_CYAN':         ('Cyn', 'Set text color to Cyan'),
	'COL_DARK_BLUE':    ('DkBlu', 'Set text color to Dark Blue'),
	'COL_DARK_CYAN':    ('DkCyn', 'Set text color to Dark Cyan'),
	'COL_DARK_GRAY':    ('DkGry', 'Set text color to Dark Gray'),
	'COL_DARK_PURPLE':  ('DkPur', 'Set text color to Dark Purple'),
	'COL_DARK_YELLOW':  ('DkYel', 'Set text color to Dark Yellow'),
	'COL_GREEN':        ('Grn', 'Set text color to Green'),
	'COL_LIGHT_BLUE':   ('LBlu', 'Set text color to Light Blue'),
	'COL_LIGHT_CYAN':   ('LtCyn', 'Set text color to Light Cyan'),
	'COL_LIGHT_GRAY':   ('LtGry', 'Set text color to Light Gray'),
	'COL_LIGHT_GREEN':  ('LGrn', 'Set text color to Light Green'),
	'COL_LIGHT_GRN':    ('LtGrn', 'Set text color to Light Green'),
	'COL_LIGHT_RED':    ('LRed', 'Set text color to Light Red'),
	'COL_MEDIUM_GRAY':  ('MdGry', 'Set text color to Medium Gray'),
	'COL_ORANGE':       ('Orng', 'Set text color to Orange'),
	'COL_PINK':         ('Pink', 'Set text color to Pink'),
	'COL_PURPLE':       ('Pur', 'Set text color to Purple'),
	'COL_RED':          ('Red', 'Set text color to Red'),
	'COL_WHITE':        ('Wht', 'Set text color to White'),
	'COL_YELLOW':       ('Yel', 'Set text color to Yellow'),
	'COL_YELLOW_GREEN': ('YlGrn', 'Set text color to Yellow Green'),
	'CRSR_DOWN':        ('Crsr ↓', 'Cursor Down'),
	'CRSR_HOME':        ('HOME', 'Cursor Home'),
	'CRSR_LEFT':        ('Crsr ←', 'Cursor Left'),
	'CRSR_RIGHT':       ('Crsr →', 'Cursor Right'),
	'CRSR_UP':          ('Crsr ↑', 'Cursor Up'),
	'DEL':              ('DEL', 'Delete'),
	'DIS_CASE_SWITCH':  ('Disable Case', 'Disable Case-Switching Keys'),
	'DIS_MODE_SWITCH':  ('Disable Mode', 'Disable Mode Switch'),
	'ENA_CASE_SWITCH':  ('Enable Case', 'Enable Case-Switching Keys'),
	'ENA_MODE_SWITCH':  ('Enable Mode', 'Enable Mode Switch'),
	'ESC':              ('ESC', 'Escape'),
	'FLASH_OFF':        ('Flash Off', 'Flash Off'),
	'FLASH_ON':         ('Flash On', 'Flash On'),
	'INST':             ('INST', 'Insert'),
	'KEY_F1':           ('f1', 'f1 key'),
	'KEY_F2':           ('f2', 'f2 key'),
	'KEY_F3':           ('f3', 'f3 key'),
	'KEY_F4':           ('f4', 'f4 key'),
	'KEY_F5':           ('f5', 'f5 key'),
	'KEY_F6':           ('f6', 'f6 key'),
	'KEY_F7':           ('f7', 'f7 key'),
	'KEY_F8':           ('f8', 'f8 key'),
	'LINE_FEED':        ('LF', 'Line Feed'),
	'LOWER_CASE':       ('Lower Case', 'Switch to lower case'),
	'RETURN':           ('RETURN', 'Return'),
	'RUN':              ('RUN', 'RUN'),
	'RVS_OFF':          ('RVS Off', 'Reverse Off'),
	'RVS_ON':           ('RVS On', 'Reverse On'),
	'SHIFT_RETURN':     ('SHIFT RETURN', 'Disabled Return'),
	'TAB_SET_CLR':      ('Tab set/clr', 'Tab set/clear'),
	'UNDERLINE_OFF':    ('Underline Off', 'Underline Off'),
	'UNDERLINE_ON':     ('Underline On', 'Underline On'),
	'UPPER_CASE':       ('Upper Case', 'Switch to upper case'),
}
description_from_control_code = {}
symbol_from_control_code = {}
for machine in ['C64', 'C128', 'TED']:
	symbol_from_control_code[machine] = {}
	description_from_control_code[machine] = {}
	for line in open('control_codes_{}.txt'.format(machine.lower())):
		line = line.split('#')[0].rstrip()
		if len(line) == 0:
			continue
		petscii = int(line[0:2], 16)
		symbol = line[3:].split(' ')[0] # XXX there may be more
		symbol_from_control_code[machine][petscii] = symbol
		if len(symbol) > 0:
			description_from_control_code[machine][petscii] = description_from_control_code_symbol[symbol]


#
# Read Palettes
#
color_index_from_color_name = {}
hex_color_from_color_index = {}
for machine in ['C64', 'C128', 'TED']:
	color_index_from_color_name[machine] = {}
	hex_color_from_color_index[machine] = {}
	color_index = 0
	for line in open('palette_{}.txt'.format(machine.lower())):
		line = line.split('#')[0].rstrip()
		if len(line) == 0:
			continue
		values = line.split(' ')
		while '' in values:
			values.remove('')
		hex_color = '#' + values[0]
		color_name = values[1]
		color_index_from_color_name[machine][color_name] = color_index
		hex_color_from_color_index[machine][color_index] = hex_color
		color_index += 1

#
# read PETSCII -> Unicode
#
description_from_unicode = {}
unicode_from_petscii = []
unicode_from_petscii.append({})
for line in open('C64IPRI.TXT'):
	line = line.split('#')[0].rstrip()
	if len(line) == 0:
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:12], 16)
	unicode_from_petscii[0][petscii] = unicode
	description_from_unicode[unicode] = line[14:]
unicode_from_petscii.append({})
for line in open('C64IALT.TXT'):
	line = line.split('#')[0].rstrip()
	if len(line) == 0:
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

####################################################################

print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<html>')
print('<head>')
print('<title>Character Set | Ultimate C64 Reference</title>')
print('')
print('<script language="javascript" src="script.js"></script>')
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

#print('<div id="current-image">')
#print('	<img src="43627586.png" />')
#print('</div>')


print('<div">')

print('<div id="screencode_overview">')

for scrcode in range(0, 256):
	print(pixel_char_html_from_scrcode(scrcode))
	if scrcode & 15 == 15:
		print('<br />')

print('</div>')

print('<div id="info_box"></div>')

print('</div>')


print('<br />')
print('<br />')
print('<br />')
print('<br />')
print('<br />')

print('<div">')

print('<div id="petscii_overview">')

machine = 'C64'

for petscii in range(0, 256):
	scrcode = scrcode_from_petscii[petscii]
	description = None
	if not is_petscii_printable(petscii):
		description = description_from_control_code[machine].get(petscii)
		if description:
			(description, _) = description
		if not description:
			description = ''

	hex_color = None
	if not is_petscii_printable(petscii):
		symbol = symbol_from_control_code[machine][petscii]
		if symbol in color_index_from_color_name['C64']:
			hex_color = hex_color_from_color_index['C64'][color_index_from_color_name['C64'][symbol]]
	print(pixel_char_html_from_scrcode(scrcode, description, hex_color))
	if petscii & 15 == 15:
		print('<br />')

print('</div>')

print('</div>')
print('</div>')

# Screencode Boxes
for scrcode in range(0, 256):
	print('<div id="info_scrcode_{}">'.format(hex(scrcode)))
	print('<h2>Screencode {}</h2>'.format(hex(scrcode)))
	scrcode7 = scrcode & 0x7f
	is_reverse = scrcode >= 0x80
	if is_reverse:
		inverted = 'inverted'
		print('<li>REVERSE</li>')
	else:
		inverted = ''
	print('<li><span class="char-box {}"><span class="char-img char-{}"></span></span></li>'.format(inverted, hex(scrcode7)))

	print('<table><th>PETSCII<br/>hex</th><th>PETSCII<br/>dec</th><th>Keyboard</th><th>Mode</th>')
	run = 0
	if is_reverse:
		scrcode_list = [scrcode7, scrcode]
	else:
		scrcode_list = [scrcode]
	for eff_scrcode in scrcode_list:
		for petscii in petscii_from_scrcode[eff_scrcode]:
			print('<tr>')
			print('<td>${:02X}</td><td>{}</tt></td>'.format(petscii, petscii))

			(modifiers_and_scancodes_html, other_petscii) = modifiers_and_scancodes_html_from_petscii(petscii)

			print('<td>')
			if other_petscii == None and len(modifiers_and_scancodes_html) > 0:
				for html in modifiers_and_scancodes_html:
					print('{}<br/>'.format(html))
			print('</td>')
			print('<td>')
			if run == 0:
				if is_reverse:
					print('in reverse mode')
			else:
				print('control code in quote mode')
			print('</td>')

			print('</tr>')
		run += 1

	print('</table>')
	petscii = petscii_from_scrcode[scrcode7][0]
	unicode = unicode_from_petscii[0][petscii]
	print('<li>Unicode U+{:04X} # {}</li>'.format(unicode, description_from_unicode[unicode]))
	print('<li>Unicode <span class="unicode-box">&#x{:x};</span></li>'.format(unicode))
	print('</div>');

# PETSCII Boxes
for petscii in range(0, 256):

	print('<div id="info_petscii_{}">'.format(hex(petscii)))
	print('<h2>PETSCII ${:02X}</h2>'.format(petscii))
	scrcode = scrcode_from_petscii[petscii]
	print('<li>{}</li>'.format(pixel_char_html_from_scrcode(scrcode)))
	if not is_petscii_printable(petscii):
		description = description_from_control_code[machine].get(petscii)
		if description:
			(_, description) = description
		if not description:
			description = ''
		print('<li>Description: {}</li>'.format(description))

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
		print('<li>Unicode <span class="unicode-box">&#x{:x};</span></li>'.format(unicode))
	print('</div>');

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
		for machine in ['C64', 'C128', 'TED']: #machines:
			description = description_from_control_code[machine].get(petscii)
			if description:
				(_, description) = description
			color_html = ''
			symbol = symbol_from_control_code[machine][petscii]
			if not description:
				description = ''
			if symbol in color_index_from_color_name[machine]:
				hex_color = hex_color_from_color_index[machine][color_index_from_color_name[machine][symbol]]
				description = '<span style="background-color:{}; border: solid gray 1px; width: 1em; height: 1em; display: inline-block;"> </span> '.format(hex_color) + description
			print('<td>{}</td>'.format(description))



	print('</tr>')

print('</table>')

print('</body>')
print('</html>')

