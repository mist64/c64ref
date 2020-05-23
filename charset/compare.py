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

	#print("Reading {}".format(filename_in))
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

all_charset_crcs = list(charset_descriptions_from_crc.keys())

frendly_name_for_crc = {
	# base
	3435009579: "PET upper",
	605158551:  "PET lower",
	2829211046: "PET 1 lower swapped",

	4273001443: "VIC-20 upper",
	371145055:  "VIC-20 lower",

	43627586:   "C64/C16/C128 upper",
	3491641016: "C64 lower",
	239914569:  "C64 upper alt",
	3704310963: "C64 lower alt",
	2047760083: "C128 lower",
	265494848:  "C16 lower",

	18405299:   "LCD upper",
	3336443024: "LCD lower",

	#
	# PET-style
	#

	453258916:  "VIC-20/C128 German upper",
	18896184:   "VIC-20/C128 German lower",

	4101158221: "C128 Danish upper",
	1940591026: "C128 Danish lower",

	3526512616: "PET French upper",

	2762550771: "C128 French upper",
	1044248186: "C128 French upper alt",
	1835942841: "C128 French lower",
	3010141862: "C128 French lower alt",

	2267404205: "PET German upper",
	619984985:  "PET German lower", # "from VICE"; sane layout
	3068260560: "PET German lower alt", # less sane layout
	3794189463: "PET German lower alt", # 8296D

	3980244294: "PET Greek upper", # greek characters instead of latin, some latin in graphics
	3648127786: "PET Greek lower",

	556671508:  "PET Norwegian upper",
	3534714178: "PET Norwegian lower",
	813334050:  "C128 Norwegian upper",
	420996052:  "C128 Norwegian upper alt",
	1384180002: "C128 Norwegian lower",
	2188101221: "C128 Norwegian lower alt",

	3522684517: "VIC-20/C128 Norwegian upper",
	1316062724: "VIC-20/C128 Norwegian upper alt",
	1319596343: "VIC-20/C128 Norwegian lower",
	738416628:  "VIC-20/C128 Norwegian lower alt",

	2975021441: "PET Russian upper", # cyrillic in graphics

	2712146221: "C128 Spanish upper",
	3401793753: "C128 Spanish upper alt",
	1382891279: "C128 Spanish lower",
	1625115699: "C128 Spanish lower alt",

	1378924721: "PET/VIC-20 Swedish upper",
	738563421:  "PET/VIC-20 Swedish lower",
	2706267264: "VIC-20 Swedish lowern alt", # same as above, but ö seems buggy

	891747983:  "C128 Swiss upper",
	2947687686: "C128 Swiss upper alt",
	4242641093: "C128 Swiss lower (PET French lower)",
	585420250:  "C128 Swiss lower alt",

	1044400996: "VIC-20 Japanese upper", # pound -> yen
	3580406124: "VIC-20 Japanese upper/Kanji",

	#
	# C64-style
	#

	2746692664: "C64 Danish upper",
	2942455347: "C64 Danish upper alt",
	3266402763: "C64 Danish lower",
	3462669248: "C64 Danish lower alt",

	3962070790: "C64 Hungarian lower",
	3911143684: "C64 Hungarian lower alt",

	3224365868: "C64 Spanish upper",
	2256338360: "C64 Spanish lower",

	684454765:  "C64 Swedish upper",
	4104886629: "C64 Swedish upper 2",
	4099903933: "C64 Swedish upper alt",
	4169065326: "C64 Swedish upper 2 alt",
	2117474727: "C64 Swedish lower",
	3699529572: "C64 Swedish lower 2",
	3324836326: "C64 Swedish lower alt",
	2743931256: "C64 Swedish lower 2 alt",

	679100969:  "C16 Hungarian upper",
	2966169543: "C16 Hungarian lower",

	#
	# PET other
	#
	909143548:  "SuperPET ASCII",
	276903316:  "SuperPET ASCII Swedish",
	2832168426: "SuperPET APL",

	#
	# Other
	#
	1220100133: "C64 Japanese upper", # PET looks, one line shifted down, symbols scrambled
	2318553394: "C64 Japanese upper/Kanji",
	1258522589: "C64 Turkish upper", # probably 3rd party
	1004035711: "C64 Turkish lower", # probably 3rd party
	2503191058: "C64 upper (buggy 1)", # from C128 Norwegian
	1495968665: "C64 upper (buggy 2)", # from C128 Norwegian
	1802520121: "C64 lower (buggy 1)", # from C128 Norwegian
	163579034:  "C64 lower (buggy 1)", # from C128 Norwegian
}

reference_charset_crcs = list(frendly_name_for_crc.keys())

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
	if charset_crc in reference_charset_crcs:
		print('{}:'.format(frendly_name_for_crc[charset_crc]))
	else:
		print(charset_descriptions_from_crc[charset_crc], charset_crc)

	data = []
	for similar_charset_crc in similar_charsets.keys():
		data.append((similar_charsets[similar_charset_crc], similar_charset_crc))
	data.sort(key=lambda tup: tup[0], reverse=True)

	for (num, crc) in data:
		print('\t', num, frendly_name_for_crc[crc])

