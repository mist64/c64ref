#!/usr/bin/env python3

import os

####################################################################

# Keyboard

VSCALE = 2
SCALE = 8
ROUND = 5
HINSET = 1
VINSET = 1
FONT_SIZE1 = 14.5
FONT_SIZE2 = 9
FONT_VADJUST1 = 7
FONT_VADJUST2 = 4
FONT_LEN_CUTOFF = 1
BIG_WHITELIST = ['00', 'CE']

cap_replacements = {
	'L.SHIFT': 'SHIFT',
	'R.SHIFT': 'SHIFT',
	'CRSR↑': '↑',
	'CRSR↓': '↓',
	'CRSR←': '←',
	'CRSR→': '→',
	'↑CRSR↓': '↑↓',
	'←CRSR→': '←→',
	'LINE_FEED': 'LF',
	'NO_SCROLL': 'SCRL',
	'GRAPH': 'GRPH',
	'REPEAT': 'RPT',
	'40/80_DISPLAY': '40/80',
	'CAPS_LOCK': 'CAPS',
}

cap_autoshift_map = {
	'↑CRSR↓': '↑',
	'←CRSR→': '←',
}

def flood_fill(x, y):
	c = layout_lines[y][x]
	if c == '+' or c == '|' or c == '-' or c == 'X':
		return
	l = list(layout_lines[y])
	l[x] = 'X'
	cells.append((x, y))
	layout_lines[y] = ''.join(l)
	flood_fill(x + 1, y)
	flood_fill(x - 1, y)
	flood_fill(x, y + 1)
	flood_fill(x, y - 1)

def html_encode(s1):
	s2 = ''
	for c in s1:
		if c == '&':
			c = '&amp;'
		elif c == '<':
			c = '&lt;'
		elif c == '>':
			c = '&gt;'
		s2 += c
	return s2

def keyboard_layout_html(machine, ll):
	global layout_lines
	global cells

	layout_lines = ll

	html = ''

	cells_from_scancode = {}

	for y in range(0, len(layout_lines)):
		for x in range(0, len(layout_lines[y])):
			c = layout_lines[y][x]
			if c != '+' and c != '|' and c != '-' and c != 'X':
				# we found a key!
				scancode = ''
				for x2 in range(x, len(layout_lines[y])):
					c = layout_lines[y][x2]
					if c == '+' or c == '|' or c == '-':
						break
					scancode += c
				scancode = scancode.lstrip().rstrip()
				if scancode == '':
					continue # empty area
				if scancode[0] == '/':
					# the C65 keyboard has LEFT and UP keys that
					# simulate SHIFT and RIGHT/DOWN
					scancode = int(scancode[1:], 16) | 0x10000
				elif scancode == '...':
					scancode = -1 # key does no produce a scancode
				else:
					scancode = int(scancode, 16)
				# mark all cells as seen
				cells = []
				flood_fill(x, y)
				if scancode in cells_from_scancode:
					cells_from_scancode[scancode].append(cells)
				else:
					cells_from_scancode[scancode] = [cells]

	html += '<div class="{}">'.format(machine)
	html += '<h2>{}</h2>'.format(machine)

	total_width = 0

	for line in layout_lines:
		if len(line) > total_width:
			total_width = len(line)

	total_width *= SCALE
	total_height = len(layout_lines) * VSCALE * SCALE

	svg = '<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">'.format(total_width, total_height)
	svg += '<!-- This SVG was generated from a textual description. Check out c64ref on GitHub for more information. -->'
	for scancode in cells_from_scancode.keys():
		cells = cells_from_scancode[scancode]

		for cell in cells:
			minx = None
			miny = None
			maxx = None
			maxy = None
			for (x, y) in cell:
				if (not minx) or x < minx:
					minx = x
				if (not miny) or y < miny:
					miny = y
				if (not maxx) or x > maxx:
					maxx = x
				if (not maxy) or y > maxy:
					maxy = y
			width = maxx - minx + 2
			height = maxy - miny + 2

			miny *= VSCALE
			height *= VSCALE

			minx *= SCALE
			miny *= SCALE
			width *= SCALE
			height *= SCALE

			minx += HINSET
			miny += VINSET
			width -= HINSET*2
			height -= VINSET*2

			rscancode = scancode & 0xffff
			if rscancode >= 0 and rscancode < len(description_from_scancode[machine]):
				description = description_from_scancode[machine][rscancode]
			else:
				description = ''
			if scancode & 0x10000 and description in cap_autoshift_map:
				description = cap_autoshift_map[description]
			if description in cap_replacements:
				description = cap_replacements[description]
			if description.startswith('[') and description.endswith(']'):
				description = description[1:-1]
			#description = description.replace('_', '\r')

			if len(description) > FONT_LEN_CUTOFF and not description in BIG_WHITELIST:
				font_size = FONT_SIZE2
				font_vadjust = FONT_VADJUST2
			else:
				font_size = FONT_SIZE1
				font_vadjust = FONT_VADJUST1

			description = html_encode(description)

			if height > width:
				style = 'style="writing-mode: tb; glyph-orientation-vertical: 0; letter-spacing: -1;"'
				font_vadjust = 0
			else:
				style = ''

			petscii = {}
			for modifier in description_from_modifier.keys():
				if scancode & 0x10000:
					# keys that press SHIFT internally
					petscii[modifier] = petscii_from_scancode[machine]['shift'][scancode & 0xffff]
				elif len(petscii_from_scancode[machine][modifier]) > scancode:
					petscii[modifier] = petscii_from_scancode[machine][modifier][scancode]
				else:
					petscii[modifier] = 0xff

			modifier = modifier_scancodes[machine].get(scancode)
			if not modifier:
				modifier = ''

			svg += '<a xlink:href="javascript:void(0)" onclick="highlight_key(\'{}\',{}, \'petscii_{}\',\'petscii_{}\',\'petscii_{}\',\'petscii_{}\', \'{}\');">'.format(machine, scancode, hex(petscii['regular']), hex(petscii['shift']), hex(petscii['cbm']), hex(petscii['ctrl']), modifier)
			svg += '<rect class="keyrect keyrect_{}_{}" x="{}" y="{}" rx="{}" ry="{}" width="{}" height="{}" style="stroke:black;fill:white;"/>\n'.format(machine, scancode, minx, miny, ROUND, ROUND, width, height)
			svg += '<text class="keytext keytext_{}_{}" text-anchor="middle" font-family="Helvetica" font-size="{}" {} fill="black">'.format(machine, scancode, font_size, style)
			svg += '<tspan x="{}" y="{}">{}</tspan>'.format(minx + width/2, miny + height/2 + font_vadjust, description)
			svg += '</text>'
			svg += '</a>'

	svg += '      </svg>'
	html += svg
	html += '</div>'
	return html

####################################################################

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
			if scancode in modifier_scancodes[machine].keys():
				continue
			p2 = petscii_from_scancode[machine][modifier][scancode]
			if p2 != 0xff and p2 == petscii:
				modifiers_and_scancodes.append((modifier, scancode))
	return modifiers_and_scancodes

def modifiers_and_scancodes_html_from_petscii(petscii, scrcode, other_ok = True, machine = 'C64'):
	modifiers_and_scancodes_html = []
	modifiers_and_scancodes = modifiers_and_scancodes_from_petscii(petscii, machine)
	other_petscii = None
	if other_ok and len(modifiers_and_scancodes) == 0 and scrcode is not None:
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
			else:
				d = d.replace('_', ' ')

			if m:
				m = '<span class="key-box">{}</span> + '.format(m)
			else:
				m = ''
			modifiers_and_scancodes_html.append('<div class="key-box">{}<span class="key-box">{}</span></div>'.format(m, html_encode(d)))

	return (modifiers_and_scancodes_html, other_petscii)

def all_keyboard_html_from_petscii(petscii, scrcode, other_ok = False):
	all_modifiers_and_scancodes_html = {}
	for machine in machines:
		all_modifiers_and_scancodes_html[machine] = []
		(modifiers_and_scancodes_html, other_petscii) = modifiers_and_scancodes_html_from_petscii(petscii, scrcode, other_ok, machine)
		if len(modifiers_and_scancodes_html) > 0:
			html = ''
			for h in modifiers_and_scancodes_html:
					html += '{}'.format(h)
		else:
			html = ' -'
		all_modifiers_and_scancodes_html[machine] = html

	if len(set(all_modifiers_and_scancodes_html.values())) == 1:
		return (all_modifiers_and_scancodes_html[machines[0]], other_petscii)
	else:
		all_keyboard_html = ''
		for machine in machines:
			all_keyboard_html += '<div class="{}"><b>{}</b>:'.format(machine, machine)
			all_keyboard_html += all_modifiers_and_scancodes_html[machine]
			all_keyboard_html += '</div>'
		return (all_keyboard_html, other_petscii)

def combined_description_from_control_code(petscii):
	description_to_machines = {}
	machines_with_function = []
	for machine in machines:
		if machine in description_from_control_code and petscii in description_from_control_code[machine]:
			(_, description) = description_from_control_code[machine][petscii]
			if description in description_to_machines:
				description_to_machines[description].append(machine)
			else:
				description_to_machines[description] = [machine]
			machines_with_function.append(machine)

	machines_without_function = list(machines) # copy
	for machine in machines_with_function:
		machines_without_function.remove(machine)
	if len(machines_without_function) > 0:
		description_to_machines['<i>no function</i>'] = machines_without_function


	combined_description = '<dl>'
	for description in description_to_machines.keys():
		if len(description_to_machines[description]) != len(machines):
			machines_string = '<dt>' + '/'.join(description_to_machines[description]) + ':</dt><dd>'
		else:
			machines_string = '<dt></dt><dd>'
		combined_description += machines_string + description + '</dd>'
	combined_description += '</dl>'
	return combined_description


def pixel_char_html_from_scrcode(scrcode, description = None, link = None, filename = None):
	scrcode7 = scrcode & 0x7f

	description_html = ''
		
	if description is not None:
		description_html = '<div class="char-txt">{}<br/></div>'.format(description)
		#description_html = '<div class="char-txt"><svg viewBox="0 0 10 10"><text x="0" y="15">{}</text></svg></div>'.format(description)

	link_html1 = ''
	link_html2 = ''
	if link:
		link_html1 = ' onclick="test(\'{}\')"'.format(link)
		link_html2 = ' id="{}"'.format(link)

	return '<div class="char-box"{}{}><div class="char-img char-{}"></div>{}</div>'.format(link_html2, link_html1, hex(scrcode), description_html)

def displayname_for_charset_details(machine, locale, type, version):
	if locale == '':
		locale = 'US'
	return '{} {} {} ({})'.format(locale, type, version, machine)

####################################################################

machines = ['PET-N', 'PET-B', 'CBM2', 'VIC-20', 'C64', 'C128', 'C65', 'TED']

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
	'BELL_TONE':        ('BEL', 'Bell Tone'),
	'CE':               ('CE', 'Clear Entry'),
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
	'DEL_LINE':         ('DEL Line', 'Delete Line'),
	'DIS_CASE_SWITCH':  ('Lock Case', 'Disable Case-Switching Keys'),
	'DIS_MODE_SWITCH':  ('Lock Mode', 'Disable Mode Switch'),
	'ENA_CASE_SWITCH':  ('Unlock Case', 'Enable Case-Switching Keys'),
	'ENA_MODE_SWITCH':  ('Unlock Mode', 'Enable Mode Switch'),
	'ERASE_TO_BEGIN':   ('Erase Line ←', 'Erase to Begining of Line'),
	'ERASE_TO_END':     ('Erase Line →', 'Erase to End of Line'),
	'ESC':              ('ESC', 'Escape'),
	'FLASH_OFF':        ('FLASH Off', 'Flash Off'),
	'FLASH_ON':         ('FLASH On', 'Flash On'),
	'HELP':             ('HELP', 'HELP'),
	'INSERT_LINE':      ('INST Line', 'Insert Line'),
	'INST':             ('INST', 'Insert'),
	'KEY_F1':           ('f1', 'f1 key'),
	'KEY_F10':          ('f10', 'f10 key'),
	'KEY_F11':          ('f11', 'f11 key'),
	'KEY_F12':          ('f12', 'f12 key'),
	'KEY_F13':          ('f13', 'f13 key'),
	'KEY_F14':          ('f14', 'f14 key'),
	'KEY_F2':           ('f2', 'f2 key'),
	'KEY_F3':           ('f3', 'f3 key'),
	'KEY_F4':           ('f4', 'f4 key'),
	'KEY_F5':           ('f5', 'f5 key'),
	'KEY_F6':           ('f6', 'f6 key'),
	'KEY_F7':           ('f7', 'f7 key'),
	'KEY_F8':           ('f8', 'f8 key'),
	'KEY_F9':           ('f9', 'f9 key'),
	'LINE_FEED':        ('LF', 'Line Feed'),
	'LOWER_CASE':       ('Lower Case', 'Switch to lower case'),
	'RETURN':           ('RET', 'Return'),
	'RUN':              ('RUN', 'RUN'),
	'RVS_OFF':          ('RVS Off', 'Reverse Off'),
	'RVS_ON':           ('RVS On', 'Reverse On'),
	'SCROLL_DOWN':      ('Scroll Down', 'Scroll Down'),
	'SCROLL_UP':        ('Scroll Up', 'Scroll Up'),
	'SET_TAB':          ('Set TAB', 'Set TAB'),
	'SHIFT_CE':         ('SHIFT CE', 'SHIFT Clear Entry'),
	'SHIFT_RETURN':     ('SHIFT RET', 'Disabled Return'),
	'STOP':             ('STOP', 'STOP'),
	'TAB':              ('TAB', 'Forward TAB'),
	'TAB_SET_CLR':      ('Tab set/clr', 'Tab set/clear'),
	'UNDERLINE_OFF':    ('ULINE Off', 'Underline Off'),
	'UNDERLINE_ON':     ('ULINE On', 'Underline On'),
	'UPPER_CASE':       ('Upper Case', 'Switch to upper case'),
	'WINDOW_BOTTOM':    ('Win Bot', 'Window Bottom'),
	'WINDOW_TOP':       ('Win Top', 'Window Top'),
}
description_from_control_code = {}
symbol_from_control_code = {}
for machine in machines:
	symbol_from_control_code[machine] = {}
	description_from_control_code[machine] = {}
	for line in open('control_codes_{}.txt'.format(machine.lower())):
		line = line.split('#')[0].rstrip()
		if len(line) == 0:
			continue
		petscii = int(line[0:2], 16)
		symbol = line[3:].split(' ')[0] # XXX C128 and C65 have more than one function!
		symbol_from_control_code[machine][petscii] = symbol
		if len(symbol) > 0:
			description_from_control_code[machine][petscii] = description_from_control_code_symbol[symbol]


#
# Read Palettes
#
color_index_from_color_name = {}
hex_color_from_color_index = {}
for machine in machines:
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
unicode_from_petscii = {}
unicode_from_petscii['upper'] = {}
for line in open('C64IPRI.TXT'):
	line = line.rstrip()
	if len(line) == 0 or line.startswith('#'):
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:12], 16)
	unicode_from_petscii['upper'][petscii] = unicode
	description_from_unicode[unicode] = line[14:]
unicode_from_petscii['lower'] = {}
for line in open('C64IALT.TXT'):
	line = line.rstrip()
	if len(line) == 0 or line.startswith('#'):
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:12], 16)
	unicode_from_petscii['lower'][petscii] = unicode
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

petscii_from_scancode = {}
description_from_scancode = {}
modifier_scancodes = {}
keyboard_layout = {}
for machine in machines:
	description_from_scancode[machine] = []
	modifier_scancodes[machine] = {}
	petscii_from_scancode[machine] = {}
	petscii_from_scancode[machine]['regular'] = []
	petscii_from_scancode[machine]['shift'] = []
	petscii_from_scancode[machine]['cbm'] = []
	petscii_from_scancode[machine]['ctrl'] = []
	keyboard_layout[machine] = []
	for line in open('keyboard_{}.txt'.format(machine.lower())):
		line = line.split('#')[0].rstrip()
		if len(line) == 0:
			continue
		key = line[:8].rstrip()
		line = line[8:]
		values = line.split(' ')
		while '' in values:
			values.remove('')
		if key == 'layout':
			keyboard_layout[machine].append(line)
		elif key == 'cap' or key == 'capx':
			values = [d.replace('HASH', '#') for d in values]
			description_from_scancode[machine].extend(values)
		elif key == 'mod':
			scancode = int(values[0], 16)
			cap = values[1]
			modifier_scancodes[machine][scancode] = cap
		else:
			v1 = values
			values = []
			for v in v1:
				if v.startswith('X'):
					values.append(-int(v[1:], 16))
				else:
					values.append(int(v, 16))
			petscii_from_scancode[machine][key].extend(values)
	while keyboard_layout[machine][0] == '':
		keyboard_layout[machine] = keyboard_layout[machine][1:]

####################################################################

charsets = [
	('---', 'Common', '', '', ''),
	('vic-20_us_upper', 'VIC-20', '', 'upper', ''),
	('vic-20_us_lower', 'VIC-20', '', 'lower', ''),
	('c64_us_upper', 'C64/TED/C128', '', 'upper', ''),
	('c64_us_lower', 'C64', '', 'lower', ''),
	('ted_us_lower', 'TED', '', 'lower', ''),
	('c128_us_lower', 'C128', '', 'lower', ''),
	('---', 'PET Style', '', '', ''),
	('pet_us_upper', 'PET', '', 'upper', ''),
	('pet_us_lower', 'PET', '', 'lower', ''),
	('pet_us_lower_swapped', 'PET', '', 'lower', 'swapped'),
	('vic-20_us_upper', 'VIC-20', '', 'upper', ''),
	('vic-20_us_lower', 'VIC-20', '', 'lower', ''),
	('---', 'PET Style Localized', '', '', ''),
	('vic-20_danish_upper', 'VIC-20', 'Danish', 'upper', ''),
	('vic-20_danish_lower', 'VIC-20', 'Danish', 'lower', ''),
	('c128_danish_upper', 'C128', 'Danish', 'upper', ''),
	('c128_danish_lower', 'C128', 'Danish', 'lower', ''),
	('pet_french_upper', 'PET', 'French', 'upper', ''),
	('pet_french_lower', 'PET', 'French', 'lower', ''),
	('c128_french_upper', 'C128', 'French', 'upper', ''),
	('c128_french_upper_alt', 'C128', 'French', 'upper', 'alt'),
	('c128_french_lower', 'C128', 'French', 'lower', ''),
	('c128_french_lower_alt', 'C128', 'French', 'lower', 'alt'),
	('pet_german_upper', 'PET', 'German', 'upper', ''),
	('pet_german_lower', 'PET', 'German', 'lower', ''),
	('pet_german_lower_alt', 'PET', 'German', 'lower', 'alt'),
	('pet_german_lower_alt2', 'PET', 'German', 'lower', 'alt'),
	('c128_german_upper', 'C128', 'German', 'upper', ''),
	('c128_german_lower', 'C128', 'German', 'lower', ''),
	('pet_greek_upper', 'PET', 'Greek', 'upper', ''),
	('pet_greek_lower', 'PET', 'Greek', 'lower', ''),
	('pet_hungarian_upper', 'PET', 'Hungarian', 'upper', ''),
	('pet_hungarian_lower', 'PET', 'Hungarian', 'lower', ''),
	('pet_japanese_upper', 'PET/VIC-20', 'Japanese', 'upper', ''),
	('pet_japanese_upper_bug', 'PET/VIC-20', 'Japanese', 'upper', 'bug'),
	('vic-20_japanese_upper-kanji', 'VIC-20', 'Japanese', 'upper-Kanji', ''),
	('c64_japanese_upper', 'C64', 'Japanese', 'upper', ''),
	('c64_japanese_upper-kanji', 'C64', 'Japanese', 'upper-Kanji', ''),
	('pet_norwegian_upper', 'PET', 'Norwegian', 'upper', ''),
	('pet_norwegian_lower', 'PET', 'Norwegian', 'lower', ''),
	('c128_norwegian_lower', 'C128', 'Norwegian', 'lower', ''),
	('c128_norwegian_lower_alt', 'C128', 'Norwegian', 'lower', 'alt'),
	('c128_norwegian_upper', 'C128', 'Norwegian', 'upper', ''),
	('c128_norwegian_upper_bugs', 'C128', 'Norwegian', 'upper', 'bugs'),
	('c128_norwegian_upper_alt', 'C128', 'Norwegian', 'upper', 'alt'),
	('c128_norwegian_upper_alt-bugs', 'C128', 'Norwegian', 'upper', 'alt-bugs'),
	('c128_norwegian_lower', 'C128', 'Norwegian', 'lower', ''),
	('c128_norwegian_lower_alt', 'C128', 'Norwegian', 'lower', 'alt'),
	('pet_russian_upper', 'PET', 'Russian', 'upper', ''),
	('c128_spanish_upper', 'C128', 'Spanish', 'upper', ''),
	('c128_spanish_upper_alt', 'C128', 'Spanish', 'upper', 'alt'),
	('c128_spanish_lower', 'C128', 'Spanish', 'lower', ''),
	('c128_spanish_lower_alt', 'C128', 'Spanish', 'lower', 'alt'),
	('pet_swedish_upper', 'PET/VIC-20', 'Swedish', 'upper', ''),
	('pet_swedish_lower', 'PET/VIC-20', 'Swedish', 'lower', ''),
	('vic-20_swedish_lower_alt', 'VIC-20', 'Swedish', 'lower', 'alt'),
	('c128_swiss_upper', 'C128', 'Swiss', 'upper', ''),
	('c128_swiss_upper_alt', 'C128', 'Swiss', 'upper', 'alt'),
	('c128_swiss_lower', 'C128', 'Swiss', 'lower', ''),
	('c128_swiss_lower_alt', 'C128', 'Swiss', 'lower', 'alt'),
	('---', 'C64 Style', '', '', ''),
	('c64_us_upper', 'C64/TED/C128', '', 'upper', ''),
	('c64_us_upper_alt', 'C64', '', 'upper', 'alt'),
	('c64_us_lower', 'C64', '', 'lower', ''),
	('c64_us_lower_alt', 'C64', '', 'lower', 'alt'),
	('ted_us_lower', 'TED', '', 'lower', ''),
	('c128_us_lower', 'C128', '', 'lower', ''),
	('---', 'C64 Style Localized', '', '', ''),
	('c64_danish_upper', 'C64', 'Danish', 'upper', ''),
	('c64_danish_upper_alt', 'C64', 'Danish', 'upper', 'alt'),
	('c64_danish_lower', 'C64', 'Danish', 'lower', ''),
	('c64_danish_lower_alt', 'C64', 'Danish', 'lower', 'alt'),
	('ted_hungarian_upper', 'TED', 'Hungarian', 'upper', ''),
	('ted_hungarian_lower', 'TED', 'Hungarian', 'lower', ''),
	('c64_spanish_upper', 'C64', 'Spanish', 'upper', ''),
	('c64_spanish_lower', 'C64', 'Spanish', 'lower', ''),
	('c64_swedish_upper', 'C64', 'Swedish', 'upper', ''),
	('c64_swedish_upper_bugs', 'C64', 'Swedish', 'upper', 'bugs'),
	('c64_swedish_upper_alt', 'C64', 'Swedish', 'upper', 'alt'),
	('c64_swedish_upper_alt2', 'C64', 'Swedish', 'upper', 'alt2'),
	('c64_swedish_lower', 'C64', 'Swedish', 'lower', ''),
	('c64_swedish_lower_alt', 'C64', 'Swedish', 'lower', 'alt'),
	('c64_swedish_lower_2', 'C64', 'Swedish', 'lower', '2'),
	('c64_swedish_lower_2alt', 'C64', 'Swedish', 'lower', '2alt'),
	('---', 'LCD Style', '', '', ''),
	('lcd_us_upper', 'LCD', '', 'upper', ''),
	('lcd_us_lower', 'LCD', '', 'lower', ''),
	('---', 'Other', '', '', ''),
	('superpet_us_ascii', 'SuperPET', '', 'ASCII', ''),
	('superpet_swedish_ascii', 'SuperPET', 'Swedish', 'ASCII', ''),
	('superpet_us_apl', 'SuperPET', '', 'APL', ''),
	('c64_turkish_upper', 'C64', 'Turkish', 'upper', ''),
	('c64_turkish_lower', 'C64', 'Turkish', 'lower', ''),
	('c64_us_upper_buggy1', 'C64', '', 'upper', 'buggy1'),
	('c64_us_upper_buggy2', 'C64', '', 'upper', 'buggy2'),
	('c64_us_lower_buggy1', 'C64', '', 'lower', 'buggy1'),
	('c64_us_lower_buggy1', 'C64', '', 'lower', 'buggy1'),
]

####################################################################

# MARK: HTML Helper

def html_header_css():

	print('<link rel="stylesheet" href="../style.css">')
	print('<link rel="stylesheet" href="style.css">')

	print('<style>')
	print('')

	for c in range(0, 256):
		x = c * -8
		print('    .char-{} {{ background-position:    {}px    0px; }}'.format(hex(c), x))

	for c in range(0, 16):
		x = 0
		y = c * -8
		print('    .char16-{} {{ background-position:    {}px    {}px; }}'.format(hex(c), x, y))

	print('')
	print('</style>')

def html_div_settings(id): #settings

	print('<div id="' + id + '">')

	html_div_selection_machine("machine_selection")
	html_div_selection_charset("charset_selection", charsets)
	print('    <div id="info_box"></div>')

	print('</div>')


def html_div_navigation(id): #navigation

	print('<input checked="checked" id="tab_screencode" type="radio" name="tabs" />')
	print('<input id="tab_petscii" type="radio" name="tabs" />')
	print('<input id="tab_keyboard" type="radio" name="tabs" />')

	print('<div id="' + id + '">')
	print('    <nav>')
	print('        <label for="tab_screencode">Character Set</label><!--')
	print('        --><label for="tab_petscii">PETSCII</label><!--')
	print('        --><label for="tab_keyboard">Keyboard</label><!-- -->')
	print('    </nav>')
	print('</div>')


def html_div_overview_screencode(id, css_class): # screencode_overview

	print('<div id="' + id + '" class="'+ css_class +'">')

	# Screen Code Table
	for scrcode in range(0, 256):
		print(pixel_char_html_from_scrcode(scrcode, link = 'scrcode_' + hex(scrcode)))
		if scrcode & 15 == 15:
			print('<br/>')

	print('</div>')


def html_div_overview_petscii(id, css_class): #petscii_overview

	print('<div id="' + id + '" class="'+ css_class +'">')

	# PETSCII Table
	for petscii in range(0, 256):
		scrcode = scrcode_from_petscii[petscii]
		description = None
		if not is_petscii_printable(petscii):
			description = ''
			for machine in machines:
				d = description_from_control_code[machine].get(petscii)
				if d:
					(d, _) = d
				if not d:
					d = ''

				if machine == 'C64':
					display = ''
				else:
					display = ' display: none;'

				symbol = symbol_from_control_code[machine][petscii]
				if symbol in color_index_from_color_name[machine]:
					hex_color = hex_color_from_color_index[machine][color_index_from_color_name[machine][symbol]]
					hex_color += 'A0'
				else:
					hex_color = '#00000080'

				d = '<div style="background-color: {}; border-color:{}; {}" class="control_codes control_codes_{}">{}</div>'.format(hex_color, hex_color[:-2], display, machine, d);
				description += d

		print(pixel_char_html_from_scrcode(scrcode, description, 'petscii_' + hex(petscii)))
		if petscii & 15 == 15:
			print('<br/>')

	print('</div>')
	
	
def html_div_overview_keyboard(id, css_class): #keyboard_overview
	
	print('<div id="' + id + '" class="'+ css_class +'">')

	for machine in machines:
		print(keyboard_layout_html(machine, keyboard_layout[machine]))

	print('</div>')
	
	
def html_div_selection_machine(id):

	print('<div id="' + id + '">')
	print('  <table class="checkbox_table">')

	for i in range(0, len(machines)):
		currentMachine = machines[i];
		deselection = list(machines);
		deselection.remove(currentMachine);
		
		print('    <tr>')
		print('        <td><input type="radio" name="radios"  id="radio_' + currentMachine + '" onclick="toggleMachine(\'' + currentMachine + '\', document.getElementById(\'radio_' + currentMachine + '\').checked, [\'{}\']);" /></td>'.format("','".join(deselection)))
		print('        <td><input class="machine_checkbox" type="checkbox" id="checkbox_' + currentMachine + '" onclick="toggleMachine(\'' + currentMachine + '\', document.getElementById(\'checkbox_' + currentMachine + '\').checked);" /></td>')
		print('        <td style="white-space: nowrap;"><b>' + machines[i] + '</b>')
		print('    </tr>')

	print('  </table>')

	selection = "','".join(list(machines))
	print(' <button type="button" onclick="checkMachines([\'{}\'], true)">All</button>'.format(selection))
	print(' <button type="button" onclick="checkMachines([\'{}\'], false)">None</button>'.format(selection))
	print('</div>')


def html_div_info_screencode(id):

	print('<div id="' + id + '">')

	# Screen Code Boxes
	for scrcode in range(0, 256):
		scrcode7 = scrcode & 0x7f
		is_reverse = scrcode >= 0x80
		petscii = petscii_from_scrcode[scrcode & 0x7f][0]

		print('<div id="info_scrcode_{}">'.format(hex(scrcode)))
		print('  <div class="grid-container">')

		print('    <div class="scrcode-image">')
		print(pixel_char_html_from_scrcode(scrcode))
		print('    </div>')
		print('    <div class="scrcode-title info-title">Screen Code</div>')
		print('    <div class="scrcode-description">')
		print('        ${:02X}<br/>'.format(scrcode))
		print('        {}'.format(scrcode))
		print('    </div>')

		for unicode_map in ['upper', 'lower']:
			display = ''
			if unicode_map != 'upper':
				display = ' style="display: none;"' # default shows upper

			unicode = unicode_from_petscii[unicode_map][petscii]
			print('    <div class="unicode-image unicode_{}"{}><span class="unicode-box">&#x{:x};</span></div>'.format(unicode_map, display, unicode))
			print('    <div class="unicode-title unicode_{} info-title"{}>Unicode</div>'.format(unicode_map, display))

			print('    <div class="unicode-description unicode_{}"{}>'.format(unicode_map, display))
			print('        U+{:04X}<br/>'.format(unicode))
			print('        {}'.format(description_from_unicode[unicode]))
			if is_reverse:
				print('        <br/>+ reverse')
			print('    </div>')

		print('    <div class="additional-info">')
		
		print('        <table>')
		print('            <tr><th colspan="2">PETSCII <th rowspan="2">Keyboard</th><th rowspan="2">Mode</th></tr>')
		print('            <tr><th>hex</th><th>dec</th></tr>')

		run = 0
		if is_reverse:
			scrcode_list = [scrcode7, scrcode]
		else:
			scrcode_list = [scrcode]
		for eff_scrcode in scrcode_list:
			for petscii in petscii_from_scrcode[eff_scrcode]:
				print('            <tr>')
				print('                <td><a href="#petscii_table_{:02x}">${:02X}</a></td><td>{}</td>'.format(petscii, petscii, petscii))

				print('                <td>')

				(all_keyboard_html, _) = all_keyboard_html_from_petscii(petscii, scrcode, False)
				print(all_keyboard_html)

				print('                </td>')
				print('                <td>')
				if run == 0:
					if is_reverse:
						print('                    reverse')
					else:
						print('                    plain')
				else:
					print('                    quote mode')
				print('                </td>')
				print('            </tr>')
			run += 1

		print('        </table>')
		print('    </div>')

		print('  </div>')
		print('</div>')

	print('</div>')


def html_div_info_petscii(id):

	print('<div id="' + id + '">')

	# PETSCII Boxes

	for petscii in range(0, 256):
		scrcode = scrcode_from_petscii[petscii]

		print('<div id="info_petscii_{}">'.format(hex(petscii)))
		print('  <div class="grid-container petscii_boxes">')

		print('    <div class="petscii-title info-title">PETSCII</div>')
		print('    <div class="petscii-description">')
		print('        <a href="#petscii_table_{:02x}">${:02X}</a><br/>'.format(petscii, petscii))
		print('        {}'.format(petscii))
		print('    </div>')

		print('    <div class="scrcode-image">')
		print(pixel_char_html_from_scrcode(scrcode))
		print('    </div>')
		print('    <div class="scrcode-title info-title">Screen Code</div>')
		print('    <div class="scrcode-description">')
		print('        ${:02X}<br/>'.format(scrcode))
		print('        {}'.format(scrcode))
		print('    </div>')

		if is_petscii_printable(petscii):
			for unicode_map in ['upper', 'lower']:
				display = ''
				if unicode_map != 'upper':
					display = ' style="display: none;"'
				unicode = unicode_from_petscii[unicode_map][petscii]
				print('    <div class="unicode-image unicode_{}"{}><span class="unicode-box">&#x{:x};</span></div>'.format(unicode_map, display, unicode))
				print('    <div class="unicode-title unicode_{} info-title"{}>Unicode</div>'.format(unicode_map, display))

				print('    <div class="unicode-description unicode_{}"{}>'.format(unicode_map, display))
				print('        U+{:04X}<br/>'.format(unicode))
				print('        {}'.format(description_from_unicode[unicode]))
				print('    </div>')

		else:
			description = combined_description_from_control_code(petscii)

			print('    <div class="control-title info-title">Control code</div>')
			print('    <div class="control-description">')
			print('        {}'.format(description))
			print('    </div>')
			
		print('    <div class="additional-info">')

		(all_keyboard_html, other_petscii) = all_keyboard_html_from_petscii(petscii, scrcode, other_ok = is_petscii_printable(petscii))

		print('        <div class="info-title">Keyboard')

		if other_petscii:
			print('            (alt code ${:02X})'.format(other_petscii))
		print('        </div>')

		print('        <div>')
		print(all_keyboard_html)
		print('        </div>')
		print('    </div>')

		print('  </div>')
		print('</div>');

	print('</div>')

def html_select_charset(id, default, onChange):
	html = ''
	html += '<select name="charset" id="{}" onChange="{}">'.format(id, onChange)
	seen_selected = False
	last_machine = ''
	for (filename, machine, locale, type, version) in charsets:
		if filename == '---':
			if last_machine != '':
				html += '    </optgroup>'
			last_machine = machine
			html += '    <optgroup label="{}">'.format(machine)

		else:
			if filename == default and not seen_selected:
				seen_selected = True
				selected = 'selected'
			else:
				selected = ''
			displayname = displayname_for_charset_details(machine, locale, type, version)
			html += '        <option value="bin/{}.bin" {}>{}</option>'.format(filename, selected, displayname)
	html += '    </optgroup>'
	html += '</select>'
	return html

def html_div_selection_charset(id, charsets):

	print('<div id="' + id + '">')

	print('<label for="charset">Character Set</label><br/>')
	print(html_select_charset('charset', 'c64_us_upper', 'charsetSwitch(this.options[this.selectedIndex].value);'))

#	print('')
#	print('<br/>')
#	print('')
#	print('<label for="unicode">Unicode Map</label><br/>')
#	print('<select name="unicode" id="unicode" onChange="unicodeSwitch(this.selectedIndex);">')
#	print('    <option value="us_upper">US Upper Case</option>')
#	print('    <option value="us_lower">US Lower Case</option>')
#	print('</select>')
	print('')
	print('<br/>')
	print('')
	print('<label for="controlcodes">Control Codes</label><br/>')
	print('<select name="controlcodes" id="controlcodes" onChange="controlcodesSwitch(this.options[this.selectedIndex].value);">')
	for machine in machines:
		print('    <option value="{}">{}</option>'.format(machine, machine))
	print('</select>')
	print('')
	print('<br/>')
	print('')
	print('<label for="color_set">Color Scheme</label><br/>')
	print('<select name="color_set" id="color_set" onChange="colorsetSwitch(this.selectedIndex);">')
	print('    <option value="colorset_1">Black on White</option>')
	print('    <option value="colorset_2">PET</option>')
	print('    <option value="colorset_3">VIC-20</option>')
	print('    <option value="colorset_4">C64</option>')
	print('    <option value="colorset_5">C128</option>')
	print('    <option value="colorset_6">C65</option>')
	print('    <option value="colorset_7">TED</option>')
	print('</select>')
	print('')
	print('<br/>')
	print('')
	print('<label for="aspectratio">Aspect Ratio</label><br/>')
	print('<select name="aspectratio" id="aspectratio" onChange="aspectratioSwitch(this.selectedIndex);">')
	print('    <option value="aspectratio_1">Square</option>')
	print('    <option value="aspectratio_2">0.955:1 (C64 PAL)</option>')
	print('    <option value="aspectratio_3">0.75:1 (C64 NTSC)</option>')
	print('    <option value="aspectratio_5">1:2 (C128 VDC)</option>')
	print('    <option value="aspectratio_4">2:1 (VIC-20)</option>')
	print('</select>')

	print('</div>')


def html_div_table_charset_compare(id, css_class, charsets): #charset_compare_table_div

	print('<div id="' + id + '" class="'+ css_class +'">')

	print('<table>')

	charset1 = 'c64_us_lower'
	charset2 = 'ted_us_lower'
	for i in range(0, 3):
		print('    <tr>')

		if i == 0 or i == 2:
			print('        <td>')
			if i == 0:
				filename = charset1
				cmpindex = 0
			else:
				filename = charset2
				cmpindex = 1
			print(html_select_charset('charset_compare_select' + str(i), filename, 'charsetCompareSwitch({}, this.options[this.selectedIndex].value);'.format(cmpindex)))
			print('        </td>')
			print('        <td>')
			print('        <div class="char-box128"><div class="char-img128 charset_cmp_{}" id="bin/{}.bin"></div></div>'.format(cmpindex, filename))
			print('        </td>')
		else:
			print('        <td style="float: right; font-size: smaller;">XOR</td>')
			print('        <td>')
			print('        <div class="char-box128"><div class="char-img128" id="charset_cmp"></div></div>')
			print('        </td>')

		print('    </tr>')
	print('</table>')
	print('</div>')


def html_div_table_charset(id, css_class, charsets): #charset_table_div

	print('<div id="' + id + '" class="'+ css_class +'">')

	print('<label for="case">Filter: </label>')
	print('<select name="case" id="case" onChange="caseSwitch(this.selectedIndex);">')
	print('    <option value="all">All</option>')
	print('    <option value="upper">Upper Case</option>')
	print('    <option value="lower">Lower Case</option>')
	print('</select>')

	print('<table>')

	for (filename, machine, locale, type, version) in charsets:
		if filename == '---':
			print('    <tr>')
			print('        <td colspan="2" class="header">')
			print('            {}'.format(machine))
			print('        </td>')
			print('    </tr>')
		else:
			if 'upper' in type:
				case = 'table_upper'
			else:
				case = 'table_lower'
			print('    <tr class="{}">'.format(case))
			print('        <td>')
			print(displayname_for_charset_details(machine, locale, type, version))
			print('<span style="float: right;"><a href="bin/{}.bin">.bin</a></span>'.format(filename))
			print('        </td>')
			print('        <td>')
			print('        <div class="char-box128"><div class="char-img128" id="bin/{}.bin"></div></div>'.format(filename))
			print('        </td>')
			print('    </tr>')

	print('</table>')
	print('</div>')


def html_div_table_petscii(id, css_class): #petscii_table_div

	print('<div id="' + id + '" class="'+ css_class +'">')

	print('<label for="petscii_show">Show: </label>')
	print('<select name="petscii_show" id="petscii_show" onChange="petsciiTableSwitch(this.selectedIndex);">')
	print('    <option value="petscii_keyboard">Keyboard</option>')
	print('    <option value="petscii_control">Control Codes</option>')
	print('    <option value="petscii_both" selected>Both</option>')
	print('</select>')

	# PETSCII Table

	print('<table>')

	print('    <tr>')
	print('        <th>PETSCII</th>')
	print('        <th>Screen Code</th>')
	print('        <th>Char</th>')
	print('        <th colspan="3" class="unicode_upper">Unicode Upper</th>')
	print('        <th colspan="3" class="unicode_lower" style="display: none;">Unicode Lower</th>')
	i = 0
	for machine in machines:
		print('        <th class="petscii_keyboard {}" style="background: var(--title-color-{})">{}<br/>Keyboard</th>'.format(machine, i+1, machine))
		i += 1
	i = 0
	for machine in machines:
		print('        <th class="petscii_control {}" style="background: var(--title-color-{})">{}<br/>Control Code</th>'.format(machine, i+1, machine))
		i += 1
	print('    </tr>')

	for petscii in range(0, 256):
		print('    <tr>')

		print('        <td><a id="petscii_table_{:02x}">${:02X}</a></td>'.format(petscii, petscii))
		
		scrcode = scrcode_from_petscii[petscii]

		print('        <td>${:02X}</td>'.format(scrcode))
		print('        <td>{}</td>'.format(pixel_char_html_from_scrcode(scrcode)))

		if is_petscii_printable(petscii):
			unicode = unicode_from_petscii['upper'][petscii]
			print('        <td class="unicode_upper"><span class="unicode-box">&#x{:x};</span></td>'.format(unicode))
			print('        <td class="unicode_upper">U+{:04X}</td>'.format(unicode))
			print('        <td class="unicode_upper">{}</td>'.format(description_from_unicode[unicode]))

			unicode = unicode_from_petscii['lower'][petscii]
			print('        <td class="unicode_lower" style="display: none;"><span class="unicode-box">&#x{:x};</span></td>'.format(unicode))
			print('        <td class="unicode_lower" style="display: none;">U+{:04X}</td>'.format(unicode))
			print('        <td class="unicode_lower" style="display: none;">{}</td>'.format(description_from_unicode[unicode]))
		else:
			print('        <td colspan="3" class="unicode_upper"></td>')
			print('        <td colspan="3" class="unicode_lower" style="display: none;"></td>')

		# Keyboard
		i = 0
		for machine in machines:
			print('        <td class="petscii_keyboard {}" style="background: var(--light-color-{})">'.format(machine, i+1))
			(modifiers_and_scancodes_html, other_petscii) = modifiers_and_scancodes_html_from_petscii(petscii, scrcode, True, machine)
			if len(modifiers_and_scancodes_html) > 0:
				if not other_petscii:
					for html in modifiers_and_scancodes_html:
						print('            {}'.format(html))
			print('        </td>')
			i += 1


		if is_petscii_printable(petscii):
			print('        <td colspan="{}"></td>'.format(len(machines)))

		else:
			i = 0
			for machine in machines:
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
				print('        <td class="petscii_control {}" style="background: var(--light-color-{})">{}</td>'.format(machine, i+1, description))
				i += 1

		print('    </tr>')

	print('</table>')
	print('</div>')

####################################################################


# MARK: HTML Writer


print('<!DOCTYPE html>')
print('<html lang="en-US">')
print('<head>')
print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<title>Charset · PETSCII · Keyboard | Ultimate C64 Reference</title>')
print('')
print('<script src="script.js"></script>')
print('<script src="charset.js"></script>')

print('')

html_header_css()

print('</head>')

print('<body>')

# http://tholman.com/github-corners/
print('<a href="https://github.com/mist64/c64ref" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:var(--main-color); color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a>')

print('<div class="topnav">')
print('    <h1>Ultimate Commodore 64 Reference</h1> ')
print('    <a href="../6502/">6502</a>')
print('    <a href="../kernal/">KERNAL API</a>')
print('    <a href="../c64disasm/">ROM Disassembly</a>')
print('    <a href="../c64mem/">Memory Map</a>')
print('    <a class="active" href="#">Charset · PETSCII · Keyboard</a>')
#print('    <a  href="../c64io/">I/O Map</a>')
print('    <a class="home" href="https://www.pagetable.com/">pagetable.com</a>')
print('</div>')

print('<div class="main">')
print('<h1>Character Set · PETSCII · Keyboard</h1>')

f = os.popen('git log -1 --pretty=format:%h .')
revision = f.read()
f = os.popen('git log -1 --date=short --pretty=format:%cd .')
date = f.read()
print('<p><i>by <a href="http://www.pagetable.com/">Michael Steil</a>, Lisa Brodner, <a href="https://github.com/mist64/c64ref">github.com/mist64/c64ref</a>. Revision ' + revision + ', ' + date + '</i></p>')

print('</div>')
print('<div class="tabbed">')

html_div_settings("settings")

html_div_navigation("navigation")

# Screen Codes and Character Sets

html_div_overview_screencode("screencode_overview", "screencode_group")
html_div_overview_petscii("petscii_overview", "petscii_group")
html_div_overview_keyboard("keyboard_overview", "keyboard_group")

html_div_table_charset_compare("charset_compare_table_div", "screencode_group", charsets)
html_div_table_charset("charset_table_div", "screencode_group", charsets)
html_div_table_petscii("petscii_table_div", "petscii_group")

print('</div>')#tabbed

print('<div style="display: none">')
html_div_info_screencode("screencode_boxes")
html_div_info_petscii("petscii_boxes")
print('</div>');

print('<hr/>')

print('<div class="main">')

print('<h2>Notes<a id="notes"></a></h2>')
print('<ul>')
print('<li>')
print('PET-N is a PET with a ROM version below 4 (i.e. base set of control codes) and a "normal" (chicklet or graphics) keyboard. PET-B is a PET 8xxx with a ROM version of 4 (i.e. extended set of control codes) and a business keyboard. The graphics keyboard also existed for the later PETs, and early PETs could be upgraded with newer ROMs, but for the sake of simplicity, I limitied the PET series to these two systems.')
print('</li>')
print('<li>')
print('The colors in the C128 control codes are the VDC ones. In VIC-II mode, the colors match the C64 ones.')
print('</li>')
print('<li>')
print('The character sets have been taken from <a href="http://www.zimmers.net/anonftp/pub/cbm/firmware/characters/">zimmers.net</a> and <a href="http://www.6502.org/users/sjgray/computer/cbmchr/cbmchr.html">sjgray\'s page</a>. Each ROM image has been split into individual character sets, reverse versions have been normalized, and duplicates have been eliminated. See the "compare.py" script in the repository for details.')
print('</li>')
print('<li>')
print('The regular and reverse versions of the C64 system characater sets differ in the \'@\' symbol, and some other machines have various differences and sometimes bugs (flipped bits) in their copies. For simplicity, the viewer is using a single variant for both regular and reverse. You can select the alternative/buggy version in the charset picker.')
print('</li>')
print('<li>')
print('The PETSCII to Unicode conversion is done using the mappings from the <a href="https://en.wikipedia.org/wiki/Symbols_for_Legacy_Computing">Symbols for Legacy Computing</a> additions to Unicode; <a href="https://www.unicode.org/L2/L2019/19025-aux-mappings.zip">19025-aux-mappings.zip</a>. As of mid 2020, common operating systems don\'t support all symbls yet.')
print('</li>')
print('<li>')
print('Note that some keyboard keys (VIC-20/C64/C128/C65: <span class="key-box">RESTORE</span>, C128/C65: <span class="key-box">CAPS LOCK</span>, C128: <span class="key-box">40/80 DISPLAY</span>) produce no scancode, and therefore no PETSCII code. Other keys (C128/C65: <span class="key-box">NO SCROLL</span>) produce a scancode, but no PETSCII code.')
print('</li>')
print('</ul>')

print('</div>')
print('</body>')
print('</html>')

