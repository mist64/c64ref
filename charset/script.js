function test(element) {
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

function unicodeLower() {
	showHide(document.getElementsByClassName("unicode_lower"), document.getElementsByClassName("unicode_upper"));
}

function unicodeUpper() {
	showHide(document.getElementsByClassName("unicode_upper"), document.getElementsByClassName("unicode_lower"));
}
