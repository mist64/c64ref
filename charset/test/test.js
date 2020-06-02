window.onload = init;
function init() {
	var req = new XMLHttpRequest();
	req.open("GET", "chargen", true);
	req.responseType = "arraybuffer";

	req.onload = function (oEvent) {
		var arrayBuffer = req.response;
		if (arrayBuffer) {
			var byteArray = new Uint8Array(arrayBuffer);
			createSVG(byteArray.slice(0,8));
		}
	};
	req.send(null);
}

function createSVG(bin) {
	var infoBox = document.getElementById("main");
	svg = "";
	for (y = 0; y < 8; y++) {
		byte = bin[y];
		for (x = 0; x < 8; x++) {
			bit = (byte >> (7-x)) & 1;
			svg += bit + ",";
		}
		svg += "<br/>";
	}
	infoBox.innerHTML = svg;

}
