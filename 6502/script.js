window.onload = init;

function init() {
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", 'cpu_6502.txt', false);
	rawFile.onload = function ()
	{
		present(rawFile.responseText);
	}
	rawFile.send(null);
}

function present(text) {
	div = document.getElementById('test');
	div.innerHTML = text;
	text = text.split('\n');
	var section = '';
	var opcodes = [];
	var operations = {};
	for (var i = 0; i <= 255; i++) {
		opcodes[i] = {};
	}
	for (var i = 0; i < text.length; i++) {
		line = text[i].trim();
		if (!line) {
			continue;
		}
		if (line.startsWith('-')) {
			section = line.substring(2);
			console.log(section);
			continue;
		}
		switch (section) {
			case 'opcodes':
				line = line.split(/\s+/);
				var o = parseInt(line[0], 16);
				var mnemo = line[1];
				if (mnemo.startsWith('*')) {
					mnemo = mnemo.substring(1);
					opcodes[o].illegal = true;
				}
				opcodes[o].illegal = false;
				opcodes[o].mnemo = mnemo;
				opcodes[o].addmode = line[2];
				var cycles = line[3];
				opcodes[o].extracycle = false;
				if (cycles == 'X') {
					cycles = undefined;
				} else {
					if (cycles.endsWith('*')) {
						opcodes[o].extracycle = true;
						cycles = cycles.substring(0, cycles.length - 1);
					}
					cycles = parseInt(cycles);
				}
				opcodes[o].cycles = cycles;
				break;
			case 'mnemos':
				line = line.split(/\s+/);
				var mnemo = line[0];
				operations[mnemo] = {};
				operations[mnemo].flags = line[1];
				operations[mnemo].description = line.slice(2).join(' ');
				break;
			case 'addmodes':
				console.log(line);
				break;
		}
	}
//	console.log(opcodes);
//	console.log(operations);
}
