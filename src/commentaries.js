/*
// Add this to the using HTML with the relevant config changes:
<script>
const pageConfiguration = {
	storage_prefix: "com.pagetable.c64mem.",
	number_of_entries: 8,
	number_of_header_columns: 3,
	has_decimal_column: true,
	decimal_column: 2
};
</script>
<script src="script.js"></script>
};
*/

// Global variable to store the configuration
let config;

window.onload = function() {
	config = pageConfiguration;
	//console.log(config);
	init()
};

function init() {
	var tbl = document.getElementById("disassembly_table");
	for (var i = 0; i < config.number_of_entries; i++) {
		var key = config.storage_prefix + "column_" + i;
		var element_name = "checkbox_" + i;
		var checked = localStorage.getItem(key) != "hidden";
		document.getElementById(element_name).checked = checked;
		hideCol(i, checked);
	}

	if (config.has_decimal_column) {
		var key = config.storage_prefix + "column_decimal";
		var element_name = "checkbox_decimal";
		var visible = localStorage.getItem(key) == "visible";
		document.getElementById(element_name).checked = visible;
		toggleDecimal(visible);
	}
}

function toggleDecimal(visible) {
	var tbl = document.getElementById("disassembly_table");
	for (var i = 0; i < tbl.rows.length; i++) {
		tbl.rows[i].cells[config.decimal_column].style.display = visible ? "" : "none";
	}
	var key = config.storage_prefix + "column_decimal";
	//var cnt = document.getElementById("disassembly_container");
	if (visible) {
		localStorage.setItem(key, "visible");
	} else {
		localStorage.removeItem(key);
	}
}

function hideCol(col, checked) {
	var tbl = document.getElementById("disassembly_table");
	for (var i = 0; i < tbl.rows.length; i++) {
		tbl.rows[i].cells[col + config.number_of_header_columns].style.display = checked ? "" : "none";
	}
	var key = config.storage_prefix + "column_" + col;
	if (checked) {
		localStorage.removeItem(key);
	} else {
		localStorage.setItem(key, "hidden");
	}
}

function openAll() {
	var elems = document.getElementsByTagName("details");
	document.getElementById("toggle_details_button").innerHTML = "Hide All Details";
	document.getElementById("toggle_details_button").setAttribute("onClick", "javascript: closeAll();");

	for (let item of elems) {
		item.setAttribute("open", true);
	}
}

function closeAll() {
	var elems = document.getElementsByTagName("details");
	document.getElementById("toggle_details_button").setAttribute("onClick", "javascript: openAll();");
	document.getElementById("toggle_details_button").innerHTML = "Expand All Details";

	for (let item of elems) {
		item.removeAttribute("open");
	}
}
