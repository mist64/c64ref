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
unicode_from_scrcode = []
unicode_from_scrcode.append({})
for line in open('C64IPRI.TXT'):
	line = line.rstrip()
	if line.startswith('#') or len(line) == 0:
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:11], 16)
	unicode_from_scrcode[0][petscii] = unicode
	description_from_unicode[unicode] = line[14:]
unicode_from_scrcode.append({})
for line in open('C64IALT.TXT'):
	line = line.rstrip()
	if line.startswith('#') or len(line) == 0:
		continue
	petscii = int(line[2:4], 16)
	unicode = int(line[7:11], 16)
	unicode_from_scrcode[1][petscii] = unicode
	description_from_unicode[unicode] = line[14:]

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
	if c < 128:
		for petscii in petscii_from_scrcode[c]:
			print('<li><tt>CHR$({})</tt></li>'.format(petscii))
		unicode = unicode_from_scrcode[0][petscii_from_scrcode[c][0]]
		print('<li>Unicode U+{:04X} # {}</li>'.format(unicode, description_from_unicode[unicode]))
		print('<li>Unicode \'&#x{:x};\'</li>'.format(unicode))

print('</body>')
print('</html>')

