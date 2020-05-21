#!/usr/bin/python3

import sys
import binascii
import pprint
from PIL import Image, ImageDraw

def is_reverse(charset):
	set_pixels = 0
	for c in range(0, 128):
		for y in range(0, 8):
			for x in range(0, 8):
				if charset[((c << 3) | y)] & (1 << (7-x)) > 0:
					set_pixels += 1
	return set_pixels > 4096

def invert(charset):
	for i in range(0, 1024):
		charset[i] ^= 0xff
	return charset

def write_png(charset, filename_out):
	img = Image.new('1', (16 * 8, 8 * 8), color = 'white')
	pixels = img.load()
	for c in range(0, 128):
		for y in range(0, 8):
			for x in range(0, 8):
				if charset[((c << 3) | y)] & (1 << (7-x)) > 0:
					pixels[((c & 15) * 8) | x, (c >> 4) * 8 | y] = 0

	print("Writing {}".format(filename_out))
	img.save(filename_out)


if len(sys.argv) < 2:
	print("Usage: {} <charset.bin>".format(sys.argv[0]))
	exit(1)

charset_descriptions_from_crc = {}
charset_from_crc = {}
char_descriptions_from_crc = {}

for filename_in in sys.argv[1:]:
	if filename_in[-4:] == '.bin' or filename_in[-4:] == '.rom':
		filename_base = filename_in[:-4]
	else:
		filename_base = filename_in

	print("Reading {}".format(filename_in))
	charset_collection = open(filename_in, "rb").read()

	start_offset = 0
	index = 0

	while start_offset < len(charset_collection):
		charset = bytearray(charset_collection[start_offset:start_offset+1024])

		reverse = is_reverse(charset)

		if reverse:
			charset = invert(charset)


		crc = binascii.crc32(charset)

		charset_description = (filename_in, index, reverse)
		if crc in charset_descriptions_from_crc:
			charset_descriptions_from_crc[crc].append(charset_description)
		else:
			charset_descriptions_from_crc[crc] = [charset_description]

		charset_from_crc[crc] = charset

		for c in range(0, 128):
			char = charset[c*8:c*8+8]
			crc = binascii.crc32(char)
			crc_charset = binascii.crc32(charset)
			char_description = (crc_charset, c)
			if crc in char_descriptions_from_crc:
				char_descriptions_from_crc[crc].add(char_description)
			else:
				char_descriptions_from_crc[crc] = set([char_description])

		#write_png(charset, filename_base + '_{}.png'.format(index))

		start_offset += 1024
		index += 1

pprint.pprint(charset_descriptions_from_crc)
#pprint.pprint(char_descriptions_from_crc)
#pprint.pprint(charset_from_crc)

reference_charset_crcs = [
	43627586,   # C64 upper
	3491641016, # C64 lower
	3435009579, # PET upper
	605158551,  # PET lower
	#239914569  # C64 upper alt
	#3704310963 # C64 lower alt
	#2047760083 # C128 lower
	#265494848  # C16 lower
]

for charset_crc in charset_from_crc.keys():
	charset = charset_from_crc[charset_crc]
	similar_charsets = {}
	for c in range(0, 128):
		char = charset[c*8:c*8+8]
		crc = binascii.crc32(char)
		char_descriptions = char_descriptions_from_crc[crc]
		for (charset_crc2, same_c) in char_descriptions:
			if same_c == c and charset_crc2 in reference_charset_crcs:
				if charset_crc2 in similar_charsets:
					similar_charsets[charset_crc2] += 1
				else:
					similar_charsets[charset_crc2] = 1
	print(charset_crc, similar_charsets)

