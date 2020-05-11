#!/usr/bin/python3

import sys
import os
import pprint

with open('c64mem_src_basic.txt', 'r') as f:
	lines = f.read().split('\n')

with open('basic_sym.txt', 'r') as f:
	sym = f.read().split('\n')

symbols = {}

for s in sym:
	address = s[0:4]
	name = s[5:]
	symbols[name] = address

pprint.pprint(symbols)

for line in lines:
	if line.startswith(' '):
		print('             ' + line)
		continue
	symbol = line[0:6].rstrip()
	description = line[8:]
	if symbol in symbols:
		address = ('$' + symbols[symbol] + "        ")
	else:
		address = "$????        "
	print(address + (symbol + '     ')[:6] + '  ' + description)

