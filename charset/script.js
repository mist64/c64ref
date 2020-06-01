function test(element) {
	console.log(element);
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

function showHide(items1, items2) {
	var i;
	for (i = 0; i < items1.length; i++) {
		var currentItem = items1[i];
		currentItem.style.display = null;
	}
	var i;
	for (i = 0; i < items2.length; i++) {
		var currentItem = items2[i];
		currentItem.style.display = "none";
	}
}

function unicodeSwitch(index) {
	if (index == 0) {
		showHide(document.getElementsByClassName("unicode_upper"), document.getElementsByClassName("unicode_lower"));
	} else if (index == 1) {
		showHide(document.getElementsByClassName("unicode_lower"), document.getElementsByClassName("unicode_upper"));
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

function highlight_key(machine, scancode, petscii, is_modifier) {
	items = document.getElementsByClassName('keyrect')
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.fill = 'white';
	}
	items = document.getElementsByClassName('keyrect_' + machine + '_' + scancode)
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.fill = 'gray';
	}
	items = document.getElementsByClassName('keytext')
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.fill = 'black';
	}
	items = document.getElementsByClassName('keytext_' + machine + '_' + scancode)
	for (i = 0; i < items.length; i++) {
		var currentItem = items[i];
		currentItem.style.fill = 'white';
	}
	if (!is_modifier) {
		test(petscii);
	}
}
