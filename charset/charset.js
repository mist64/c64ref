function svgPathFromBin(bin) {
	svg = "";
	for (y = 0; y < 8; y++) {
		byte = bin[y];
		is_first = true;
		prev = -1;
		count = 1;
		for (x = 0; x < 8; x++) {
			bit = (byte >> (7-x)) & 1;
			if (bit == prev) {
				count++;
			} else {
				if (prev == 1) {
					svg += "M" + (x - count) + " " + y + "h" + count;
				}
				prev = bit;
				count = 1;
			}
		}
		if (prev == 1) {
			svg += "M" + (x - count) + " " + y + "h" + count;
		}
	}
	return svg;
}

function svgFromCharBin(bin, size, fgcolor, bgcolor) {
	return "<svg width=\"" + size + "\" height=\""+ size + "\" style=\"background-color:" + bgcolor + "\" shape-rendering=\"crispEdges\" viewBox=\"0 -.5 8 8\"><path stroke=\"" + fgcolor + "\" d=\"" + svgPathFromBin(bin) + "\"/></svg>";
}
