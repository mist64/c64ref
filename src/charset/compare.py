#!/usr/bin/env python3

import sys
import binascii
import pprint
from PIL import Image, ImageDraw

frendly_name_for_crc = {
	# base
	3435009579: ("PET", "", "upper", ""),
	605158551:  ("PET", "", "lower", ""),
	2829211046: ("PET", "", "lower", "swapped"),

	4273001443: ("VIC-20", "", "upper", ""), # same as "PET upper", but '£' instead of '\'
	371145055:  ("VIC-20", "", "lower", ""), # same as "PET lower", but '£' instead of '\'

	43627586:   ("C64/C16/C128", "", "upper", ""),
	239914569:  ("C64", "", "upper", "alt"), # dual-pixel '@'
	3491641016: ("C64", "", "lower", ""),
	3704310963: ("C64", "", "lower", "alt"), # dual-pixel '@'
	265494848:  ("C16", "", "lower", ""),
	2047760083: ("C128", "", "lower", ""),

	18405299:   ("LCD", "", "upper", ""),
	3336443024: ("LCD", "", "lower", ""),

	#
	# PET-style
	#

	4228823884: ("VIC-20", "Danish", "upper", ""),
	3624743168: ("VIC-20", "Danish", "lower", ""),

	4101158221: ("C128", "Danish", "upper", ""),
	1940591026: ("C128", "Danish", "lower", ""),

	3526512616: ("PET", "French", "upper", ""),

	2762550771: ("C128", "French", "upper", ""),
	1044248186: ("C128", "French", "upper", "alt"),
	1835942841: ("C128", "French", "lower", ""),
	3010141862: ("C128", "French", "lower", "alt"),
	4274898967: ("PET", "French", "lower", ""), # 8096; unconfirmed whether it's French

	2267404205: ("PET", "German", "upper", ""),
	619984985:  ("PET", "German", "lower", ""), # "from VICE"; sane layout
	3068260560: ("PET", "German", "lower", "alt"), # less sane layout
	3794189463: ("PET", "German", "lower", "alt2"), # 8296D

	453258916:  ("C128", "German", "upper", ""), # extra characters in last graphics row
	18896184:   ("C128", "German", "lower", ""), # extra characters graphics

	3980244294: ("PET", "Greek", "upper", ""), # greek characters instead of latin, some latin in graphics
	3648127786: ("PET", "Greek", "lower", ""),

	2058038919: ("PET", "Hungarian", "upper", ""),
	1566913143: ("PET", "Hungarian", "lower", ""),

	1044400996: ("PET/VIC-20", "Japanese", "upper", ""),    # pound -> yen, used on VIC-20
	1761655243: ("PET/VIC-20", "Japanese", "upper", "bug"), # same as above, bug pixel in arrow-left, used on PET
	3580406124: ("VIC-20", "Japanese", "upper-Kanji", ""),

	556671508:  ("PET", "Norwegian", "upper", ""),
	3534714178: ("PET", "Norwegian", "lower", ""),
	1384180002: ("C128", "Norwegian", "lower", ""), # similar layout, but unrelated
	2188101221: ("C128", "Norwegian", "lower", "alt"),

	3522684517: ("C128", "Norwegian", "upper", ""),
	813334050:  ("C128", "Norwegian", "upper", "bugs"), # as above; bugs (several unset pixels)
	1316062724: ("C128", "Norwegian", "upper", "alt"),  # underlined 'AE'
	420996052:  ("C128", "Norwegian", "upper", "alt-bugs"), # as above; bugs (several set pixels)
	1319596343: ("C128", "Norwegian", "lower", ""),
	738416628:  ("C128", "Norwegian", "lower", "alt"),

	2975021441: ("PET", "Russian", "upper", ""), # cyrillic in graphics

	2712146221: ("C128", "Spanish", "upper", ""),
	3401793753: ("C128", "Spanish", "upper", "alt"), # different 'Ç'
	1382891279: ("C128", "Spanish", "lower", ""),
	1625115699: ("C128", "Spanish", "lower", "alt"), # bug: extra pixel in 'Z'

	1378924721: ("PET/VIC-20", "Swedish", "upper", ""),
	738563421:  ("PET/VIC-20", "Swedish", "lower", ""),
	2706267264: ("VIC-20", "Swedish", "lower", "alt"), # as above; buggy 'ö'

	891747983:  ("C128", "Swiss", "upper", ""),
	2947687686: ("C128", "Swiss", "upper", "alt"),
	4242641093: ("C128", "Swiss", "lower",  ""), # also: PET French lower,
	585420250:  ("C128", "Swiss", "lower", "alt"),

	#
	# C64-style
	#

	2746692664: ("C64", "Danish", "upper", ""),
	2942455347: ("C64", "Danish", "upper", "alt"),
	3266402763: ("C64", "Danish", "lower", ""),
	3462669248: ("C64", "Danish", "lower", "alt"),

	679100969:  ("C16", "Hungarian", "upper", ""),
	2966169543: ("C16", "Hungarian", "lower", ""),

	3224365868: ("C64", "Spanish", "upper", ""),
	2256338360: ("C64", "Spanish", "lower", ""),

	684454765:  ("C64", "Swedish", "upper", ""),       # 1-pixel '@', 1-pixel 'Ä'/'Ö' dots
	4099903933: ("C64", "Swedish", "upper", "bugs"),  # as above; buggy 'Ä'
	4104886629: ("C64", "Swedish", "upper", "alt"),   # 1-pixel '@', 2-pixel 'Ä'/'Ö' dots
	4169065326: ("C64", "Swedish", "upper", "alt2"), # 2-pixel '@', 2-pixel 'Ä'/'Ö' dots
	2117474727: ("C64", "Swedish", "lower", ""),       # 1-pixel '@', 1-pixel 'ä'/'ö'/'Ä'/'Ö'
	3324836326: ("C64", "Swedish", "lower", "alt"),   # as above; buggy 'Ä', 2-pixel '@'
	3699529572: ("C64", "Swedish", "lower", "2"),     # 1-pixel '@', 2-pixel 'ä'/'ö'/'Ä'/'Ö', different 'å'
	2743931256: ("C64", "Swedish", "lower", "2alt"), # as above; buggy 'ä', 2-pixel '@'

	#
	# PET other
	#
	909143548:  ("SuperPET", "", "ASCII", ""),
	276903316:  ("SuperPET", "Swedish", "ASCII", ""),
	2832168426: ("SuperPET", "", "APL", ""),

	#
	# Other
	#
	1220100133: ("C64", "Japanese", "upper", ""), # PET looks, one line shifted down, symbols scrambled
	2318553394: ("C64", "Japanese", "upper-Kanji", ""),
	1258522589: ("C64", "Turkish", "upper", ""), # probably 3rd party
	1004035711: ("C64", "Turkish", "lower", ""), # probably 3rd party
	2503191058: ("C64", "", "upper", "buggy1"), # from C128 Norwegian
	1495968665: ("C64", "", "upper", "buggy2"), # from C128 Norwegian
	1802520121: ("C64", "", "lower", "buggy1"), # from C128 Norwegian
	163579034:  ("C64", "", "lower", "buggy1"), # from C128 Norwegian
}

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

def friendly_filename_for_crc(crc):
	(machine, locale, type, version) = frendly_name_for_crc[crc]
	if locale == '':
		locale = 'us'
	filename = machine.split('/')[0] + '_' + locale + '_' + type
	if version != '':
		filename += '_' + version
	return filename.lower()

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
		#write_png(charset, str(binascii.crc32(charset)) + '.png'.format(index))
		#write_png(charset, friendly_filename_for_crc(binascii.crc32(charset)) + '.png')

		#open(friendly_filename_for_crc(binascii.crc32(charset)) + '.bin', "wb").write(charset)


		start_offset += 1024
		index += 1

for crc in [3435009579,605158551,2829211046,4273001443,371145055,43627586,239914569,3491641016,3704310963,265494848,2047760083,18405299,3336443024,4228823884,3624743168,4101158221,1940591026,3526512616,2762550771,1044248186,1835942841,3010141862,4274898967,2267404205,619984985,3068260560,3794189463,453258916,18896184,3980244294,3648127786,2058038919,1566913143,1044400996,1761655243,3580406124,556671508,3534714178,1384180002,2188101221,3522684517,813334050,1316062724,420996052,1319596343,738416628,2975021441,2712146221,3401793753,1382891279,1625115699,1378924721,738563421,2706267264,891747983,2947687686,4242641093,585420250,2746692664,2942455347,3266402763,3462669248,679100969,2966169543,3224365868,2256338360,684454765,4099903933,4104886629,4169065326,2117474727,3324836326,3699529572,2743931256,909143548,276903316,2832168426,1220100133,2318553394,1258522589,1004035711,2503191058,1495968665,1802520121,163579034]:
	filename = friendly_filename_for_crc(crc)
	(machine, locale, type, version) = frendly_name_for_crc[crc]
	print("('" + filename + "', '" + machine + "', '" + locale + "', '" + type + "', '" + version + "'),")


pprint.pprint(charset_descriptions_from_crc)
#pprint.pprint(char_descriptions_from_crc)
#pprint.pprint(charset_from_crc)

all_charset_crcs = list(charset_descriptions_from_crc.keys())


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

