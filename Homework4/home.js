$( document ).ready(function() {
	var id = document.getElementById("id").className;
	var token = document.getElementById("id").innerHTML;
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
		$.get( "add_friend.php?id=" + id + "&token=" + token, function( data ) {
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
	console.log("loaded");
	var id = document.getElementById("id").className;
	var f = 'jqueryui';
	//toggle `popup` / `inline` mode
	$.fn.editable.defaults.mode = 'popup';     
	//make username editable
	$('#school').editable();			
	//var stat = document.getElementById("statUpdate");
	//console.log(stat.className);

	//$('#statUpdate').keypress(function (e) {
	$(document).on('keypress', 'textarea', function(e) {
	  console.log("pressed");
	  if (e.which == 13) {
		$.get( "add_comment.php?id=" + id + "&comment="+$('#statUpdate').val(), function( data ) {
			location.reload();
		});	
		return false;
		
	  }
	});
});
