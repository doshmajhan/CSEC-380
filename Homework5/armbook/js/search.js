$( document ).ready(function() {
	var id = document.getElementById("id").className;
	$('.fancybox').fancybox();
	
	$('#search').keypress(function (e) {
	  if (e.which == 13) {
		$('#search_form').submit();
		return false;
	  }
	});		
	$.get( "timeline.php?id=" + id, function( data ) {
	  $( "#botcont" ).html( data );
	});		

	$( "#friends" ).click(function() {
		$.get( "friends.php?id=" + id, function( data ) {
		  $( "#botcont" ).html( data );
		  event.preventDefault();
		});
	});
	$( "#add_friend" ).click(function() {
		$.get( "add_friend.php?id=" + id, function( data ) {
		  event.preventDefault();
		});
		location.reload();
	});
	$( "#del_friend" ).click(function() {
		$.get( "del_friend.php?id=" + id, function( data ) {	
		  event.preventDefault();
		});
		location.reload();
	});		
});
