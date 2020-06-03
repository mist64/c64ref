function svgPathFromBin(bin) {
	svg = "";
	for (var y = 0; y < 256 * 8; y++) {
		ty = y & 7;
		byte = bin[y & 0x3ff];
		if (y & (0x80 << 3)) {
			byte ^= 0xff;
		}
		is_first = true;
		prev = -1;
		count = 1;
		for (x = 0; x < 8; x++) {
			tx = y & ~7 | x;
			bit = (byte >> (7-x)) & 1;
			if (bit == prev) {
				count++;
			} else {
				if (prev == 1) {
					svg += "M" + (tx - count) + " " + ty + "h" + count;
				}
				prev = bit;
				count = 1;
			}
		}
		if (prev == 1) {
			svg += "M" + (tx - count + 1) + " " + ty + "h" + count;
		}
	}
	return svg;
}

function svgFromCharBin(bin, scale, fgcolor, bgcolor) {
	fgcolor = fgcolor.replace("#", "%23");
	bgcolor = bgcolor.replace("#", "%23");
	return "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"" + 256 * 8 + "\" height=\"8\" style=\"background-color:" + bgcolor + "\" shape-rendering=\"auto\" viewBox=\"0 -.5 " + 256 * 8 + " 8\"><path stroke=\"" + fgcolor + "\" d=\"" + svgPathFromBin(bin) + "\"/></svg>";
}
