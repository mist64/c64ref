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

def all_keyboard_html_from_petscii(petscii, other_ok = False):
	all_keyboard_html = ''
	for machine in machines:
		all_keyboard_html += '<div class="{}"><b>{}</b>:'.format(machine, machine)
		(modifiers_and_scancodes_html, other_petscii) = modifiers_and_scancodes_html_from_petscii(petscii, machine)
		if len(modifiers_and_scancodes_html) > 0:
			if other_ok or not other_petscii:
				for html in modifiers_and_scancodes_html:
					all_keyboard_html += '{}<br/>'.format(html)
			else:
				all_keyboard_html += ' -'
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
		description_to_machines['no function'] = machines_without_function


	combined_description = ''
	for description in description_to_machines.keys():
		if len(description_to_machines[description]) != len(machines):
			machines_string = '<b>' + '/'.join(description_to_machines[description]) + '</b>: '
		else:
			machines_string = ''
		combined_description += machines_string + description + '<br/>'
	return combined_description


def pixel_char_html_from_scrcode(scrcode, description = None, hex_color = None, link = None):
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

	link_html1 = ''
	link_html2 = ''
	if link:
		link_html1 = ' onclick="test(\'{}\')"'.format(link)
		link_html2 = ' id="{}"'.format(link)

	return '<div class="char-box {}"{}{}><span class="char-img char-{}"></span>{}</div>'.format(inverted, link_html2, link_html1, hex(scrcode7), description_html)

####################################################################

machines = ['PET', 'VIC-20', 'C64', 'C128', 'C65', 'TED']
#machines.append('CBM2')

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
	'DIS_CASE_SWITCH':  ('Lock Case', 'Disable Case-Switching Keys'),
	'DIS_MODE_SWITCH':  ('Lock Mode', 'Disable Mode Switch'),
	'ENA_CASE_SWITCH':  ('Unlock Case', 'Enable Case-Switching Keys'),
	'ENA_MODE_SWITCH':  ('Unlock Mode', 'Enable Mode Switch'),
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
	'KEY_F9':           ('f9', 'f9 key'),
	'KEY_F10':          ('f10', 'f10 key'),
	'KEY_F11':          ('f11', 'f11 key'),
	'KEY_F12':          ('f12', 'f12 key'),
	'KEY_F13':          ('f13', 'f13 key'),
	'KEY_F14':          ('f14', 'f14 key'),
	'LINE_FEED':        ('LF', 'Line Feed'),
	'LOWER_CASE':       ('Lower Case', 'Switch to lower case'),
	'RETURN':           ('RETURN', 'Return'),
	'RUN':              ('RUN', 'RUN'),
	'RVS_OFF':          ('RVS Off', 'Reverse Off'),
	'RVS_ON':           ('RVS On', 'Reverse On'),
	'SHIFT_RETURN':     ('SHIFT RETURN', 'Disabled Return'),
	'STOP':             ('STOP', 'STOP'),
	'TAB_SET_CLR':      ('Tab set/clr', 'Tab set/clear'),
	'UNDERLINE_OFF':    ('Underline Off', 'Underline Off'),
	'UNDERLINE_ON':     ('Underline On', 'Underline On'),
	'UPPER_CASE':       ('Upper Case', 'Switch to upper case'),
	'BELL_TONE': ('BEL', 'Bell Tone'),
	'TAB': ('TAB', 'Forward TAB'),
	'HELP': ('HELP', 'HELP'),
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
			values = [d.replace('HASH', '#') for d in values]
			description_from_scancode[machine].extend(values)
		elif key == 'exclude':
			values = [int(v, 16) for v in values]
			excluded_scancodes[machine].extend(values)
		else:
			values = [int(v, 16) for v in values]
			petscii_from_scancode[machine][key].extend(values)

####################################################################

print('<!DOCTYPE html>')
print('<html lang="en-US">')
print('<head>')
print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<title>Character Set | Ultimate C64 Reference</title>')
print('')
print('<script src="script.js"></script>')
print('')
print('<link rel="stylesheet" href="../style.css">')
print('<link rel="stylesheet" href="style.css">')
print('<style>')
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

print('<div class="tabbed">')
print('')
print('   <input checked="checked" id="tab_screencode" type="radio" name="tabs" />')
print('   <input id="tab_petscii" type="radio" name="tabs" />')
print('')
print('   <nav>')
print('      <label for="tab_screencode">Screencodes</label>')
print('      <label for="tab_petscii">PETSCII</label>')
print('   </nav>')
print('')
print('   <figure>')
print('      <div id="screencode_overview">')

# Screencode Table
for scrcode in range(0, 256):
	print(pixel_char_html_from_scrcode(scrcode, link = 'scrcode_' + hex(scrcode)))
	if scrcode & 15 == 15:
		print('<br />')


print('      </div>')
print('')
print('      <div id="petscii_overview">')



machine = 'TED'

# PETSCII Table
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
		if symbol in color_index_from_color_name[machine]:
			hex_color = hex_color_from_color_index[machine][color_index_from_color_name[machine][symbol]]
	print(pixel_char_html_from_scrcode(scrcode, description, hex_color, 'petscii_' + hex(petscii)))
	if petscii & 15 == 15:
		print('<br />')


print('      </div>')
print('   </figure>')

print('</div>')

print('<div id="info_box"></div>')

print('</div>')

print('<table class="checkbox_table">')
for i in range(0, len(machines)):
	currentMachine = machines[i];
	deselection = list(machines);
	deselection.remove(currentMachine);
	
	print('<tr>')
	print(' <td><input type="radio" name="radios"  id="radio_' + currentMachine + '" onclick="toggleMachine(\'' + currentMachine + '\', document.getElementById(\'radio_' + currentMachine + '\').checked, [\'{}\']);" /></td>'.format("','".join(deselection)))
	print(' <td><input type="checkbox" id="checkbox_' + currentMachine + '" checked onclick="toggleMachine(\'' + currentMachine + '\', document.getElementById(\'checkbox_' + currentMachine + '\').checked);" /></td>')
	print(' <td style="white-space: nowrap;"><b>' + machines[i] + '</b>')
	print('</tr>')
print('</table>')

print('<div style="display: none">')

# Screencode Boxes
print('<div id="screencode_boxes">')

for scrcode in range(0, 256):
	scrcode7 = scrcode & 0x7f
	is_reverse = scrcode >= 0x80
	petscii = petscii_from_scrcode[scrcode & 0x7f][0]

	print('<div id="info_scrcode_{}">'.format(hex(scrcode)))
	print(' <div class="grid-container">')

	print('  <div class="scrcode-image">')
	print(pixel_char_html_from_scrcode(scrcode))
	print('  </div>')
	print('  <div class="scrcode-title info-title">Screencode</div>')
	print('  <div class="scrcode-description">')
	print('${:02X}<br/>'.format(scrcode))
	print('{}'.format(scrcode))
	print('  </div>')

	for unicode_map in ['upper', 'lower']:
		display = ''
		if unicode_map != 'upper':
			display = ' style="display: none;"'
		print('<div class="unicode_{}" {}>'.format(unicode_map, display))
		unicode = unicode_from_petscii[unicode_map][petscii]
		print('  <div class="unicode-image"><span class="unicode-box">&#x{:x};</span></div>'.format(unicode))
		print('  <div class="unicode-title info-title">Unicode</div>')

		print('  <div class="unicode-description">')
		print('   U+{:04X}<br/>'.format(unicode))
		print('   {}'.format(description_from_unicode[unicode]))
		if is_reverse:
			print('   <br/>+ reverse')
		print('  </div>')
		print('</div>')

	print('  <div class="additional-info">')
	
	print('   <table>')
	print('    <tr><th colspan="2">PETSCII <th rowspan="2">Keyboard</th><th rowspan="2">Mode</th></tr>')
	print('    <tr><th>hex</th><th>dec</th></tr>')

	run = 0
	if is_reverse:
		scrcode_list = [scrcode7, scrcode]
	else:
		scrcode_list = [scrcode]
	for eff_scrcode in scrcode_list:
		for petscii in petscii_from_scrcode[eff_scrcode]:
			print('    <tr>')
			print('     <td><a href="#petscii_table_{:02x}">${:02X}</a></td><td>{}</td>'.format(petscii, petscii, petscii))

			print('     <td>')

			(all_keyboard_html, _) = all_keyboard_html_from_petscii(petscii, False)
			print(all_keyboard_html)

			print('     </td>')
			print('     <td>')
			if run == 0:
				if is_reverse:
					print('reverse')
				else:
					print('plain')
			else:
				print('quote mode')
			print('     </td>')

			print('    </tr>')
		run += 1

	print('   </table>')
	print('  </div>')
	print(' </div>')
	print('</div>')

print('</div>')


# PETSCII Boxes
print('<div id="petscii_boxes">')

for petscii in range(0, 256):
	scrcode = scrcode_from_petscii[petscii]

	print('<div id="info_petscii_{}">'.format(hex(petscii)))
	print(' <div class="grid-container petscii_boxes">')

	print('  <div class="petscii-title info-title">PETSCII</div>')
	print('  <div class="petscii-description">')
	print('   <a href="#petscii_table_{:02x}">${:02X}</a><br/>'.format(petscii, petscii))
	print('   {}'.format(petscii))
	print('  </div>')

	print('  <div class="scrcode-image">')
	print(pixel_char_html_from_scrcode(scrcode))
	print('  </div>')
	print('  <div class="scrcode-title info-title">Screencode</div>')
	print('  <div class="scrcode-description">')
	print('   ${:02X}'.format(scrcode))
	print('   {}'.format(scrcode))
	print('  </div>')

	if is_petscii_printable(petscii):
		for unicode_map in ['upper', 'lower']:
			display = ''
			if unicode_map != 'upper':
				display = ' style="display: none;"'
			print('<div class="unicode_{}" {}>'.format(unicode_map, display))
			unicode = unicode_from_petscii[unicode_map][petscii]
			print('  <div class="unicode-image"><span class="unicode-box">&#x{:x};</span></div>'.format(unicode))
			print('  <div class="unicode-title info-title">Unicode</div>')

			print('  <div class="unicode-description">')
			print('   U+{:04X}<br/>'.format(unicode))
			print('   {}'.format(description_from_unicode[unicode]))
			print('  </div>')
			print('</div>')

	else:
		description = combined_description_from_control_code(petscii)

		print('  <div class="control-title info-title">Control code</div>')

		print('  <div class="control-description">')
		print('   {}'.format(description))
		print('  </div>')
		
	print('  <div class="additional-info">')

	(all_keyboard_html, other_petscii) = all_keyboard_html_from_petscii(petscii, is_petscii_printable(petscii))

	print('   <div><span class="info-title">')
	print('    Keyboard</span>')
	if other_petscii:
		print('    (alt code ${:02X})<br/>'.format(other_petscii))
	print('    </div>')

	print('    <div>')
	print(all_keyboard_html)
	print('   </div>')

	print('  </div>')

	print(' </div>')
	print('</div>');

print('</div>');
print('</div>');


charsets = [
	('c64_us_upper.png', 'C64/C16/C128', '', 'upper', ''),
	('c64_us_lower.png', 'C64', '', 'lower', ''),
	('---', 'PET Style', '', '', ''),
	('pet_us_upper.png', 'PET', '', 'upper', ''),
	('pet_us_lower.png', 'PET', '', 'lower', ''),
	('pet_us_lower_swapped.png', 'PET', '', 'lower', 'swapped'),
	('vic-20_us_upper.png', 'VIC-20', '', 'upper', ''),
	('vic-20_us_lower.png', 'VIC-20', '', 'lower', ''),
	('---', 'C64 Style', '', '', ''),
	('c64_us_upper.png', 'C64/C16/C128', '', 'upper', ''),
	('c64_us_upper_alt.png', 'C64', '', 'upper', 'alt'),
	('c64_us_lower.png', 'C64', '', 'lower', ''),
	('c64_us_lower_alt.png', 'C64', '', 'lower', 'alt'),
	('c16_us_lower.png', 'C16', '', 'lower', ''),
	('c128_us_lower.png', 'C128', '', 'lower', ''),
	('---', 'LCD Style', '', '', ''),
	('lcd_us_upper.png', 'LCD', '', 'upper', ''),
	('lcd_us_lower.png', 'LCD', '', 'lower', ''),
	('---', 'PET Style Localized', '', '', ''),
	('vic-20_danish_upper.png', 'VIC-20', 'Danish', 'upper', ''),
	('vic-20_danish_lower.png', 'VIC-20', 'Danish', 'lower', ''),
	('c128_danish_upper.png', 'C128', 'Danish', 'upper', ''),
	('c128_danish_lower.png', 'C128', 'Danish', 'lower', ''),
	('pet_french_upper.png', 'PET', 'French', 'upper', ''),
	('c128_french_upper.png', 'C128', 'French', 'upper', ''),
	('c128_french_upper_alt.png', 'C128', 'French', 'upper', 'alt'),
	('c128_french_lower.png', 'C128', 'French', 'lower', ''),
	('c128_french_lower_alt.png', 'C128', 'French', 'lower', 'alt'),
	('pet_french_lower.png', 'PET', 'French', 'lower', ''),
	('pet_german_upper.png', 'PET', 'German', 'upper', ''),
	('pet_german_lower.png', 'PET', 'German', 'lower', ''),
	('pet_german_lower_alt.png', 'PET', 'German', 'lower', 'alt'),
	('pet_german_lower_alt.png', 'PET', 'German', 'lower', 'alt'),
	('c128_german_upper.png', 'C128', 'German', 'upper', ''),
	('c128_german_lower.png', 'C128', 'German', 'lower', ''),
	('pet_greek_upper.png', 'PET', 'Greek', 'upper', ''),
	('pet_greek_lower.png', 'PET', 'Greek', 'lower', ''),
	('pet_hungarian_upper.png', 'PET', 'Hungarian', 'upper', ''),
	('pet_hungarian_lower.png', 'PET', 'Hungarian', 'lower', ''),
	('pet_japanese_upper.png', 'PET/VIC-20', 'Japanese', 'upper', ''),
	('pet_japanese_upper_bug.png', 'PET/VIC-20', 'Japanese', 'upper', 'bug'),
	('vic-20_japanese_upper-kanji.png', 'VIC-20', 'Japanese', 'upper-Kanji', ''),
	('pet_norwegian_upper.png', 'PET', 'Norwegian', 'upper', ''),
	('pet_norwegian_lower.png', 'PET', 'Norwegian', 'lower', ''),
	('c128_norwegian_lower.png', 'C128', 'Norwegian', 'lower', ''),
	('c128_norwegian_lower_alt.png', 'C128', 'Norwegian', 'lower', 'alt'),
	('c128_norwegian_upper.png', 'C128', 'Norwegian', 'upper', ''),
	('c128_norwegian_upper_bugs.png', 'C128', 'Norwegian', 'upper', 'bugs'),
	('c128_norwegian_upper_alt.png', 'C128', 'Norwegian', 'upper', 'alt'),
	('c128_norwegian_upper_alt-bugs.png', 'C128', 'Norwegian', 'upper', 'alt-bugs'),
	('c128_norwegian_lower.png', 'C128', 'Norwegian', 'lower', ''),
	('c128_norwegian_lower_alt.png', 'C128', 'Norwegian', 'lower', 'alt'),
	('pet_russian_upper.png', 'PET', 'Russian', 'upper', ''),
	('c128_spanish_upper.png', 'C128', 'Spanish', 'upper', ''),
	('c128_spanish_upper_alt.png', 'C128', 'Spanish', 'upper', 'alt'),
	('c128_spanish_lower.png', 'C128', 'Spanish', 'lower', ''),
	('c128_spanish_lower_alt.png', 'C128', 'Spanish', 'lower', 'alt'),
	('pet_swedish_upper.png', 'PET/VIC-20', 'Swedish', 'upper', ''),
	('pet_swedish_lower.png', 'PET/VIC-20', 'Swedish', 'lower', ''),
	('vic-20_swedish_lower_alt.png', 'VIC-20', 'Swedish', 'lower', 'alt'),
	('c128_swiss_upper.png', 'C128', 'Swiss', 'upper', ''),
	('c128_swiss_upper_alt.png', 'C128', 'Swiss', 'upper', 'alt'),
	('c128_swiss_lower.png', 'C128', 'Swiss', 'lower', ''),
	('c128_swiss_lower_alt.png', 'C128', 'Swiss', 'lower', 'alt'),
	('---', 'C64 Style Localized', '', '', ''),
	('c64_danish_upper.png', 'C64', 'Danish', 'upper', ''),
	('c64_danish_upper_alt.png', 'C64', 'Danish', 'upper', 'alt'),
	('c64_danish_lower.png', 'C64', 'Danish', 'lower', ''),
	('c64_danish_lower_alt.png', 'C64', 'Danish', 'lower', 'alt'),
	('c16_hungarian_upper.png', 'C16', 'Hungarian', 'upper', ''),
	('c16_hungarian_lower.png', 'C16', 'Hungarian', 'lower', ''),
	('c64_spanish_upper.png', 'C64', 'Spanish', 'upper', ''),
	('c64_spanish_lower.png', 'C64', 'Spanish', 'lower', ''),
	('c64_swedish_upper.png', 'C64', 'Swedish', 'upper', ''),
	('c64_swedish_upper_bugs.png', 'C64', 'Swedish', 'upper', 'bugs'),
	('c64_swedish_upper_alt.png', 'C64', 'Swedish', 'upper', 'alt'),
	('c64_swedish_upper_alt2.png', 'C64', 'Swedish', 'upper', 'alt2'),
	('c64_swedish_lower.png', 'C64', 'Swedish', 'lower', ''),
	('c64_swedish_lower_alt.png', 'C64', 'Swedish', 'lower', 'alt'),
	('c64_swedish_lower_2.png', 'C64', 'Swedish', 'lower', '2'),
	('c64_swedish_lower_2alt.png', 'C64', 'Swedish', 'lower', '2alt'),
	('---', 'PET Other', '', '', ''),
	('superpet_us_ascii.png', 'SuperPET', '', 'ASCII', ''),
	('superpet_swedish_ascii.png', 'SuperPET', 'Swedish', 'ASCII', ''),
	('superpet_us_apl.png', 'SuperPET', '', 'APL', ''),
	('---', 'Other', '', '', ''),
	('c64_japanese_upper.png', 'C64', 'Japanese', 'upper', ''),
	('c64_japanese_upper-kanji.png', 'C64', 'Japanese', 'upper-Kanji', ''),
	('c64_turkish_upper.png', 'C64', 'Turkish', 'upper', ''),
	('c64_turkish_lower.png', 'C64', 'Turkish', 'lower', ''),
	('c64_us_upper_buggy1.png', 'C64', '', 'upper', 'buggy1'),
	('c64_us_upper_buggy2.png', 'C64', '', 'upper', 'buggy2'),
	('c64_us_lower_buggy1.png', 'C64', '', 'lower', 'buggy1'),
	('c64_us_lower_buggy1.png', 'C64', '', 'lower', 'buggy1'),
]

print('<label for="charset">Character Set</label>')
print('<select name="charset" id="charset" onChange="charsetSwitch(this.options[this.selectedIndex].value);">')
seen_selected = False
for (filename, machine, locale, type, version) in charsets:
	if filename == '---':
		print('  <option disabled>------------------------------</option>')
		print('  <option disabled>{}</option>'.format(machine))
		print('  <option disabled>------------------------------</option>')
	else:
		if locale == '':
			locale = 'US'
		if filename == 'c64_us_upper.png' and not seen_selected:
			seen_selected = True
			selected = 'selected'
		else:
			selected = ''
		print('  <option value="png/{}" {}>{} {} {} ({})</option>'.format(filename, selected, locale, type, version, machine))
print('</select>')
print('<br/>')
print('<label for="unicode">Unicode Map</label>')
print('<select name="unicode" id="unicode" onChange="unicodeSwitch(this.selectedIndex);">')
print('  <option value="us_upper">US Upper Case</option>')
print('  <option value="us_lower">US Lower Case</option>')
print('</select>')


# PETSCII Table
print('<table border="1">')
print('<tr>')
print('<th>PETSCII</th>')
print('<th>Screen Code</th>')
print('<th>Char</th>')
print('<th colspan="3" class="unicode_upper">Unicode Upper</th>')
print('<th colspan="3" class="unicode_lower" style="display: none;">Unicode Lower</th>')
i = 0
for machine in machines:
	print('<th class="{}" style="background: var(--title-color-{})">{}<br/>Keyboard</th>'.format(machine, i+1, machine))
	i += 1
i = 0
for machine in machines:
	print('<th class="{}" style="background: var(--title-color-{})">{}<br/>Control Code</th>'.format(machine, i+1, machine))
	i += 1
print('</tr>')
for petscii in range(0, 256):
	print('<tr>')

	print('<td><a id="petscii_table_{:02x}">${:02X}</a></td>'.format(petscii, petscii))
    
	scrcode = scrcode_from_petscii[petscii]

	print('<td>${:02X}</td>'.format(scrcode))

	print('<td>{}</td>'.format(pixel_char_html_from_scrcode(scrcode)))

	if is_petscii_printable(petscii):
		unicode = unicode_from_petscii['upper'][petscii]
		print('<td class="unicode_upper"><span class="unicode-box">&#x{:x};</span></td>'.format(unicode))
		print('<td class="unicode_upper">U+{:04X}</td>'.format(unicode))
		print('<td class="unicode_upper">{}</td>'.format(description_from_unicode[unicode]))

		unicode = unicode_from_petscii['lower'][petscii]
		print('<td class="unicode_lower" style="display: none;"><span class="unicode-box">&#x{:x};</span></td>'.format(unicode))
		print('<td class="unicode_lower" style="display: none;">U+{:04X}</td>'.format(unicode))
		print('<td class="unicode_lower" style="display: none;">{}</td>'.format(description_from_unicode[unicode]))
	else:
		print('<td colspan="3"></td>')

	# keyboard
	i = 0
	for machine in machines:
		print('<td class="{}" style="background: var(--light-color-{})">'.format(machine, i+1))
		(modifiers_and_scancodes_html, other_petscii) = modifiers_and_scancodes_html_from_petscii(petscii, machine)
		if len(modifiers_and_scancodes_html) > 0:
			if not other_petscii:
				for html in modifiers_and_scancodes_html:
					print('{}<br/>'.format(html))
		print('</td>')
		i += 1


	if is_petscii_printable(petscii):
		print('<td colspan="{}"></td>'.format(len(machines)))

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
			print('<td class="{}" style="background: var(--light-color-{})">{}</td>'.format(machine, i+1, description))
			i += 1



	print('</tr>')

print('</table>')

print('</body>')
print('</html>')

