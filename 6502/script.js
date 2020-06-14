window.onload = init;

const cpus = [
	'6502',
	'6502ill',
]

var files_loaded = 0;
var file_data = {};
var opcodes = [];
var operations = {};
var addmodes = {};

function filename_for_cpu_and_type(cpu, type) {
	return 'cpu_' + cpu + '_' + type + '.txt';
}

function init() {
	var files_to_load = [];
	for (var i = 0; i < cpus.length; i++) {
		var cpu = cpus[i];
		for (var type of ['opcodes', 'operations', 'addmodes', 'timing']) {
			files_to_load.push({
				cpu: cpu,
				type: type,
				filename: filename_for_cpu_and_type(cpu, type),
			});
		}
	}

	for (var i = 0; i < files_to_load.length; i++) {
		var r = new XMLHttpRequest();
		r.file_to_load = files_to_load[i];
		r.open("GET", r.file_to_load.filename, false);
		r.onload = function() {
			if (r.status == 200 || r.status == 0) {
				file_data[r.file_to_load.filename] = r.responseText;
				files_loaded++;
				if (files_loaded == files_to_load.length) {
					var cpu = '6502ill';
					decode_opcodes(cpu);
					decode_operations(cpu);
					decode_addmodes(cpu);
					decode_timing(cpu);
					show();
				}
			} else {
				file_data[r.file_to_load.filename] = undefined;
			}
		}
		r.send(null);
	}
}

function decode_text(text) {
	text = text.split('\n');
	var text2 = [];
	for (var i = 0; i < text.length; i++) {
		line = text[i].trim();
		if (!line) {
			continue;
		}
		line = line.split(/\s+/);
		if (line[0] == '.basedon') {
			var other_text = decode_text(file_data[line[1]]);
			text2 = text2.concat(other_text);
		} else {
			text2.push(line);
		}
	}
	return text2;
}

function decode_opcodes(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'opcodes')];
	text = decode_text(text);
	for (var i = 0; i <= 255; i++) {
		opcodes[i] = {};
	}
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var o = parseInt(line[0], 16);
		var mnemo = line[1];
		opcodes[o].illegal = false;
		if (mnemo.startsWith('*')) {
			mnemo = mnemo.substring(1);
			opcodes[o].illegal = true;
		}
		opcodes[o].mnemo = mnemo;
		opcodes[o].addmode = line[2];
	}
	console.log(opcodes);
}
function decode_operations(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'operations')];
	text = decode_text(text);
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var mnemo = line[0];
		operations[mnemo] = {};
		operations[mnemo].flags = line[1];
		operations[mnemo].type = line[2];
		operations[mnemo].description = line.slice(3).join(' ');
	}
}

function decode_addmodes(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'addmodes')];
	text = decode_text(text);
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var addmode = line[0];
		addmodes[addmode] = {};
		addmodes[addmode].syntax = line[1] != '-' ? line[1] : '';
		addmodes[addmode].description = line[2];
	}
}

function decode_timing(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'timing')];
	text = decode_text(text);
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var o = parseInt(line[0], 16);
		var cycles = line[1];
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
	}
}

function show() {
//	console.log(opcodes);
//	console.log(operations);
//	console.log(addmodes);

	var opcode_table = document.getElementById('opcode_table');
	for (var y = 0; y < 16; y++) {
		var tr = document.createElement("tr");
		opcode_table.appendChild(tr);
		for (var x = 0; x < 16; x++) {
			var td = document.createElement("td");
			tr.appendChild(td);
			td.className = 'opcodecell';
			var o = y << 4 | x;
			var opcode = opcodes[o];

			if (opcode.mnemo) {
				td.className += '  ' + operations[opcode.mnemo].type;
				if (opcode.illegal) {
					td.className += ' ill';
				}
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
			} else {
				td.innerHTML = '-';
			}
		}
	}
}

// TODO:
// * 6502 without ROR

