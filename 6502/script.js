window.onload = init;

const filename_opcodes = 'cpu_6502_opcodes.txt';
const filename_operations = 'cpu_6502_operations.txt';
const filename_addmodes = 'cpu_6502_addmodes.txt';

function init() {
	var req1 = new XMLHttpRequest();
	req1.open("GET", filename_opcodes, false);
	req1.onload = function() {
		decode_opcodes(req1.responseText);
		var req2 = new XMLHttpRequest();
		req2.open("GET", filename_operations, false);
		req2.onload = function() {
			decode_operations(req2.responseText);
			var req3 = new XMLHttpRequest();
			req3.open("GET", filename_addmodes, false);
			req3.onload = function() {
				decode_operations(req3.responseText);
				show();
			}
			req3.send(null);
		}
		req2.send(null);
	}
	req1.send(null);
}

var opcodes = [];
var operations = {};
var addmodes = {};

function tidy_text(text) {
	text = text.split('\n');
	var text2 = [];
	for (var i = 0; i < text.length; i++) {
		line = text[i].trim();
		if (!line) {
			continue;
		}
		line = line.split(/\s+/);
		text2.push(line);
	}
	return text2;
}

function decode_opcodes(text) {
	text = tidy_text(text);
	for (var i = 0; i <= 255; i++) {
		opcodes[i] = {};
	}
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
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
	}
}
function decode_operations(text) {
	text = tidy_text(text);
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var mnemo = line[0];
		operations[mnemo] = {};
		operations[mnemo].flags = line[1];
		operations[mnemo].type = line[2];
		operations[mnemo].description = line.slice(3).join(' ');
	}
}

function decode_addmodes(text) {
	text = tidy_text(text);
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var addmode = line[0];
		addmodes[addmode] = {};
		addmodes[addmode].syntax = line[1] != '-' ? line[1] : '';
		addmodes[addmode].description = line[2];
	}
}

function show() {
//	console.log(opcodes);
//	console.log(operations);
	console.log(addmodes);

	var opcode_table = document.getElementById('opcode_table');
	for (var y = 0; y < 16; y++) {
		var tr = document.createElement("tr");
		opcode_table.appendChild(tr);
		for (var x = 0; x < 16; x++) {
			var td = document.createElement("td");
			tr.appendChild(td);
			var o = y << 4 | x;
//			console.log(opcodes[o].mnemo,operations[opcodes[o].mnemo].type);
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

