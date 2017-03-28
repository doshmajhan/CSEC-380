$( document ).ready(function() {
		console.log("loaded");
		var id = document.getElementById("id").className;
		var f = 'jqueryui';
		//toggle `popup` / `inline` mode
		$.fn.editable.defaults.mode = 'popup';     
		//make username editable
		$('#school').editable();			
		$('#statUpdate').keypress(function (e) {
		  if (e.which == 13) {
			$.get( "add_comment.php?id=" + id + "&comment="+$('#statUpdate').val(), function( data ) {
				location.reload();
			});	
			return false;
			
		  }
		});
	});
