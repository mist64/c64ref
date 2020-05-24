#!/usr/bin/python3





print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<html>')
print('<head>')
print('<title>Memory Map | Ultimate C64 Reference</title>')
print('')
print('<script language="javascript">')
print('</script>')
print('')
print('<link rel="stylesheet" href="style.css">')
print('<style type="text/css">')
print('')
print('')
print('.charset {')
print('  background-image: url(\'3491641016.png\');')
print('  background-repeat: no-repeat;')
print('  background-color:#f00;')
print('  transform: scale(4,4);')
print('  height: 8px;')
print('  width: 8px;')
print('  margin:16px;')
print('  padding:0px;')
print('  border: 0px;')
print('  display: inline-block;')
print('  image-rendering: pixelated;')
print(' }')

for c in range(0, 128):
	x = (c & 15) * -8
	y = (c >> 4) * -8
	print('.char-{} {{ background-position:    {}px    {}px; }}'.format(hex(c), x, y))


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
	print('<span class="charset char-{}"></span>'.format(hex(c)))
	if c & 15 == 15:
		print('<br />')

print('</div>')
print('</div>')
print('</body>')
print('</html>')

