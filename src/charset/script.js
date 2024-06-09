window.onload = init;

const colorsets = [
	{ fg: '#000000', bg: '#FFFFFF'}, // black on white
	{ fg: '#4DF600', bg: '#000000'}, // PET: green on black
	{ fg: '#2E2C9B', bg: '#FFFFFF'}, // VIC-20: blue on white
	{ fg: '#706DEB', bg: '#2E2C9B'}, // C64: lt.blue on blue
	{ fg: '#A9FF9F', bg: '#7B7B7B'}, // C128: lt.green on gray
	{ fg: '#FFFFFF', bg: '#2E2C9B'}, // C65: white on blue
	{ fg: '#000000', bg: '#B2B2B2'}, // TED: lt.green on gray
];

const scales = [
	{ h: 4, v: 4 },       // Square
	{ h: 4*0.955, v: 4 }, // C64 PAL
	{ h: 4*0.75, v: 4 },  // C64 NTSC
	{ h: 2, v: 4 },       // C128
	{ h: 4, v: 2 },       // VIC-20
];

var gSheet;
var gfgcolor = colorsets[3]['fg'];
var gbgcolor = colorsets[3]['bg'];
var gcharset = "bin/c64_us_upper.bin";
var ghscale = 4;
var gvscale = 4;

function init() {
	gSheet = document.createElement('style')
	document.body.appendChild(gSheet);

	updateCharset();

	populateCharsetTable('char-img128');

	xorCharsets();

	document.getElementById("radio_C64").click();
}

function setBackgroundImage(backgroundImage) {
	css = "";
	css += ".char-img {";
	css += "    background-image: " + backgroundImage + ";";
	css += "        transform: scale(" + ghscale + ", " + gvscale + ");";
	css += "}";
	gSheet.innerHTML = css;
}

function updateCharset() {
	loadCharset(gcharset, gfgcolor, gbgcolor);
}

function loadCharset(filename, fgcolor, bgcolor) {
	var req = new XMLHttpRequest();
	req.open("GET", filename, true);
	req.responseType = "arraybuffer";

	req.onload = function (oEvent) {
		var arrayBuffer = req.response;
		if (arrayBuffer) {
			var byteArray = new Uint8Array(arrayBuffer);
			scale = 2;
			svg = svgFromCharBin(byteArray, scale, fgcolor, bgcolor);
			setBackgroundImage("url('data:image/svg+xml;utf8," + svg + "')");
		}
	};
	req.send(null);
}

function charsetSwitch(filename) {
	gcharset = filename;
	updateCharset();

	if (gcharset.includes('upper')) {
		unicodeSwitch(0);
	} else {
		unicodeSwitch(1);
	}
}


function colorsetSwitch(index) {
	gfgcolor = colorsets[index]['fg'];
	gbgcolor = colorsets[index]['bg'];
	updateCharset();
}

function aspectratioSwitch(index) {
	ghscale = scales[index]['h'];
	gvscale = scales[index]['v'];
	updateCharset();
}

function controlcodesSwitch(machine) {
	hideItems("control_codes");
	showItems("control_codes_" + machine);
}

function populateCharsetTable(className) {
	items = document.getElementsByClassName(className);
	for (var i = 0; i < items.length; i++) {
		var item = items[i];
		var filename = item.id;
		if (filename == 'charset_cmp') {
			continue;
		}

		var makeRequest = function(item) {
			var req = new XMLHttpRequest();
			req.open("GET", filename, true);
			req.responseType = "arraybuffer";
			req.onload = function(data) {
				// extraInfo is accessible here
				reply = data.target.response;
				var arrayBuffer = req.response;
				if (arrayBuffer) {
					var byteArray = new Uint8Array(arrayBuffer);
					scale = 1;
					svg = svgFromCharBin(byteArray, scale, '#000000', '#FFFFFF');
					item.style.backgroundImage = "url('data:image/svg+xml;utf8," + svg + "')";
				}
			};
			req.send(null);
		};
		makeRequest(item);
	}
}

function charsetCompareSwitch(index, filename) {
	className = 'charset_cmp_' + index;
	item = document.getElementsByClassName(className)[0];
	item.id = filename;
	populateCharsetTable(className);
	xorCharsets();
}

function xorCharsets() {
	filename1 = document.getElementsByClassName('charset_cmp_0')[0].id;
	filename2 = document.getElementsByClassName('charset_cmp_1')[0].id;
	console.log(filename1);
	console.log(filename2);

	var req1 = new XMLHttpRequest();
	req1.open("GET", filename1, true);
	req1.responseType = "arraybuffer";

	req1.onload = function (oEvent) {
		var arrayBuffer1 = req1.response;
		if (arrayBuffer1) {
			var req2 = new XMLHttpRequest();
			req2.open("GET", filename2, true);
			req2.responseType = "arraybuffer";

			req2.onload = function (oEvent) {
				var arrayBuffer2 = req2.response;
				if (arrayBuffer2) {
					var byteArray1 = new Uint8Array(arrayBuffer1);
					var byteArray2 = new Uint8Array(arrayBuffer2);
					for (var i = 0; i < 1024; i++) {
						byteArray1[i] ^= byteArray2[i];
					}
					item = document.getElementById('charset_cmp');
					scale = 1;
					svg = svgFromCharBin(byteArray1, scale, '#000000', '#FFFFFF');
					item.style.backgroundImage = "url('data:image/svg+xml;utf8," + svg + "')";
				}
			};
			req2.send(null);
		}
	};
	req1.send(null);
}

function test(element) {
	if (element == null) {
		var infoBox = document.getElementById("info_box");
		infoBox.innerHTML = '';
	} else {
		var box = document.getElementById(element);
		box.classList.add("highlighted");

		var boxes = document.getElementsByClassName("char-box highlighted");
		var i;
		for (i = 0; i < boxes.length; i++) {
			var currentBox = boxes[i];
			if (currentBox != box) {
				currentBox.classList.remove("highlighted");
			}
		}

		var infoId = "info_".concat(element) ;
		var currentInfo = document.getElementById(infoId);
		var infoBox = document.getElementById("info_box");
		infoBox.innerHTML = currentInfo.innerHTML;
	}
}

function checkMachines(selectionArray, checked) {
	var x;
	for (x = 0; x < selectionArray.length; x++) {
		var currentMachine = selectionArray[x];
		toggleMachine(currentMachine, checked, []);
	}
}

function toggleMachine(machine, checked, deselectionArray=[]) {

	/* hide everything in the deselection array */
	var x;
	for (x = 0; x < deselectionArray.length; x++) {
		var currentClass = deselectionArray[x];
		var currentCheckboxId = "checkbox_".concat(currentClass);
		var currentCheckbox = document.getElementById(currentCheckboxId);

		var items = document.getElementsByClassName(currentClass);
		var i;
		for (i = 0; i < items.length; i++) {
			var currentItem = items[i];
			currentItem.style.display = "none";
		}

		currentCheckbox.checked = false;
	}
	
	/* hide or show the selected class */
	var items = document.getElementsByClassName(machine);
	var i;
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		if (checked) {
			currentItem.style.display = null;
		} else {
			currentItem.style.display = "none";
		}
	}

	/* update radio button and checkbox selection state */
	var currentCheckboxId = "checkbox_".concat(machine);
	var currentCheckbox = document.getElementById(currentCheckboxId);
	currentCheckbox.checked = checked;

	if (deselectionArray.length == 0) {
		var radioList = document.getElementsByName("radios");
		var y;
		for (y = 0; y < radioList.length; y++) {
			var currentRadio = radioList[y];
			currentRadio.checked = false;
		}
	}

	// hide PETSCII table columns that are disabled
	var item = document.getElementById("petscii_show");
	index = item.selectedIndex;
	if (index == 0) {
		hideItems("petscii_control");
	} else if (index == 1) {
		hideItems("petscii_keyboard");
	}

	if (deselectionArray.length != 0) {
		switch (machine) {
			case 'PET-N':
			case 'PET-B':
			case 'CBM2':
				gcharset = 'bin/pet_us_upper.bin';
				colindex = 1;
				scalesindex = 0;
				break;
			case 'VIC-20':
				gcharset = 'bin/vic-20_us_upper.bin';
				colindex = 2;
				scalesindex = 4;
				break;
			case 'C64':
				gcharset = 'bin/c64_us_upper.bin';
				colindex = 3;
				scalesindex = 1;
				break;
			case 'C128':
				gcharset = 'bin/c64_us_upper.bin';
				colindex = 4;
				scalesindex = 1;
				break;
			case 'C65':
				gcharset = 'bin/c64_us_upper.bin';
				colindex = 5;
				scalesindex = 0;
				break;
			case 'TED':
				gcharset = 'bin/c64_us_upper.bin';
				colindex = 6;
				scalesindex = 0;
				break;
		}
		gfgcolor = colorsets[colindex]['fg'];
		gbgcolor = colorsets[colindex]['bg'];
		ghscale = scales[scalesindex]['h'];
		gvscale = scales[scalesindex]['v'];
		updateCharset();

		controlcodesSwitch(machine);

		document.getElementById("color_set").selectedIndex = colindex;
		document.getElementById("aspectratio").selectedIndex = scalesindex;

		var sel = document.getElementById('charset');
		var opts = sel.options;
		for (var opt, j = 0; opt = opts[j]; j++) {
			if (opt.value == gcharset) {
				sel.selectedIndex = j;
				break;
			}
		}

		var sel = document.getElementById('controlcodes');
		var opts = sel.options;
		for (var opt, j = 0; opt = opts[j]; j++) {
			if (opt.value == machine) {
				sel.selectedIndex = j;
				break;
			}
		}
	}
}

function showItems(name) {
	items = document.getElementsByClassName(name)
	var i;
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.display = null;
	}
}

function hideItems(name) {
	items = document.getElementsByClassName(name)
	var i;
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.display = "none";
	}
}

function unicodeSwitch(index) {
	if (index == 0) {
		showItems("unicode_upper");
		hideItems("unicode_lower");
	} else if (index == 1) {
		hideItems("unicode_upper");
		showItems("unicode_lower");
	}
}

function caseSwitch(index) {
	if (index == 0) {
		showItems("table_upper");
		showItems("table_lower");
	} else if (index == 1) {
		showItems("table_upper");
		hideItems("table_lower");
	} else if (index == 2) {
		hideItems("table_upper");
		showItems("table_lower");
	}
}

function petsciiTableSwitch(index) {
	if (index == 0) {
		showItems("petscii_keyboard");
		hideItems("petscii_control");
	} else if (index == 1) {
		hideItems("petscii_keyboard");
		showItems("petscii_control");
	} else if (index == 2) {
		showItems("petscii_keyboard");
		showItems("petscii_control");
	}
	// hide machines that are disabled
	var items = document.getElementsByClassName("machine_checkbox");
	for (i = 0; i < items.length; i++) {
		if (!items[i].checked) {
			machine = items[i].id.substring(9);
			var items2 = document.getElementsByClassName(machine);
			for (j = 0; j < items2.length; j++) {
				var currentItem = items2[j];
				currentItem.style.display = "none";
			}
		}
	}
}

var gmodifier = 'regular';

function highlight_key(machine, scancode, petscii_regular, petscii_shift, petscii_cbm, petscii_ctrl, modifier) {
	clear_all = false;
	if (modifier == '') {
		// a printabe key was pressed
		if (gmodifier == 'regular') {
			petscii = petscii_regular;
			clear_all = true;
		} else if (gmodifier == 'shift') {
			petscii = petscii_shift;
		} else if (gmodifier == 'cbm') {
			petscii = petscii_cbm;
		} else if (gmodifier == 'ctrl') {
			petscii = petscii_ctrl;
		}
		if (petscii != 'petscii_0xff') {
			test(petscii);
		} else {
			test(null)
		}
		gmodifier = 'regular';
	} else {
		// a modifier was pressed
		clear_all = true;
		gmodifier = modifier
	}

	if (clear_all) {
		items = document.getElementsByClassName('keyrect')
		for (i = 0; i < items.length; i++) {
			var currentItem = items[i];
			currentItem.style.fill = 'white';
		}
		items = document.getElementsByClassName('keytext')
		for (i = 0; i < items.length; i++) {
			var currentItem = items[i];
			currentItem.style.fill = 'black';
		}
	}

	items = document.getElementsByClassName('keyrect_' + machine + '_' + scancode)
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.fill = 'gray';
	}
	items = document.getElementsByClassName('keytext_' + machine + '_' + scancode)
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.fill = 'white';
	}
}
