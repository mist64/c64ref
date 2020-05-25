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
}
