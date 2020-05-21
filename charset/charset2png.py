#!/usr/bin/python3

from PIL import Image, ImageDraw

charset = open("chargen", "rb").read()

img = Image.new('1', (16 * 8, 16 * 8), color = 'white')
pixels = img.load()
for c in range(0, 256):
	for y in range(0, 8):
		for x in range(0, 8):
			if charset[((c << 3) | y)] & (1 << (7-x)) > 0:
				pixels[((c & 15) * 8) | x, (c >> 4) * 8 | y] = 0

img.save("charset-c64.png")

