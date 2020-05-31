#!/usr/bin/python3

machine = 'PET'

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
	line = line[:45] #XXX
	if key == 'layout':
		layout_lines.append(line)
for line in layout_lines:
	print(line)

cells_from_scancode = {}

for y in range(0, len(layout_lines)):
	for x in range(0, len(line)):
		c = layout_lines[y][x]
		if c != '+' and c != '|' and c != '-' and c != 'X':
			# we found a key!
			#print(x, y)
			scancode = ''
			for x2 in range(x, len(line)):
				c = layout_lines[y][x2]
				if c == '+' or c == '|' or c == '-':
					break
				scancode += c
			scancode = scancode.lstrip().rstrip()
			scancode = int(scancode, 16)
			#print('scancode', hex(scancode))
			# mark all cells as seen
			cells = []
			flood_fill(x, y)
			#print(cells)
			cells_from_scancode[scancode] = cells

for line in layout_lines:
	print(line)

print(cells_from_scancode)
