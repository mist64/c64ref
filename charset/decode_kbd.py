#!/usr/bin/python3

VSCALE = 4/3
SCALE = 10
ROUND = 5

machine = 'TED'

def flood_fill(x, y):
	#print(':',x,y)
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

layout_lines = []
for line in open('keyboard_{}.txt'.format(machine.lower())):
	line = line.split('#')[0].rstrip()
	if len(line) == 0:
		continue
	key = line[:8].rstrip()
	line = line[8:]
	if key == 'layout':
		layout_lines.append(line)
print('<pre>')
for line in layout_lines:
	print(line)
print('</pre>')

cells_from_scancode = {}

for y in range(0, len(layout_lines)):
	for x in range(0, len(layout_lines[y])):
		c = layout_lines[y][x]
		if c != '+' and c != '|' and c != '-' and c != 'X':
			# we found a key!
			#print(x, y)
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
				scancode = int(scancode[1:], 16) | 128
			else:
				scancode = int(scancode, 16)
			#print('scancode', hex(scancode))
			# mark all cells as seen
			cells = []
			flood_fill(x, y)
			#print(cells)
			if scancode in cells_from_scancode:
				cells_from_scancode[scancode].append(cells)
			else:
				cells_from_scancode[scancode] = [cells]

print('<pre>')
for line in layout_lines:
	print(line)
print('</pre>')

#print(cells_from_scancode)

print('<br/>')
print('<hr/>')

total_width = 0

for line in layout_lines:
    if len(line) > total_width:
        total_width = len(line)

total_width *= SCALE
total_height = len(layout_lines) * VSCALE * SCALE

svg = '      <svg id="svgelem" width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">'.format(total_width, total_height)
for scancode in cells_from_scancode.keys():
	cells = cells_from_scancode[scancode]

	for cell in cells:
		#print(cell)

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

		svg += '<rect x="{}" y="{}" rx="{}" ry="{}" width="{}" height="{}" style="stroke:black;fill:none;"/>\n'.format(minx, miny, ROUND, ROUND, width, height)
		svg += '<text x="{}" y="{}" font-family="Helvetica" font-size="8" fill="black">{:02X}</text>'.format(minx, miny, scancode)
svg += '      </svg>'
print(svg)

