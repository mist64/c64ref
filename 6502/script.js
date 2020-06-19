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
	'-',
	'A',
	'#d8',
	'#d16',
	'a16',
	'a16,X',
	'a16,Y',
	'(a16)',
	'(a16,X)',
	'a8',
	'a8,X',
	'a8,Y',
	'(a8)',
	'(a8,X)',
	'(a8),Y',
	'(a8),Z',
	'[a8]',
	'[a16]',
	'a24',
	'a24,X',
	'r8',
	'r16',
	'a8,r8',
	'a8,S',
	'(a8,S),Y',
	'(a8,SP),Y',
	'src,dest',
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

const category_descriptions = {
	'load':      'Load/Store',
	'trans':     'Transfer',
	'stack':     'Stack',
	'shift':     'Shift',
	'logic':     'Logic',
	'arith':     'Arithmetic',
	'inc':       'Arithmetic: Inc/Dec',
	'ctrl':      'Control Flow',
	'bra':       'Control Flow: Branch',
	'flags':     'Flags',
	'kil':       'KIL',
	'nop':       'NOP',
	'undefined': 'Undefined',
};

const all_cycle_symbols = 'mxwpt';

const cycle_symbol_descriptions = {
	'*': '*Undocumented.',
	'm': 'm: =1 if memory and accumulator are 8 bit.',
	'x': 'x: =1 if index registers are 8 bit.',
	'w': 'w: =1 if DL register ≠ 0.',
	'p': 'p: =1 if page is crossed.',
	't': 't: =1 if branch is taken.',
};

const default_tabno = 1;
const numtabs = 5;

var cpu_data = {};
var files_loaded = 0;
var file_data = {};
var showillegal;
var separateillegal;

var cpu;
var tabno;

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
						decode_generic(cpu, 'info');
						decode_registers(cpu);
						decode_generic(cpu, 'vectors');
						decode_flags(cpu);
						decode_opcodes(cpu);
						decode_operations(cpu);
						decode_mnemos(cpu);
						decode_addmodes(cpu);
						decode_timing(cpu);
						decode_documentation_mnemos(cpu);
						decode_documentation_addmodes(cpu);
						fixup_data(cpu);
					}
					populate_cpu_list();
					handle_args();
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
	var text;
	if (!file_data[cpu][section]) {
		text = [];
	} else {
		text = file_data[cpu][section].text;
	}
	if (!text) {
		text = [];
	}
	if (cpu_data[cpu].info && cpu_data[cpu].info.basedon && !(file_data[cpu].noinherit && file_data[cpu].noinherit.includes(section))) {
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
		line = line.split('##')[0]; // remove comments
		var starts_with_space = line[0] == ' ';
		line = line.trim();
		if (!line) {
			continue;
		} else if (line[0] == '[' && line[line.length - 1] == ']') {
			section = line.substr(1, line.length - 2);
			section = section.split('|');
			if (section.length > 1) {
				switch (section[1]) { // options
					case 'noinherit':
						if (data_out.noinherit == undefined) {
							data_out.noinherit = [];
						}
						data_out.noinherit.push(section[0]);
						break;
				}
			}
			section = section[0];
			data_out[section] = {};
		} else {
			line = line.split(/\s+/);
			if (section) {
				if (!data_out[section].text) {
					data_out[section].text = [];
				}
				if (starts_with_space) {
					line = [''].concat(line);
				}
				data_out[section].text.push(line);
			}
		}
	}
	file_data[cpu] = data_out;
}

function decode_generic(cpu, section) {
	var text = get_file_data(cpu, section);
	cpu_data[cpu][section] = {};
	for (var line of text) {
		cpu_data[cpu][section][line[0]] = line.slice(1).join(' ');
	}
}

function decode_registers(cpu) {
	var text = get_file_data(cpu, 'registers');

	cpu_data[cpu].registers = {};

	for (var line of text) {
		var name = line[0];
		if (name == '#') {
			cpu_data[cpu].registers.registers = line[1].split(',');
		} else {
			cpu_data[cpu].registers[name] = {};
			cpu_data[cpu].registers[name].size = line[1];
			cpu_data[cpu].registers[name].description = line.slice(2).join(' ');
		}
	}
}

function decode_flags(cpu) {
	var text = get_file_data(cpu, 'flags');
	var name = {};
	var description = {};
	for (var line of text) {
		var id = line[0];
		name[id] = line[1];
		description[id] = line.slice(2).join(' ');
	}
	function sort_id(a, b) {
		if (a < 10) {
			a += 20;
		}
		if (b < 10) {
			b += 20;
		}
		return b - a;
	}
	ids = Object.keys(name).sort(sort_id);
	var names = '';
	for (id of ids) {
		names += name[id];
	}

	cpu_data[cpu].flags = {};
	cpu_data[cpu].flags.names = names;
	for (id of ids) {
		cpu_data[cpu].flags[name[id]] = description[id];
	}
}

function decode_opcodes(cpu) {
	var text = get_file_data(cpu, 'opcodes');
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
	var text = get_file_data(cpu, 'operations');
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
	var text = get_file_data(cpu, 'mnemos');
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
	var text = get_file_data(cpu, 'addmodes');
	cpu_data[cpu].addmodes = {};
	for (var line of text) {
		var addmode = line[0];
		cpu_data[cpu].addmodes[addmode] = {};
		cpu_data[cpu].addmodes[addmode].bytes = line[1];
		cpu_data[cpu].addmodes[addmode].syntax = line[2] != '-' ? line[2] : '';
		cpu_data[cpu].addmodes[addmode].description = line.slice(3).join(' ');
	}
}

function evaluate_single(single, state, encountered_symbols) {
	if (state[single] != undefined) {
		encountered_symbols.push(single);
		return state[single];
	} else {
		return parseInt(single);
	}
}

function evaluate_component(component, state, encountered_symbols) {
	var index = component.indexOf('*');
	if (index < 0) {
		return evaluate_single(component, state, encountered_symbols);
	} else {
		var l = evaluate_single(component.slice(0, index), state, encountered_symbols);
		var r = evaluate_single(component.slice(index + 1), state, encountered_symbols);
		return l * r;
	}
}

function evaluate_cycles(cycles) {
	var min = 999;
	var max = 0;

	const symbols = all_cycle_symbols;
	for (var i = 0; i < 1 << symbols.length; i++) {
		var state = {};
		for (var j = 0; j < symbols.length; j++) {
			state[symbols[j]] = (i >> j) & 1;
		}

		var encountered_symbols = [];
		var c = cycles.slice();
		var operator = '+';
		var value = 0;
		while (true) {
			var index = c.search(/[+-]/);

			if (index < 0) {
				var component = c;
			} else {
				var component = c.slice(0, index);
			}

			var value2 = evaluate_component(component, state, encountered_symbols);
			if (operator == '+') {
				value += value2;
			} else {
				value -= value2;
			}

			if (index < 0) {
				break;
			}

			operator = c[index];
			c = c.slice(index+1);
		}
		min = Math.min(min, value);
		max = Math.max(max, value);
	}
	return { min: min, max: max, symbols: encountered_symbols };
}

function decode_timing(cpu) {
	var text = get_file_data(cpu, 'timing');
	for (var line of text) {
		var o = parseInt(line[0], 16);
		cpu_data[cpu].opcodes[o].cycles = line[1];

		var evaluated = evaluate_cycles(line[1])

		cpu_data[cpu].opcodes[o].mincycles = evaluated.min;
		cpu_data[cpu].opcodes[o].maxcycles = evaluated.max;
		cpu_data[cpu].opcodes[o].cyclesymbols = evaluated.symbols;
	}
}

function decode_documentation_mnemos(cpu) {
	var text = get_file_data(cpu, 'documentation-mnemos');
	var mnemo;
	for (var line of text) {
		if (line[0] != '') {
			mnemo = line[0];
			cpu_data[cpu].operations[mnemo].documentation = {};
			cpu_data[cpu].operations[mnemo].documentation.title = line.slice(1).join(' ');
		} else {
			if (cpu_data[cpu].operations[mnemo].documentation.text == undefined) {
				cpu_data[cpu].operations[mnemo].documentation.text = [];
			}
			cpu_data[cpu].operations[mnemo].documentation.text.push(line.slice(1).join(' '));
		}
	}
}

function decode_documentation_addmodes(cpu) {
	var text = get_file_data(cpu, 'documentation-addmodes');
	var mnemo;
	for (var line of text) {
		if (line[0] != '') {
			addmode = line[0];
			cpu_data[cpu].addmodes[addmode].documentation = {};
			cpu_data[cpu].addmodes[addmode].documentation.title = line.slice(1).join(' ');
		} else {
			if (cpu_data[cpu].addmodes[addmode].documentation.text == undefined) {
				cpu_data[cpu].addmodes[addmode].documentation.text = [];
			}
			cpu_data[cpu].addmodes[addmode].documentation.text.push(line.slice(1).join(' '));
		}
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

function populate_cpu_list() {
	var select = document.getElementById('cpu');
	for (cpu of cpus) {
		var option = document.createElement("option");
		option.value = cpu_data[cpu].info.id;
		option.innerHTML = cpu_name(cpu);
		if (cpu_data[cpu].info.revision) {
			option.innerHTML += ' (' + cpu_data[cpu].info.revision + ')';
		}
		select.appendChild(option);
	}
}

function handle_args() {
	const queryString = window.location.search;
	const urlParams = new URLSearchParams(queryString);
	if (urlParams.has('cpu')) {
		document.getElementById('cpu').value = urlParams.get('cpu');
	}
	if (urlParams.has('tab')) {
		tabno = urlParams.get('tab');
	} else {
		tabno = default_tabno;
	}
	document.getElementById('tab' + tabno).checked = true;
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
	for (tabno = 0; tabno < numtabs; tabno++) {
		if (document.getElementById('tab' + tabno).checked) {
			break;
		}
	}
	if (tabno == numtabs) {
		tabno = default_tabno;
	}

	cpu = document.getElementById('cpu').value;
	showillegal = document.getElementById('showillegal').checked;
	separateillegal = document.getElementById('separateillegal').checked;
	var has_illegal = cpu_has_illegal(cpu);

	// create URL
	var url = window.location.href;
	url = url.split('?')[0];
	url = url.split('#')[0];
	args = [];
	if (cpu != cpus[0]) {
		args.push('cpu=' + cpu);
	}
	if (tabno != default_tabno) {
		args.push('tab=' + tabno);
	}
	if (args.length) {
		args = '?' + args.join('&');
	} else {
		args = '';
	}
	history.pushState({}, null, url + args);

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

	for (var id of [
		'info_div',
		'flags_div',
		'registers_div',
		'vectors_div',
		'opcode_div1',
		'opcode_div2',
		'addmode_div',
		'legend1',
		'legend2',
		'big_table_div1',
		'big_table_div2',
		'mnemos_by_category',
		'reference1',
		'reference2',
	]) {
		document.getElementById(id).innerHTML = '';
	}

	for (var i = 0; i < numtabs; i++) {
		if (i == tabno) {
			document.getElementById('tab'+i+'c').style.display = '';
		} else {
			document.getElementById('tab'+i+'c').style.display = 'none';
		}
	}

	console.log(tabno);
	switch (tabno) {
		case 0:
			generate_info('info_div');
			generate_flags_div('flags_div');
			generate_registers_div('registers_div');
			generate_vectors_div('vectors_div');
			break;
		case 1:
			generate_opcode_table('opcode_div1', filter1);
			generate_opcode_table('opcode_div2', filter2);
			generate_legend('legend1');
			break;
		case 2:
			generate_mnemos_by_category('mnemos_by_category', filter1);
			generate_reference('reference1', filter1);
			generate_reference('reference2', filter2);
			break;
		case 3:
			generate_addmode_table('addmode_div');
			break;
		case 4:
			generate_big_table('big_table_div1', filter1);
			generate_big_table('big_table_div2', filter2);
			generate_legend('legend2');
			break;
	}
}

function o_from_x_y(x, y, opcode_table_organization) {
	if (opcode_table_organization == '4-4') {
		return y << 4 | x;
	} else if (opcode_table_organization == '3-3-2/h') {
		var a = y & 7;
		var b = x & 7;
		var c = x >> 3;
		return a << 5 | b << 2 | c;
	} else if (opcode_table_organization == '3-3-2/v') {
		var a = y & 7;
		var b = x & 7;
		var c = y >> 3;
		return a << 5 | b << 2 | c;
	}
}

function cpu_name(cpu) {
	s = '';
	if (cpu_data[cpu].info.manufacturer) {
		s = cpu_data[cpu].info.manufacturer + ' ';
	}
	return s + cpu_data[cpu].info.name;
}

function generate_info(id) {
	var div = document.getElementById(id);

	if (cpu_data[cpu].info.manufacturer) {
		var img = document.createElement("img");
		div.appendChild(img);
		img.src = cpu_data[cpu].info.manufacturer.toLowerCase() + '.svg';
		img.className = 'info_logo';
	}

	var h3 = document.createElement("h3");
	div.appendChild(h3);

	h3.innerHTML = cpu_name(cpu);
	if (cpu_data[cpu].info.revision) {
		h3.innerHTML += ' (' + cpu_data[cpu].info.revision + ')';
	}
	if (cpu_data[cpu].info.year) {
		h3.innerHTML += ' [' + cpu_data[cpu].info.year + ']';
	}

	var p = document.createElement("p");
	div.appendChild(p);
	p.innerHTML = cpu_data[cpu].info.description;
}

function generate_opcode_table(id, filter) {
	opcode_table_organization = document.getElementById('opcode_table_organization').value;

	var opcode_div = document.getElementById(id);
	opcode_div.innerHTML = '';

	var table = document.createElement("table");
	opcode_div.appendChild(table);
	table.className = 'opcode_table';

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
	table.appendChild(tr);
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
		table.appendChild(tr);
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
		}
	}
}

function generate_addmode_table(id) {
	var div = document.getElementById(id);
	div.innerHTML = '';

	if (false) {
		var table = document.createElement("table");
		div.appendChild(table);

		tr = document.createElement("tr");
		table.appendChild(tr);
		for (var h of ['Short', 'Syntax', 'Description']) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.innerHTML = h;
		}

		for (var addmode of cpu_data[cpu].all_addmodes['all']) {
			var tr = document.createElement("tr");
			table.appendChild(tr);

			var td = document.createElement("td");
			tr.appendChild(td);
			td.innerHTML = addmode;

			var td = document.createElement("td");
			tr.appendChild(td);
			td.innerHTML = cpu_data[cpu].addmodes[addmode].syntax;

			var td = document.createElement("td");
			tr.appendChild(td);
			td.innerHTML = cpu_data[cpu].addmodes[addmode].description;

		}
	} else {
		for (var addmode of cpu_data[cpu].all_addmodes['all']) {
			var div2 = document.createElement("div");
			div2.classList.add('reference_card_addmode');
			div.appendChild(div2);

			var h2 = document.createElement("h2");
			div2.appendChild(h2);

			if (cpu_data[cpu].addmodes[addmode].documentation) {
				h2.innerHTML = cpu_data[cpu].addmodes[addmode].documentation.title;
			} else {
				h2.innerHTML = cpu_data[cpu].addmodes[addmode].description;
			}

			var span = document.createElement("span");
			h2.appendChild(span);
			span.innerHTML = cpu_data[cpu].addmodes[addmode].syntax;
			span.style.float = 'right';

			if (cpu_data[cpu].addmodes[addmode].documentation) {
				var p = document.createElement("p");
				div2.appendChild(p);
				p.innerHTML = cpu_data[cpu].addmodes[addmode].documentation.text
			} else {

			}
		}
	}
}

function hex16(a) {
	return ('0' + a.toString(16).toUpperCase()).slice(-2);
}

function pretty_cycles(cpu, opcode) {
	if (cpu_data[cpu].opcodes[opcode].cycles == 'X') {
		return '&infin;';
	} else {
		var min = cpu_data[cpu].opcodes[opcode].mincycles;
		var max = cpu_data[cpu].opcodes[opcode].maxcycles;
		if (min == max) {
			return min;
		} else {
			return min + '-' + max;
		}
	}
}

function generate_mnemos_by_category(id, filter) {
	var div = document.getElementById(id);
	div.innerHTML = '';

	table = document.createElement("table");
	div.appendChild(table);

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
	table.appendChild(tr);
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
		table.appendChild(tr);
		for (var column of data) {
			if (column.length == 1) {
				continue;
			}

			td = document.createElement("td");
			tr.appendChild(td);
			if (column[i]) {
				td.className = column[0];
				a = document.createElement("a");
				a.href='#mnemo_' + column[i];
				a.innerHTML = column[i] +  '<br/>'
				td.appendChild(a);
			}
		}
	}
}

function generate_registers_div(id) {
	var div = document.getElementById(id);
	div.innerHTML = '';

	var table = document.createElement("table");
	div.appendChild(table);

	tr = document.createElement("tr");
	table.appendChild(tr);
	for (var h of ['Name', 'Size', 'Description']) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = h;
	}

	for (var register of cpu_data[cpu].registers.registers) {
		tr = document.createElement("tr");
		table.appendChild(tr);
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = register;
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = cpu_data[cpu].registers[register].size;
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = cpu_data[cpu].registers[register].description;
	}
}

function generate_flags_div(id) {
	var div = document.getElementById(id);
	div.innerHTML = '';

	var table = document.createElement("table");
	div.appendChild(table);

	tr = document.createElement("tr");
	table.appendChild(tr);
	for (var i = 0; i < cpu_data[cpu].flags.names.length; i++) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.innerHTML = cpu_data[cpu].flags.names[i];
	}

	var table = document.createElement("table");
	div.appendChild(table);

	for (var i = 0; i < cpu_data[cpu].flags.names.length; i++) {
		var bitno = i >= 8 ? '-' : 7 - i;
		var name = cpu_data[cpu].flags.names[i];
		var description = cpu_data[cpu].flags[name];
		tr = document.createElement("tr");
		table.appendChild(tr);
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = bitno;
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = name;
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = description;
	}
}

function generate_vectors_div(id) {
	var div = document.getElementById(id);
	div.innerHTML = '';

	var table = document.createElement("table");
	div.appendChild(table);

	for (var address of Object.keys(cpu_data[cpu].vectors).sort()) {
		tr = document.createElement("tr");
		table.appendChild(tr);
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = '$' + address;
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = cpu_data[cpu].vectors[address];
	}

}

function all_mnemos_sorted(cpu, filter, sortbycat) {
	if (filter == 'none') {
		return [];
	}
	var all_mnemos = cpu_data[cpu].all_mnemos[filter].slice();
	if (sortbycat) {
		function sort_by_cat(a, b) {
			var cat_a = cpu_data[cpu].operations[a].category;
			var cat_b = cpu_data[cpu].operations[b].category;
			if (cat_a == cat_b) {
				return a.localeCompare(b);
			} else {
				return all_sorted_categories.findIndex(x => x == cat_a) - all_sorted_categories.findIndex(x => x == cat_b);
			}
		}
		all_mnemos = all_mnemos.sort(sort_by_cat);
	}
	return all_mnemos;
}


function generate_big_table(id, filter) {
	var div = document.getElementById(id);
	div.innerHTML = '';

	var table = document.createElement("table");
	table.className = 'big_table';
	div.appendChild(table);

	if (filter == 'none') {
		return;
	}

	showoperation = document.getElementById('showoperation').checked;
	showopcodes = document.getElementById('showopcodes').checked;
	showbytes = document.getElementById('showbytes').checked;
	showcycles = document.getElementById('showcycles').checked;
	cycledetails = document.getElementById('cycledetails').checked;
	sortbycat = document.getElementById('sortbycat1').checked;

	tr = document.createElement("tr");
	table.appendChild(tr);

	th = document.createElement("th");
	tr.appendChild(th);
	th.classList.add('rotate');
	var div2 = document.createElement("div");
	th.appendChild(div2);
	var span = document.createElement("span");
	div2.appendChild(span);
	span.innerHTML = 'Mnemonic';

	if (showoperation) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.classList.add('rotate');
		var div2 = document.createElement("div");
		th.appendChild(div2);
		var span = document.createElement("span");
		div2.appendChild(span);
		span.innerHTML = 'Operation';
	}

	if (showcycles || showopcodes || showbytes) {
		for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.colSpan = (showopcodes ? 1 : 0) + (showbytes ? 1 : 0) + (showcycles ? 1 : 0) ;
			th.classList.add('rotate');
			var div2 = document.createElement("div");
			th.appendChild(div2);
			var span = document.createElement("span");
			div2.appendChild(span);
			span.innerHTML = cpu_data[cpu].addmodes[addmode].description;
			///span.innerHTML = cpu_data[cpu].addmodes[addmode].syntax;
		}
	}
	th = document.createElement("th");
	tr.appendChild(th);
	th.colSpan = cpu_data[cpu].flags.names.length;
	th.classList.add('rotate');
	var div2 = document.createElement("div");
	th.appendChild(div2);
	var span = document.createElement("span");
	div2.appendChild(span);
	span.innerHTML = 'Flags';

	tr = document.createElement("tr");
	table.appendChild(tr);
	th = document.createElement("th");
	th.classList.add('leading');
	tr.appendChild(th);
	if (showoperation) {
		th = document.createElement("th");
		th.classList.add('leading');
		tr.appendChild(th);
	}
	for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
		if (showopcodes) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.classList.add('opcode');
			th.innerHTML = 'OP';
			th.classList.add('leading');
		}
		if (showbytes) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.classList.add('bytes');
			th.innerHTML = 'N';
			if (!showopcodes) {
				th.classList.add('leading');
			}
		}
		if (showcycles) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.classList.add('cycles');
			th.innerHTML = '#';
			if (!showopcodes && !showbytes) {
				th.classList.add('leading');
			}
		}
	}
	for (var i = 0; i < cpu_data[cpu].flags.names.length; i++) {
		th = document.createElement("th");
		tr.appendChild(th);
		th.classList.add('flag');
		if (i == 0) {
			th.classList.add('leading');
		}
		th.innerHTML = cpu_data[cpu].flags.names[i];
	}

	var all_mnemos = all_mnemos_sorted(cpu, filter, sortbycat);

	for (var mnemo of all_mnemos) {
		var h2, table, tr, td, th, p;

		tr = document.createElement("tr");

		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = mnemo;
		td.className = cpu_data[cpu].operations[mnemo].category;
		td.classList.add('leading');

		if (showoperation) {
			td = document.createElement("td");
			td.classList.add('operation');
			td.classList.add('leading');
			td.innerHTML = cpu_data[cpu].operations[mnemo].description;
			tr.appendChild(td);
		}

		for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
			var td1 = document.createElement("td");
			var td2 = document.createElement("td");
			var td3 = document.createElement("td");
			
			td1.classList.add('opcode');
			td1.classList.add('leading');

			td2.classList.add('bytes');
			if (!showopcodes) {
				td2.classList.add('leading');
			}
			td3.classList.add('cycles');
			if (!showopcodes && !showbytes) {
				td3.classList.add('leading');
			}
			if (cycledetails) {
				td3.classList.add('detailed');
			}
			
			var opcodes = opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter);
			for (var opcode of opcodes) {
				if (cycledetails) {
					var cycles = cpu_data[cpu].opcodes[opcode].cycles;
				} else {
					var cycles = pretty_cycles(cpu, opcode);
				}
				td1.innerHTML += hex16(opcode) + '<br/>';
				td2.innerHTML += cpu_data[cpu].addmodes[addmode].bytes + '<br/>';
				td3.innerHTML += cycles + '<br/>';
			}
			if (showopcodes) {
				tr.appendChild(td1);
			}
			if (showbytes) {
				tr.appendChild(td2);
			}
			if (showcycles) {
				tr.appendChild(td3);
			}
		}
		table.appendChild(tr);
		for (var i = 0; i < cpu_data[cpu].flags.names.length; i++) {
			td = document.createElement("td");
			td.classList.add('flag');
			if (i == 0) {
				td.classList.add('leading');
			}
			tr.appendChild(td);
			var flag = cpu_data[cpu].operations[mnemo].flags[i];
			switch (flag) {
				case '-':
				case undefined:
					td.innerHTML = '-';
					break;
				case '0':
				case '1':
					td.innerHTML = flag;
					break;
				default:
					td.innerHTML = cpu_data[cpu].flags.names[i];
					break;
			}
		}
	}
	if (cycledetails) {
		p = document.createElement("p");
		div.appendChild(p);
		p.innerHTML = description_for_cycle_symbols(all_cycle_symbols);
	}
}

function description_for_cycle_symbols(symbols) {
	html = '';
	for (s of symbols) {
		html += cycle_symbol_descriptions[s];
		html += '<br/>'
	}
	return html;
}

function generate_reference(id, filter) {
	sortbycat = document.getElementById('sortbycat2').checked;

	var reference = document.getElementById(id);
	reference.innerHTML = '';

	var all_mnemos = all_mnemos_sorted(cpu, filter, sortbycat);

	for (var mnemo of all_mnemos) {
		var div = document.createElement("div");
		div.id='mnemo_' + mnemo;
		div.classList.add('reference_card');
		div.classList.add(cpu_data[cpu].operations[mnemo].category + '_light');
		if (cpu_data[cpu].all_mnemos['illegal'].includes(mnemo)) {
			div.classList.add('ill_big');
		}
		var num_rows = 0;

		// flags
		table = document.createElement("table");
		table.className = 'reference_flags_table';
		div.appendChild(table);
		tr = document.createElement("tr");
		table.appendChild(tr);
		for (var title of cpu_data[cpu].flags.names) {
			th = document.createElement("th");
			tr.appendChild(th);
			th.innerHTML = title;
		}
		tr = document.createElement("tr");
		table.appendChild(tr);
		for (var i = 0; i < cpu_data[cpu].flags.names.length; i++) {
			td = document.createElement("td");
			tr.appendChild(td);
			var flag = cpu_data[cpu].operations[mnemo].flags[i];
			switch (flag) {
				case '-':
				case undefined:
					td.innerHTML = '-';
					break;
				case '0':
				case '1':
					td.innerHTML = flag;
					break;
				default:
					td.innerHTML = '&#10003;';
					break;
			}
		}

		// heading
		var h2, table, tr, td, th, p;
		h2 = document.createElement("h2");
		div.appendChild(h2);
		var title = mnemo;

		if (cpu_data[cpu].operations[mnemo].documentation && cpu_data[cpu].operations[mnemo].documentation.title) {
			title += ' - ' + cpu_data[cpu].operations[mnemo].documentation.title;
		} else if (cpu_data[cpu].mnemos[mnemo]) {
			title += ' - ' + cpu_data[cpu].mnemos[mnemo].description;
		}
		h2.innerHTML =  title;

		// description
		p = document.createElement("p");
		div.appendChild(p);
		p.innerHTML = '<b>Operation</b>: ' + cpu_data[cpu].operations[mnemo].description + '<br/>';

		if (cpu_data[cpu].operations[mnemo].documentation) {
			for (var line of cpu_data[cpu].operations[mnemo].documentation.text) {
				p = document.createElement("p");
				div.appendChild(p);
				p.innerHTML = line;
			}
		}

		// addressing mode table
		table = document.createElement("table");
		table.className = 'reference_table';
		div.appendChild(table);
		tr = document.createElement("tr");
		table.appendChild(tr);
		for (var title of ['Addressing Mode', 'Assembly Language Form', 'Opcode', 'No. Bytes', 'No. Cycles']) {
			th = document.createElement("th");
			th.innerHTML = title;
			th.className = cpu_data[cpu].operations[mnemo].category;
			tr.appendChild(th);
		}
		var footnotes = new Set();
		for (var addmode of cpu_data[cpu].all_addmodes[filter]) {
			var opcodes = opcodes_for_mnemo_and_addmode(cpu, mnemo, addmode, filter);
			for (var opcode of opcodes) {
				var illegal = cpu_data[cpu].opcodes[opcode].illegal;
				if (showillegal || !illegal) {
					num_rows++;

					tr = document.createElement("tr");
					if (num_rows % 2) {
						tr.className = cpu_data[cpu].operations[mnemo].category + '_light';
					} else {
						tr.style.backgroundColor = 'white';
					}
					table.appendChild(tr);
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = cpu_data[cpu].addmodes[addmode].description;
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = mnemo + ' ' + cpu_data[cpu].addmodes[addmode].syntax;
					td.style.fontFamily = 'monospace';
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = '$' + hex16(opcode);
					if (illegal) {
						td.innerHTML += '*';
						footnotes.add('*');
					}
					td.style.textAlign = 'center';
					td = document.createElement("td");
					tr.appendChild(td);
					td.innerHTML = cpu_data[cpu].addmodes[addmode].bytes;
					td.style.textAlign = 'center';
					td = document.createElement("td");
					tr.appendChild(td);
					var cycles = cpu_data[cpu].opcodes[opcode].cycles;
					td.innerHTML = cpu_data[cpu].opcodes[opcode].cycles;
					td.style.textAlign = 'center';

					cpu_data[cpu].opcodes[opcode].cyclesymbols.forEach(footnotes.add, footnotes)

				}
			}
		}
		var p = document.createElement("p");
		div.appendChild(p);
		p.innerHTML = description_for_cycle_symbols(footnotes);

		// if there were no opcodes, don't add the div
		// this happens if
		// * all opcodes were illegal and illegals were disabled
		// * the mnemo was inherited, and the current CPU doesn't have it
		if (num_rows) {
			reference.appendChild(div);
		}
	}
}

function generate_legend(id) {
	var div = document.getElementById(id);
	div.innerHTML = '';

	table = document.createElement("table");
	table.style = 'font-size: 9pt;';
	div.appendChild(table);

	for (cat of all_sorted_categories) {
		tr = document.createElement("tr");
		table.appendChild(tr);
		td = document.createElement("td");
		tr.appendChild(td);
		td.className = cat;
		td.style.width = '15px';
		td = document.createElement("td");
		tr.appendChild(td);
		td.innerHTML = category_descriptions[cat];
	}
}


// TODO:

// Data
// * documentation: add pseudocode
// * per-CPU documentation comments
// * verify undocumented with groepaz doc
// * better addmode short forms for opcode matrix
// * 65C02 decimal mode: ADC/SBC +1 cycle

// Visualization
// * CPU tree

// Features
// * diff function

// Design Features
// * detailed cycles disabled if cycles is unchecked
// * opcodes table should not be squished
