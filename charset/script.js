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

function toggleMachine(machine, checked) {
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
}




