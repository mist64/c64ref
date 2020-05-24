#!/usr/bin/python3


scale = 4 # character scale up factor
side = 8 # character width/height 8px

# generate scrcode_from_petscii mapping
scrcode_from_petscii = []
for c in range(0, 256):
	if c < 0x20:
		d = None
	elif c < 0x40:
		d = c
	elif c < 0x60:
		d = c - 0x40
	elif c < 0x80:
		d = c - 0x20
	elif c < 0xa0:
		d = None
	elif c < 0xc0:
		d = c - 0x40
	else:
		d = c - 0x80
	scrcode_from_petscii.append(d)

# generate petscii_from_scrcode mapping
petscii_from_scrcode = []
for c in range(0, 128):
	result = []
	for d in range(0, 256):
		if scrcode_from_petscii[d] == c:
			result.append(d)
	petscii_from_scrcode.append(result)

# read control code descriptions
control_code = {}
for line in open('petscii_control_codes.txt'):
	line = line.rstrip()
	if len(line) != 0:
		control_code[int(line[0:2], 16)] = line[3:]

# read PETSCII -> Unicode
description_from_unicode = {}
unicode_from_petscii = []
unicode_from_petscii.append({})
for line in open('C64IPRI.TXT'):
	line = line.rstrip()
	if line.startswith('#') or len(line) == 0:
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:11], 16)
	unicode_from_petscii[0][petscii] = unicode
	description_from_unicode[unicode] = line[14:]
unicode_from_petscii.append({})
for line in open('C64IALT.TXT'):
	line = line.rstrip()
	if line.startswith('#') or len(line) == 0:
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:11], 16)
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
	'DEL','RETURN','RT CRSR','F4','F1','F2','F3','CRSR DWN',
	'3','W','A','4','Z','S','E','L.SHIFT',
	'5','R','D','6','C','F','T','X',
	'7','Y','G','8','B','H','U','V',
	'9','I','J','0','M','K','O','N',
	'+','P','L','-','.',':','@',',',
	'YEN SIGN','*',';','HOME','R.SHIFTT','=','EXP','/',
	'1','LEFT ARROW','CTRL','2','SPACE','COM.KEY','Q','STOP',
]

print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<html>')
print('<head>')
print('<title>Character Set | Ultimate C64 Reference</title>')
print('')
print('<script language="javascript">')
print('</script>')
print('')
print('<link rel="stylesheet" href="../style.css">')
print('<style type="text/css">')
print('')
print('.container {')
print('  border: 1px solid gray;')
print('  display: inline-block;')
print('  margin: 2px;')
print('  height: ' + str(scale * side) + 'px;')
print('  width: ' + str(scale * side) + ';')
print('  padding:0px;')
print('  background-color: #0f0;')
print(' }')
print('')
print('.inverted {')
print('  filter: invert(100%)')
print(' }')
print('')
print('.character {')
print('  background-image: url(\'43627586.png\');')
print('  background-repeat: no-repeat;')
print('  background-color: #f00;')
print('  transform: scale(' + str(scale) + ',' + str(scale) + ');')
print('  transform-origin: 0% 0%;')
print('  height: ' + str(side) + 'px;')
print('  width: ' + str(side) + 'px;')
print('  margin:0px;')
print('  padding:0px;')
print('  border: 0px;')
print('  display: block;')
print('  image-rendering: pixelated;')
print(' }')
print('')



for c in range(0, 128):
	x = (c & 15) * -8
	y = (c >> 4) * -8
	print('.char-{} {{ background-position:    {}px    {}px; }}'.format(hex(c), x, y))

print('')
print('</style>')


print('<script>')
print('function test(element) {')
print('  document.getElementById(element).style.filter = "invert(100%)";')
print('}')
print('</script>')


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
		print('<span class="container">{}</span>'.format(control_code[c1]))
	else:
		print('<span class="container"><span class="character char-{}"></span></span>'.format(hex(c)))
	if c1 & 15 == 15:
		print('<br />')

print('</div>')
print('</div>')

for c in range(0, 256):
	print('<h2>Screencode {}</h2>'.format(hex(c)))
	if c > 0x80:
		inverted = 'inverted'
	else:
		inverted = ''
	print('<li><span class="container {}"><span class="character char-{}"></span></span></li>'.format(inverted, hex(c & 0x7f)))
	if c < 128:
		for petscii in petscii_from_scrcode[c]:
			print('<li><tt>CHR$({})</tt> [${:02X}]</li>'.format(petscii, petscii))
		petscii = petscii_from_scrcode[c][0]
		unicode = unicode_from_petscii[0][petscii]
		print('<li>Unicode U+{:04X} # {}</li>'.format(unicode, description_from_unicode[unicode]))
		print('<li>Unicode \'&#x{:x};\'</li>'.format(unicode))
		for petscii in petscii_from_scrcode[c]:
			for modifier in range(0, 4):
				for scancode in range(0, 64):
					p2 = petscii_from_scancode[modifier][scancode]
					if p2 != 0xff and p2 == petscii:
						m = description_from_modifier[modifier]
						d = description_from_scancode[scancode]
						if m:
							m = '<span style="background-color: black; color: white;">{}</span> + '.format(m)
						else:
							m = ''

						print('<li>{}<span style="background-color: black; color: white;">{}</span> [${:02X}]</li>'.format(m, d, petscii))

print('</body>')
print('</html>')
