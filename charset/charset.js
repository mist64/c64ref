function svgPathFromBin(bin, height) {
	svg = "";
	for (y = 0; y < height; y++) {
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

function svgFromCharBin(bin, height, scale, fgcolor, bgcolor) {
//	var xmlns = "http://www.w3.org/2000/svg";
//
//	var svg = document.createElementNS(xmlns, "svg");
//	svg.style.backgroundColor = bgcolor;
//	svg.setAttributeNS(null, "width", (8 * scale) + "em");
//	svg.setAttributeNS(null, "height", (height * scale) + "em");
//	svg.setAttributeNS(null, "shapeRendering", "crispEdges");
//	svg.setAttributeNS(null, "viewBox", "0 -.5 8 8");
//
//	var path = document.createElementNS(xmlns, "path");
//	path.setAttributeNS(null, 'stroke', fgcolor);
//	path.setAttributeNS(null, 'd', svgPathFromBin(bin));
//	svg.appendChild(path);
//	return svg;

	return "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"8\" height=\"" + height + "\" style=\"background-color:" + bgcolor + "\" shape-rendering=\"crispEdges\" viewBox=\"0 -.5 8 " + height + "\"><path stroke=\"" + fgcolor + "\" d=\"" + svgPathFromBin(bin, height) + "\"/></svg>";
}
