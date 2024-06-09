#!/usr/bin/env python3

import sys
from PIL import Image, ImageDraw

if len(sys.argv) < 2:
	print("Usage: {} <charset.bin>".format(sys.argv[0]))
	exit(1)

for filename_in in sys.argv[1:]:
	if filename_in[-4:] == '.bin' or filename_in[-4:] == '.rom':
		filename_base = filename_in[:-4]
	else:
		filename_base = filename_in

	print("Reading {}".format(filename_in))
	charset = open(filename_in, "rb").read()

	start_offset = 0
	index = 0

	while start_offset < len(charset):
		img = Image.new('1', (16 * 8, 8 * 8), color = 'white')
		pixels = img.load()
		for c in range(0, 128):
			for y in range(0, 8):
				for x in range(0, 8):
					if charset[start_offset + ((c << 3) | y)] & (1 << (7-x)) > 0:
						pixels[((c & 15) * 8) | x, (c >> 4) * 8 | y] = 0

		filename_out = filename_base + '_{}.png'.format(index)
		print("Writing {}".format(filename_out))
		img.save(filename_out)

		start_offset += 1024
		index += 1


