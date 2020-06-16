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

function filename_for_cpu(cpu, type) {
	return 'cpu_' + cpu + '.txt';
}

function init() {
	for (var cpu of cpus) {
		var r = new XMLHttpRequest();
		r.cpu = cpu;
		r.open("GET", filename_for_cpu(cpu), false);
		r.onload = function() {
			if (r.status == 200 || r.status == 0) {
				split_file_data(r.cpu, r.responseText);
				files_loaded++;
				if (files_loaded == cpus.length) {
					for (var cpu of cpus) {
						cpu_data[cpu] = {};
						decode_info(cpu);
						decode_opcodes(cpu);
						decode_operations(cpu);
						decode_mnemos(cpu);
						decode_addmodes(cpu);
						decode_timing(cpu);
						fixup_data(cpu);
					}
					show();
				}
			} else {
				file_data[r.cpu] = null;
			}
		}
		r.send(null);
	}
}

function get_file_data(cpu, section) {
	var text = file_data[cpu][section].text;
	if (!text) {
		text = [];
	}
	if (cpu_data[cpu].info && cpu_data[cpu].info.basedon) {
		var other_text = get_file_data(cpu_data[cpu].info.basedon, section);
		text = other_text.concat(text);
	}
	return text;
}

function split_file_data(cpu, text) {
	var lines_in = text.split('\n');
	var data_out = {};
	var section = null;
	for (var line of lines_in) {
		line = line.split(';')[0]; // remove comments
		line = line.trim();
		if (!line) {
			continue;
		} else 	if (line[0] == '[' && line[line.length - 1] == ']') {
			section = line.substr(1, line.length - 2);
			data_out[section] = {};
		} else {
			line = line.split(/\s+/);
			if (section) {
				if (!data_out[section].text) {
					data_out[section].text = [];
				}
				data_out[section].text.push(line);
			}
		}
	}
	file_data[cpu] = data_out;
}

function decode_info(cpu) {
	text = get_file_data(cpu, 'info');
	cpu_data[cpu].info = {};
	for (var line of text) {
		cpu_data[cpu].info[line[0]] = line.slice(1).join(' ');
	}
}

function decode_opcodes(cpu) {
	text = get_file_data(cpu, 'opcodes');
	cpu_data[cpu].opcodes = [];
	for (var i = 0; i <= 255; i++) {
		cpu_data[cpu].opcodes[i] = {};
	}
	for (var line of text) {
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
	text = get_file_data(cpu, 'operations');
	cpu_data[cpu].operations = {};
	for (var line of text) {
		var mnemo = line[0];
		cpu_data[cpu].operations[mnemo] = {};
		cpu_data[cpu].operations[mnemo].category = line[1];
		cpu_data[cpu].operations[mnemo].flags = line[2];
		cpu_data[cpu].operations[mnemo].description = line.slice(3).join(' ');
	}
}

function decode_mnemos(cpu) {
	text = get_file_data(cpu, 'mnemos');
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
	text = get_file_data(cpu, 'addmodes');
	cpu_data[cpu].addmodes = {};
	for (var line of text) {
		var addmode = line[0];
		cpu_data[cpu].addmodes[addmode] = {};
		cpu_data[cpu].addmodes[addmode].bytes = line[1];
		cpu_data[cpu].addmodes[addmode].syntax = line[2] != '-' ? line[2] : '';
		cpu_data[cpu].addmodes[addmode].description = line.slice(3).join(' ');
	}
}

function decode_timing(cpu) {
	text = get_file_data(cpu, 'timing');
	for (var line of text) {
		var o = parseInt(line[0], 16);
		cpu_data[cpu].opcodes[o].cycles = line[1];
	}
}

function should_show(filter, opcode) {
	if (filter == 'regular' && opcode.illegal) {
		return false;
	}
	if (filter == 'illegal' && !opcode.illegal) {
		return false;
	}
	return true;
}

function fixup_data(cpu) {
	// get all used mnemos
	var mnemos = Object.keys(cpu_data[cpu].operations).sort();
	cpu_data[cpu].all_mnemos = {};
	for (var filter of ['regular', 'illegal', 'all']) {
		cpu_data[cpu].all_mnemos[filter] = [];
		for (var mnemo of mnemos) {
			var found = false;
			for (var addmode of all_sorted_addmodes) {
				var opcodes = opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter);
				for (var opcode of opcodes) {
					if (should_show(filter, cpu_data[cpu].opcodes[opcode])) {
						found = true;
						break;
					}
				}
				if (found) {
					break;
				}
			}
			if (found) {
				cpu_data[cpu].all_mnemos[filter].push(mnemo);
			}
		}
	}

	// get all used addmodes
	var mnemos = Object.keys(cpu_data[cpu].operations).sort();
	cpu_data[cpu].all_addmodes = {};
	for (var filter of ['regular', 'illegal', 'all']) {
		cpu_data[cpu].all_addmodes[filter] = [];
		for (var addmode of all_sorted_addmodes) {
			var found = false;
			for (var mnemo of mnemos) {
				var opcodes = opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter);
				for (var opcode of opcodes) {
					if (should_show(filter, cpu_data[cpu].opcodes[opcode])) {
						found = true;
						break;
					}
				}
				if (found) {
					break;
				}
			}
			if (found) {
				cpu_data[cpu].all_addmodes[filter].push(addmode);
			}
		}
	}
}

function opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter) {
	var res = [];
	for (var opcode = 0; opcode <= 255; opcode++) {
		if (cpu_data[cpu].opcodes[opcode].mnemo == mnemo && cpu_data[cpu].opcodes[opcode].addmode == addmode) {
			if (filter == 'regular' && cpu_data[cpu].opcodes[opcode].illegal) {
				continue;
			}
			if (filter == 'illegal' && !cpu_data[cpu].opcodes[opcode].illegal) {
				continue;
			}
			res.push(opcode);
		}
	}
	return res;
}

function cpu_has_illegal(cpu) {
	for (var opcode of cpu_data[cpu].opcodes) {
		if (opcode.illegal) {
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

	generate_opcode_table('opcode_table1', filter1);
	generate_opcode_table('opcode_table2', filter2);
	generate_mnemos_by_category('mnemos_by_category', filter1);
	generate_opcode_cycle_reference('cycle_reference1', 'cycle', filter1);
	generate_opcode_cycle_reference('cycle_reference2', 'cycle', filter2);
	generate_opcode_cycle_reference('opcode_reference1', 'opcode', filter1);
	generate_opcode_cycle_reference('opcode_reference2', 'opcode', filter2);
	generate_big_table('big_table1', filter1);
	generate_big_table('big_table2', filter2);
	generate_reference('reference', 'all');
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

function generate_opcode_table(id, filter) {
	opcode_table_organization = document.getElementById('opcode_table_organization').value;

	var opcode_table = document.getElementById(id);
	opcode_table.innerHTML = '';

	if (filter == 'none') {
		return;
	}

	if (opcode_table_organization == '4-4') {
		var limx = 16;
		var limy = 16;
		var shape = 's';
	} else if (opcode_table_organization.slice(-1) == 'h') {
		var limx = 32;
		var limy = 8;
		var shape = 'h';
	} else {
		var limx = 8;
		var limy = 32;
		var shape = 'v';
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
			if (shape == 'h' && (x == 7 || x == 15 || x == 23)) {
				td.style.borderRight = '8px solid white';
			}
			if (shape == 'v' && (y == 7 || y == 15 || y == 23)) {
				td.style.borderBottom = '8px solid white';
			}
			var o = o_from_x_y(x, y, opcode_table_organization);
			var opcode = cpu_data[cpu].opcodes[o];

			if (opcode.mnemo && should_show(filter, opcode)) {
				td.className += ' ' + cpu_data[cpu].operations[opcode.mnemo].category;
				if (opcode.illegal) {
					td.className += ' ill';
				}
				var addmode = cpu_data[cpu].opcodes[o].addmode;
				var cell = '<b>' + cpu_data[cpu].opcodes[o].mnemo + '</b><br/>';
				if (addmode != '-') {
					cell += addmode;
				}
				cell += '<br/>';
				if (cpu_data[cpu].opcodes[o].cycles) {
					cell += '<span style="float: left;">' + pretty_cycles(cpu, o);
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

function pretty_cycles(cpu, opcode) {
	var cycles = cpu_data[cpu].opcodes[opcode].cycles;
	if (cycles == 'X') {
		return '&infin;';
	} else {
		return cycles;
	}
}

function generate_mnemos_by_category(id, filter) {
	var mnemos_by_category = document.getElementById(id);
	mnemos_by_category.innerHTML = '';

	// collect data
	var data = [];
	var max_cat_size = 0;
	for (var category of all_sorted_categories) {
		var column = [ category ];
		for (mnemo of cpu_data[cpu].all_mnemos[filter]) {
			if (cpu_data[cpu].operations[mnemo].category == category) {
					column.push(mnemo);
			}
		}
		data.push(column);
		if (max_cat_size < column.length) {
			max_cat_size = column.length;
		}
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
	for (var i = 1; i < max_cat_size; i++) {
		tr = document.createElement("tr");
		mnemos_by_category.appendChild(tr);
		for (var column of data) {
			if (column.length == 1) {
				continue;
			}

			td = document.createElement("td");
			tr.appendChild(td);
			if (column[i]) {
				td.innerHTML = column[i] +  '<br/>'
				td.className = column[0];
			}
		}
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

	for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
		th = document.createElement("th");
		tr.appendChild(th);
		if (cpu_data[cpu].addmodes[addmode]) {
			th.innerHTML = cpu_data[cpu].addmodes[addmode].description;
//			th.innerHTML = cpu_data[cpu].addmodes[addmode].syntax;
		}
//		th.className = 'vertical';
	}
	for (var mnemo of cpu_data[cpu].all_mnemos[filter]) {
		tr = document.createElement("tr");
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = mnemo;
		var row_is_empty = true;
		for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
			td = document.createElement("td");
			tr.appendChild(td);
			var opcodes = opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter);
			if (opcodes.length) {
				var opcode = opcodes[0];
				if (which == 'opcode') {
					td.innerHTML = hex16(opcode);
				} else {
					td.innerHTML = pretty_cycles(cpu, opcode);

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

	for (var title of ['Mnemonic', 'Operation']) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = title;
	}
	for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
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
	for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
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

	for (var mnemo of cpu_data[cpu].all_mnemos[filter]) {
		var h2, table, tr, td, th, p;

		tr = document.createElement("tr");

		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = mnemo;
		td.className = cpu_data[cpu].operations[mnemo].category;

		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = cpu_data[cpu].operations[mnemo].description;

		for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
			var td1 = document.createElement("td");
			var td2 = document.createElement("td");
			var td3 = document.createElement("td");
			tr.appendChild(td1);
			tr.appendChild(td2);
			tr.appendChild(td3);
			var opcodes = opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter);
			for (var opcode of opcodes) {
				var cycles = pretty_cycles(cpu, opcode);
				td1.innerHTML += hex16(opcode) + '<br/>';
				td2.innerHTML += cpu_data[cpu].addmodes[addmode].bytes + '<br/>';
				td3.innerHTML += cycles + '<br/>';
			}
		}
		big_table.appendChild(tr);
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

function generate_reference(id, filter) {
	var reference = document.getElementById(id);
	reference.innerHTML = '';

	for (var mnemo of cpu_data[cpu].all_mnemos[filter]) {
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
		for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
			var opcodes = opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter);
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
					td.innerHTML = pretty_cycles(cpu, opcode);
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
// * combine (zp) & (zp),z into one addmode
// * check stz vs stz
// * combine 65ce02 and 65c816 ($nn,s),y into same addmode
// * add instruction description text
// * switch between illop synonym sets
// * CPU summary text
// * CPU tree
// * diff function
// * evaluate cycle formula
