window.onload = init;
function init() {
	var req = new XMLHttpRequest();
	req.open("GET", "chargen", true);
	req.responseType = "arraybuffer";

	req.onload = function (oEvent) {
		var arrayBuffer = req.response;
		if (arrayBuffer) {
			var byteArray = new Uint8Array(arrayBuffer);
			all_svg = "";
			for (i = 0; i < 256; i++) {
				svg = svgFromCharBin(byteArray.slice(i*8,i*8+8));
				all_svg += svg;
			}
			var infoBox = document.getElementById("main");
			infoBox.innerHTML = all_svg;
		}
	};
	req.send(null);
}

function svgFromCharBin(bin) {
	size = '1em';
	bgcolor = '#2E2C9B';
	fgcolor = '#706DEB';
	svg = "";
	svg = "<svg width=\"" + size + "\" height=\""+ size + "\" style=\"background-color:" + bgcolor + "\" shape-rendering=\"crispEdges\" viewBox=\"0 -.5 8 8\" xmlns=\"http://www.w3.org/2000/svg\"><path stroke=\"" + fgcolor + "\" d=\"";
	for (y = 0; y < 8; y++) {
		byte = bin[y];
		is_first = true;
		prev = -1;
		count = 1;
		for (x = 0; x < 8; x++) {
			bit = (byte >> (7-x)) & 1;
			//svg += "bit #" + x + ": " + bit + "<br/>"
			if (bit == prev) {
				count++;
			} else {
				if (prev != -1) {
//					svg += "found " + count + " bits of value " + prev + "<br/>"
				}
				if (prev == 1) {
					svg += "M" + (x - count) + " " + y + "h" + count;
				}
				prev = bit;
				count = 1;
			}
		}
//		svg += "found " + count + " bits of value " + prev + "<br/>"
				if (prev == 1) {
					svg += "M" + (x - count) + " " + y + "h" + count;
				}
//		svg += "new line<br/>"
	}
//	svg += "m2 0h4m5 0h2m4 0h5m4 0h4m3"
	svg += "\"/></svg>";
	return svg;
}
