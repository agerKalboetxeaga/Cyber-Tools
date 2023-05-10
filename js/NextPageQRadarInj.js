window.onload = function(){
	var rarrow = 39;
	var larrow = 37;
	var uArrow = 38;
	var dArrow = 40;
	
	
	index = 2;
	window.onkeydown=function(gfg){
		if(gfg.keyCode == uArrow){
			eventNext;
			eventNext.click();
			eventNext.mousedown();
			eventNext.mouseup();
		}else if(gfg.keyCode == dArrow){
			eventPrevious;
			eventPervious.click();
			eventPrevious.mousedown();
			eventPervious.mouseup();
		}else if(gfg.keyCode == rarrow){
			var eventNext = document.getElementById("GUID_30");
			var pageForward = document.querySelectorAll("a[href='javascript:jumpToPage("+index+")']");
			index++;
			eventNext.click();
			eventNext.mousedown();
			eventNext.mouseup();
		}else if(gfg.keyCode == larrow){
			index--;
			var eventPervious = document.getElementById("GUID_29");
			var pageForward = document.querySelectorAll("a[href='javascript:jumpToPage("+index+")']");
			eventPrevious;
			eventPervious.click();
			eventPrevious.mousedown();
			eventPervious.mouseup();
		}
	}
}

