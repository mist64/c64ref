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
	text = text.split('\n');
	var section = '';
	var opcodes = [];
	var operations = {};
	var addmodes = {};
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
		line = line.split(/\s+/);
		switch (section) {
			case 'opcodes':
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
			case 'operations':
				var mnemo = line[0];
				operations[mnemo] = {};
				operations[mnemo].flags = line[1];
				operations[mnemo].type = line[2];
				operations[mnemo].description = line.slice(3).join(' ');
				break;
			case 'addmodes':
				var addmode = line[0];
				addmodes[addmode] = {};
				addmodes[addmode].description = line[1] ? line[1] : '';
				break;
		}
	}
//	console.log(opcodes);
	console.log(operations);
//	console.log(addmodes);

	var opcode_table = document.getElementById('opcode_table');
	for (var y = 0; y < 16; y++) {
		var tr = document.createElement("tr");
		opcode_table.appendChild(tr);
		for (var x = 0; x < 16; x++) {
			var td = document.createElement("td");
			tr.appendChild(td);
			var o = y << 4 | x;
			console.log(opcodes[o].mnemo,operations[opcodes[o].mnemo].type);
			td.className = operations[opcodes[o].mnemo].type;
			var cell = opcodes[o].mnemo + '</br>';
			if (opcodes[o].addmode != 'imp') {
				cell += opcodes[o].addmode + ' ';
			}
			if (opcodes[o].cycles) {
				cell += opcodes[o].cycles;
			}
			if (opcodes[o].extracycle) {
				cell += '*';
			}
			td.innerHTML = cell;
		}
	}
}

// TODO:
// * 6502 without ROR

