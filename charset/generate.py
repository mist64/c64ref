#!/usr/bin/python3


scale = 4 # character scale up factor
side = 8 # character width/height 8px

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
print('  background-image: url(\'3491641016.png\');')
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
print('</head>')

print('<body>')

print('<div class="body">')
print('<h1>C64 Charsets Things</h1>')

print('<div>')
print('	<img src="3491641016.png" />')
print('</div>')
print('<div>')


for c in range(0, 128):
	print('<span class="container"><span class="character char-{}"></span></span>'.format(hex(c)))
	if c & 15 == 15:
		print('<br />')

for c in range(0, 128):
	print('<span class="container inverted"><span class="character char-{}"></span></span>'.format(hex(c)))
	if c & 15 == 15:
		print('<br />')

print('</div>')
print('</div>')
print('</body>')
print('</html>')

