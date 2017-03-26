window.onload = function(){
	var num = navigator.plugins.length;
	var txt = "Installed plugins:<br/>";
	for(var i=0; i<num; i++){
		txt += navigator.plugins[i].name + "<br />";
	}
	document.getElementById("plugs").innerHTML = txt;
};
