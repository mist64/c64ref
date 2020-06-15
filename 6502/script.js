window.onload = init;

const cpus = [
	'6502',
	'6502rorbug',
	'65dtv02',
	'65c02',
	'r65c02',
	'65c02s',
	'65ce02',
	'65c816',
]

const all_sorted_addmodes = [
	'#d8',
	'#d16',
	'a16',
	'a8',
	'A',
	'-',
	'(a16,X)',
	'(a8),Y',
	'(a8)',
	'(a8),Z', // same as above
	'[a8]',
	'(r8,SP),Y',
	'a8,X',
	'a8,Y',
	'a16,X',
	'a16,Y',
	'r8',
	'r16',
	'(a16)',
	'[a16]',
	'(a16,X)',
	'a8,r8',
	'(a8,X)',
	'a24',
	'a24,X',
	'src,dest',
	'a8,S',
	'(a8,S),Y',
];

const all_sorted_categories = [
	'load',
	'trans',
	'stack',
	'shift',
	'logic',
	'arith',
	'inc',
	'ctrl',
	'bra',
	'flags',
	'kil',
	'nop',
];

var cpu_data = {};

var files_loaded = 0;
var file_data = {};
var cpu;
var showillegal;
var separateillegal;

function filename_for_cpu_and_type(cpu, type) {
	return 'cpu_' + cpu + '_' + type + '.txt';
}

function init() {
	var files_to_load = [];
	for (var i = 0; i < cpus.length; i++) {
		var cpu = cpus[i];
		for (var type of ['opcodes', 'operations', 'mnemos', 'addmodes', 'timing']) {
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
					for (var cpu of cpus) {
						cpu_data[cpu] = {};
						decode_opcodes(cpu);
						decode_operations(cpu);
						decode_mnemos(cpu);
						decode_addmodes(cpu);
						decode_timing(cpu);
					}
					show();
				}
			} else {
				file_data[r.file_to_load.filename] = null;
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
	cpu_data[cpu].opcodes = [];
	for (var i = 0; i <= 255; i++) {
		cpu_data[cpu].opcodes[i] = {};
	}
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var o = parseInt(line[0], 16);
		var mnemo = line[1];
		cpu_data[cpu].opcodes[o].illegal = false;
		if (mnemo.startsWith('*')) {
			mnemo = mnemo.substring(1);
			cpu_data[cpu].opcodes[o].illegal = true;
		}
		cpu_data[cpu].opcodes[o].mnemo = mnemo;
		cpu_data[cpu].opcodes[o].addmode = line[2] ? line[2] : '-';
	}
}
function decode_operations(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'operations')];
	text = decode_text(text);
	cpu_data[cpu].operations = {};
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var mnemo = line[0];
		cpu_data[cpu].operations[mnemo] = {};
		cpu_data[cpu].operations[mnemo].category = line[1];
		cpu_data[cpu].operations[mnemo].flags = line[2];
		cpu_data[cpu].operations[mnemo].description = line.slice(3).join(' ');
	}
}

function decode_mnemos(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'mnemos')];
	text = decode_text(text);
	cpu_data[cpu].mnemos = {};
	for (var line of text) {
		var mnemo = line[0];
		var description = line.slice(1).join(' ');
		if (description) {
			cpu_data[cpu].mnemos[mnemo] = {};
			cpu_data[cpu].mnemos[mnemo].description = description;
		} else {
			delete cpu_data[cpu].mnemos[mnemo];
		}
	}
}

function decode_addmodes(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'addmodes')];
	text = decode_text(text);
	cpu_data[cpu].addmodes = {};
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var addmode = line[0];
		cpu_data[cpu].addmodes[addmode] = {};
		cpu_data[cpu].addmodes[addmode].bytes = line[1];
		cpu_data[cpu].addmodes[addmode].syntax = line[2] != '-' ? line[2] : '';
		cpu_data[cpu].addmodes[addmode].description = line.slice(3).join(' ');
	}
}

function decode_timing(cpu) {
	text = file_data[filename_for_cpu_and_type(cpu, 'timing')];
	text = decode_text(text);
	for (var i = 0; i < text.length; i++) {
		var line = text[i];
		var o = parseInt(line[0], 16);
		cpu_data[cpu].opcodes[o].cycles = line[1];
	}
}

function opcodes_for_mnemo_and_addmode(mnemo, addmode) {
	var res = [];
	for (var i = 0; i <= 255; i++) {
		if (cpu_data[cpu].opcodes[i].mnemo == mnemo && cpu_data[cpu].opcodes[i].addmode == addmode) {
			res.push(i);
		}
	}
	return res;
}

function cpu_has_illegal(cpu) {
	for (var i = 0; i <= 255; i++) {
		if (cpu_data[cpu].opcodes[i].illegal) {
			return true;
		}
	}
	return false;
}

function show() {
	cpu = document.getElementById('cpu').value;
	showillegal = document.getElementById('showillegal').checked;
	separateillegal = document.getElementById('separateillegal').checked;
	var has_illegal = cpu_has_illegal(cpu);

	document.getElementById('showillegal_box').style.display = has_illegal ? '' : 'none';
	document.getElementById('separateillegal_box').className = showillegal ? '' : 'disabled';

	var filter1, filter2;
	if (showillegal && has_illegal) {
		if (separateillegal) {
			filter1 = 'regular';
			filter2 = 'illegal';
		} else {
			filter1 = 'all';
			filter2 = 'none';
		}
	} else {
			filter1 = 'regular';
			filter2 = 'none';
	}

	generate_opcode_table();
	generate_mnemos_by_category();
	generate_opcode_cycle_reference('cycle_reference1', 'cycle', filter1);
	generate_opcode_cycle_reference('cycle_reference2', 'cycle', filter2);
	generate_opcode_cycle_reference('opcode_reference1', 'opcode', filter1);
	generate_opcode_cycle_reference('opcode_reference2', 'opcode', filter2);
	generate_big_table('big_table1', filter1);
	generate_big_table('big_table2', filter2);
	generate_reference();
}

function o_from_x_y(x, y, opcode_table_organization) {
	if (opcode_table_organization == '4-4') {
		return y << 4 | x;
	} else if (opcode_table_organization == '3-3-2a/h') {
		var a = x & 7;
		var b = y & 7;
		var c = x >> 3;
		return a << 5 | b << 2 | c;
	} else if (opcode_table_organization == '3-3-2a/v') {
		var a = x & 7;
		var b = y & 7;
		var c = y >> 3;
		return a << 5 | b << 2 | c;
	} else if (opcode_table_organization == '3-3-2b/h') {
		var a = y & 7;
		var b = x & 7;
		var c = x >> 3;
		return a << 5 | b << 2 | c;
	} else if (opcode_table_organization == '3-3-2b/v') {
		var a = y & 7;
		var b = x & 7;
		var c = y >> 3;
		return a << 5 | b << 2 | c;
	}
}

function generate_opcode_table() {
	opcode_table_organization = document.getElementById('opcode_table_organization').value;

	var opcode_table = document.getElementById('opcode_table');
	opcode_table.innerHTML = '';

	if (opcode_table_organization == '4-4') {
		var limx = 16;
		var limy = 16;
	} else if (opcode_table_organization.slice(-1) == 'h') {
		var limx = 32;
		var limy = 8;
	} else {
		var limx = 8;
		var limy = 32;
	}

	var tr = document.createElement("tr");
	opcode_table.appendChild(tr);
	var th = document.createElement("th");
	tr.appendChild(th);
	for (var x = 0; x < limx; x++) {
		var th = document.createElement("th");
		tr.appendChild(th);
		if (opcode_table_organization == '4-4') {
			th.innerHTML = 'x' + x.toString(16).toUpperCase()
		} else {
			var o = o_from_x_y(x, 0, opcode_table_organization);
			th.innerHTML = hex16(o);
		}
	}

	for (var y = 0; y < limy; y++) {
		var tr = document.createElement("tr");
		opcode_table.appendChild(tr);
		var th = document.createElement("th");
		tr.appendChild(th);
		if (opcode_table_organization == '4-4') {
			th.innerHTML = y.toString(16).toUpperCase() + 'x';
		} else {
			var o = o_from_x_y(0, y, opcode_table_organization);
			th.innerHTML = hex16(o);
		}
		for (var x = 0; x < limx; x++) {
			var td = document.createElement("td");
			tr.appendChild(td);
			var o = o_from_x_y(x, y, opcode_table_organization);
			var opcode = cpu_data[cpu].opcodes[o];

			if (opcode.mnemo && (showillegal || !opcode.illegal)) {
				td.className += ' ' + cpu_data[cpu].operations[opcode.mnemo].category;
				if (opcode.illegal) {
					td.className += ' ill';
				}
				var addmode = cpu_data[cpu].opcodes[o].addmode;
				var cell = cpu_data[cpu].opcodes[o].mnemo + '<br/>';
				if (addmode != '-') {
					cell += addmode;
				}
				cell += '<br/>';
				if (cpu_data[cpu].opcodes[o].cycles) {
					cell += '<span style="float: left;">' + cpu_data[cpu].opcodes[o].cycles
					cell += '</span>';
					cell += '<span style="float: right;">' + cpu_data[cpu].addmodes[addmode].bytes;
					cell += '</span>';
				}
//				cell += '<br/>' + cpu_data[cpu].operations[opcode.mnemo].flags;
				td.innerHTML = cell;
			} else {
				td.className += ' undefined';
			}
//			td.innerHTML = hex16(o);
		}
	}
}

function hex16(a) {
	return ('0' + a.toString(16).toUpperCase()).slice(-2);
}

function pretty_cycles(opcode) {
	var cycles = opcode.cycles;
	if (cycles == null) {
		return '&infin;';
	} else {
		return cycles;
	}
}

function generate_mnemos_by_category() {
	var mnemos_by_category = document.getElementById('mnemos_by_category');
	mnemos_by_category.innerHTML = '';

	// collect data
	var data = [];
	for (var category of all_sorted_categories) {
		var column = [ category ];
		for (mnemo of Object.keys(cpu_data[cpu].operations)) {
			if (cpu_data[cpu].operations[mnemo].category == category) {

				var show = false;
				for (var addmode of all_sorted_addmodes) {
					var opcodes = opcodes_for_mnemo_and_addmode(mnemo, addmode);
					for (var opcode of opcodes) {
						if (showillegal || !cpu_data[cpu].opcodes[opcode].illegal) {
							show = true;
							break;
						}
					}
					if (show) {
						break;
					}
				}
				if (show) {
					column.push(mnemo);
				}
			}
		}
		data.push(column);
	}

	// build table
	tr = document.createElement("tr");
	mnemos_by_category.appendChild(tr);
	for (var column of data) {
		if (column.length == 1) {
			continue;
		}
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = column[0];
	}
	tr = document.createElement("tr");
	mnemos_by_category.appendChild(tr);
	for (var column of data) {
		if (column.length == 1) {
			continue;
		}
		var html = '';
		for (var line of column.slice(1).sort()) {
			html += line +  '<br/>'
		}

		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = html;
		td.className = column[0];
	}
}

function generate_opcode_cycle_reference(id, which, filter) {
	var cycle_reference = document.getElementById(id);
	cycle_reference.innerHTML = '';

	if (filter == 'none') {
		return;
	}

	tr = document.createElement("tr");
	cycle_reference.appendChild(tr);
	th = document.createElement("th");
	tr.appendChild(th);

	var all_mnemos = Object.keys(cpu_data[cpu].operations).sort();
	var mnemos = [];
	for (var mnemo of all_mnemos) {
		var found = false;
		for (var addmode of all_sorted_addmodes) {
			var opcodes = opcodes_for_mnemo_and_addmode(mnemo, addmode);
			for (var opcode of opcodes) {
				if (filter == 'regular' && cpu_data[cpu].opcodes[opcode].illegal) {
					continue;
				}
				if (filter == 'illegal' && !cpu_data[cpu].opcodes[opcode].illegal) {
					continue;
				}
				found = true;
				break;
			}
			if (found) {
				break;
			}
		}
		if (found) {
			mnemos.push(mnemo);
		}
	}
	console.log(filter, mnemos);

	for (var addmode of all_sorted_addmodes) {
		th = document.createElement("th");
		tr.appendChild(th);
		if (cpu_data[cpu].addmodes[addmode]) {
			th.innerHTML = cpu_data[cpu].addmodes[addmode].description;
//			th.innerHTML = cpu_data[cpu].addmodes[addmode].syntax;
		}
//		th.className = 'vertical';
	}
	for (var mnemo of mnemos) {
		tr = document.createElement("tr");
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = mnemo;
		var row_is_empty = true;
		for (var addmode of all_sorted_addmodes) {
			td = document.createElement("td");
			tr.appendChild(td);
			var opcodes = opcodes_for_mnemo_and_addmode(mnemo, addmode);
			if (opcodes.length) {
				var opcode = opcodes[0];
				if (which == 'opcode') {
					td.innerHTML = hex16(opcode);
				} else {
					td.innerHTML = pretty_cycles(cpu_data[cpu].opcodes[opcode]);

				}
				row_is_empty = false;
			}
		}
		if (!row_is_empty) {
			cycle_reference.appendChild(tr);
		}
	}
}

function generate_big_table(id, filter) {
	var big_table = document.getElementById(id);
	big_table.innerHTML = '';

	if (filter == 'none') {
		return;
	}

	tr = document.createElement("tr");
	big_table.appendChild(tr);

	var addmodes = [];
	for (var addmode of all_sorted_addmodes) {
		if (Object.keys(cpu_data[cpu].addmodes).includes(addmode)) {
			addmodes.push(addmode);
		}
	}

	for (var title of ['Mnemonic', 'Operation']) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = title;
	}
	for (var addmode of addmodes) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.colSpan = 3;
		th.innerHTML = cpu_data[cpu].addmodes[addmode].syntax;
	}
	th = document.createElement("th");
	tr.appendChild(th);
	th.colSpan = 8;
	th.innerHTML = 'Flags';

	tr = document.createElement("tr");
	big_table.appendChild(tr);
	th = document.createElement("th");
	tr.appendChild(th);
	th = document.createElement("th");
	tr.appendChild(th);
	for (var addmode of addmodes) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = 'OP';
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = 'N';
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = '#';
	}
	for (var i = 0; i < 8; i++) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = 'NV#BDIZC'[i];
	}


	for (var mnemo of Object.keys(cpu_data[cpu].operations).sort()) {
		var h2, table, tr, td, th, p;

		tr = document.createElement("tr");

		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = mnemo;
		td.className = cpu_data[cpu].operations[mnemo].category;

		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = cpu_data[cpu].operations[mnemo].description;

		var row_is_empty = true;
		for (var addmode of addmodes) {
			var td1 = document.createElement("td");
			var td2 = document.createElement("td");
			var td3 = document.createElement("td");
			tr.appendChild(td1);
			tr.appendChild(td2);
			tr.appendChild(td3);
			var opcodes = opcodes_for_mnemo_and_addmode(mnemo, addmode);
			for (var opcode of opcodes) {
				if (filter == 'regular' && cpu_data[cpu].opcodes[opcode].illegal) {
					continue;
				}
				if (filter == 'illegal' && !cpu_data[cpu].opcodes[opcode].illegal) {
					continue;
				}
				var cycles = pretty_cycles(cpu_data[cpu].opcodes[opcode]);
				td1.innerHTML += hex16(opcode) + '<br/>';
				td2.innerHTML += cpu_data[cpu].addmodes[addmode].bytes + '<br/>';
				td3.innerHTML += cycles + '<br/>';
				row_is_empty = false;
			}
		}
		if (!row_is_empty) {
			big_table.appendChild(tr);
		}

		for (var i = 0; i < 8; i++) {
			td = document.createElement("td");
			tr.appendChild(td);
			var flag = cpu_data[cpu].operations[mnemo].flags[i];
			switch (flag) {
				case '-':
				case '0':
				case '1':
					td.innerHTML = flag;
					break;
				default:
					td.innerHTML = 'NV#BDIZC'[i];
					break;
			}
		}
	}
}

function generate_reference() {
	var reference = document.getElementById('reference');
	reference.innerHTML = '';

	for (var mnemo of Object.keys(cpu_data[cpu].operations).sort()) {
		var div = document.createElement("div");
		var num_rows = 0;

		// heading
		var h2, table, tr, td, th, p;
		h2 = document.createElement("h2");
		div.appendChild(h2);
		var title = mnemo;
		if (cpu_data[cpu].mnemos[mnemo]) {
			title += ' - ' + cpu_data[cpu].mnemos[mnemo].description;
		}
		h2.innerHTML =  title;

		// description
		p = document.createElement("p");
		div.appendChild(p);
		p.innerHTML = 'Operation: ' + cpu_data[cpu].operations[mnemo].description;

		// flags
		table = document.createElement("table");
		div.appendChild(table);
		table.border = 1;
		tr = document.createElement("tr");
		table.appendChild(tr);
		for (var title of ['N', 'V', '#', 'B', 'D', 'I', 'Z', 'C']) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.innerHTML = title;
		}
		tr = document.createElement("tr");
		table.appendChild(tr);
		for (var i = 0; i < 8; i++) {
			td = document.createElement("td");
			tr.appendChild(td);
			var flag = cpu_data[cpu].operations[mnemo].flags[i];
			switch (flag) {
				case '-':
				case '0':
				case '1':
					td.innerHTML = flag;
					break;
				default:
					td.innerHTML = '&#10003;';
					break;
			}
		}

		// addressing mode table
		table = document.createElement("table");
		table.border = 1;
		div.appendChild(table);
		tr = document.createElement("tr");
		table.appendChild(tr);
		for (var title of ['Addressing Mode', 'Assembly Language Form', 'Opcode', 'No. Bytes', 'No. Cycles']) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.innerHTML = title;
		}
		var show_illegal_footnote = false;
		for (var addmode of Object.keys(cpu_data[cpu].addmodes)) {
			var opcodes = opcodes_for_mnemo_and_addmode(mnemo, addmode);
			for (var opcode of opcodes) {
				var illegal = cpu_data[cpu].opcodes[opcode].illegal;
				if (showillegal || !illegal) {
					num_rows++;

					tr = document.createElement("tr");
					table.appendChild(tr);
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = cpu_data[cpu].addmodes[addmode].description;
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = mnemo + ' ' + cpu_data[cpu].addmodes[addmode].syntax;
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = '$' + hex16(opcode);
					if (illegal) {
						td.innerHTML += '*';
						show_illegal_footnote = true;
					}
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = cpu_data[cpu].addmodes[addmode].bytes;
					td = document.createElement("td");
					tr.appendChild(td);
					var cycles = cpu_data[cpu].opcodes[opcode].cycles;
					if (cycles == null) {
						td.innerHTML = '&infin;';
					} else {
						td.innerHTML = cycles;
					}
				}
			}
		}
		if (show_illegal_footnote) {
			p = document.createElement("p");
			div.appendChild(p);
			p.innerHTML = '*Undocumented.';
		}

		// if there were no opcodes, don't add the div
		// this happens if
		// * all opcodes were illegal and illegals were disabled
		// * the mnemo was inherited, and the current CPU doesn't have it
		if (num_rows) {
			reference.appendChild(div);
		}

	}
}
// TODO:
// * # vs E
// * (zp) vs (zp),z
// * stz vs stz
// * add some more description text
// * switch between illop synonym sets
// * combine files
// * CPU summary text
// * CPU tree
