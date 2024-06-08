#!/usr/bin/env python3

import sys
import os
import pprint

with open('c64mem_64intern.txt', 'r') as f:
	lines = f.read().split('\n')

with open('symbols.txt', 'r') as f:
	sym = f.read().split('\n')

symbols = {}

for s in sym:
	if not s.startswith('$'):
		continue
	address = s[1:5]
	name = s[6:12]
	symbols[address] = name

#pprint.pprint(symbols)

for line in lines:
	if line.startswith('-') or line.startswith('#') or len(line) == 0:
		print(line)
		continue

	if not line.startswith('$'):
		print(line)
		continue
	address = line[0:13]
	start_address = line[1:5]
	description = line[21:]
	if start_address in symbols:
		symbol = (symbols[start_address] + "        ")[:8]
	else:
		symbol = "        "
	print(address + symbol + description)

