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
	if (deselectionArray.length == 0) {
	    var radioList = document.getElementsByName("radios");
		var y;
		for (y = 0; y < radioList.length; y++) {
			var currentRadio = radioList[y];
			currentRadio.checked = false;
		}

	} else {
		var currentCheckboxId = "checkbox_".concat(machine);
		var currentCheckbox = document.getElementById(currentCheckboxId);
		currentCheckbox.checked = true;

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
}

function charsetSwitch(filename) {
	//console.log(document.styleSheets)
	items = document.getElementsByClassName('char-img')
	//console.log(items.style)
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.backgroundImage = 'url(' + filename + ')'
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
