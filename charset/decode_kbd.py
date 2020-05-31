#!/usr/bin/python3

VSCALE = 2
SCALE = 10
ROUND = 5
INSET = 1
FONT_SIZE1 = 18
FONT_SIZE2 = 11.5
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
}

machines = ['PET', 'VIC-20', 'C64', 'C128', 'C65', 'TED', 'CBM2']

print('<meta http-equiv="Content-type" content="text/html; charset=utf-8" />')
print('<script src="script.js"></script>')

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

description_from_scancode = {}
for machine in machines:
	description_from_scancode[machine] = []
	layout_lines = []
	for line in open('keyboard_{}.txt'.format(machine.lower())):
		line = line.split('#')[0].rstrip()
		if len(line) == 0:
			continue
		key = line[:8].rstrip()
		line = line[8:]
		if key == 'layout':
			layout_lines.append(line)
		elif key == 'cap':
			values = line.split(' ')
			while '' in values:
				values.remove('')
			values = [d.replace('HASH', '#') for d in values]
			description_from_scancode[machine].extend(values)

	#print('<pre>')
	#print(description_from_scancode)
	#for line in layout_lines:
	#	print(line)
	#print('</pre>')

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
				elif scancode == '...':
					scancode = -1 # key does no produce a scancode
				elif scancode == 'NMI':
					scancode = -2 # NMI key
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

	#print('<pre>')
	#for line in layout_lines:
	#	print(line)
	#print('</pre>')

	#print(cells_from_scancode)

	print('<br/>')
	print('<hr/>')
	print('<h2>{}</h2>'.format(machine))

	total_width = 0

	for line in layout_lines:
		if len(line) > total_width:
			total_width = len(line)

	total_width *= SCALE
	total_height = len(layout_lines) * VSCALE * SCALE

	svg = '<svg id="svgelem" width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">'.format(total_width, total_height)
	svg += '<!-- This SVG was generated from a textual description. Check out c64ref on GitHub for more information. -->'
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

			minx += INSET
			miny += INSET
			width -= INSET*2
			height -= INSET*2

			if scancode == -2:
				description = 'RESTORE'
			elif scancode >= 0 and scancode < len(description_from_scancode[machine]):
				description = description_from_scancode[machine][scancode]
			else:
				description = ''
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

			if height > width:
				style = 'style="writing-mode: tb; glyph-orientation-vertical: 0; letter-spacing: -1;"'
				font_vadjust = 0
			else:
				style = ''

			svg += '<a xlink:href="javascript:void(0)" onclick="highlight(\'{}\',{});">'.format(machine, scancode)
			svg += '<rect class="keyrect keyrect_{}_{}" x="{}" y="{}" rx="{}" ry="{}" width="{}" height="{}" style="stroke:black;fill:white;"/>\n'.format(machine, scancode, minx, miny, ROUND, ROUND, width, height)
			svg += '<text class="keytext keytext_{}_{}" text-anchor="middle" font-family="Helvetica" font-size="{}" {} fill="black">'.format(machine, scancode, font_size, style)
			svg += '<tspan x="{}" y="{}">{}</tspan>'.format(minx + width/2, miny + height/2 + font_vadjust, description)
			svg += '</text>'
			svg += '</a>'

	svg += '      </svg>'
	print(svg)

