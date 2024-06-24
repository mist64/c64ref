window.onload = init;

function init() {
	var tbl = document.getElementById("disassembly_table");
	for (var i = 0; i < 6; i++) {
		var key = "com.pagetable.c64disasm.column_" + i;
		var element_name = "checkbox_" + i;
		var checked = localStorage.getItem(key) != "hidden";
		document.getElementById(element_name).checked = checked;
		hideCol(i, checked);
	}
}

function hideCol(col, checked) {
	var tbl = document.getElementById("disassembly_table");
	for (var i = 0; i < tbl.rows.length; i++) {
		tbl.rows[i].cells[col+1].style.display = checked ? "" : "none";
	}
	var key = "com.pagetable.c64disasm.column_" + col;
	if (checked) {
		localStorage.removeItem(key);
	} else {
		localStorage.setItem(key, "hidden");
	}
}
