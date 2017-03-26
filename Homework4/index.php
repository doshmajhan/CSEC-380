<!DOCTYPE html>
<html>
<head>
	<title>Hey there</title>
	<script src="main.js"></script>
	<!--<script src="add_friend.js"></script>-->
</head>
<body>
	<h1>Wassup</h1>
	<div id="stat"></div>
	<div id="plugs"></div>
	<br />
</body>
</html>
<?php
	if(isset($_SERVER['HTTP_REFERER'])){
		echo "Referer: " . $_SERVER['HTTP_REFERER'];
		echo "<br>";
	}
	if(isset($_SERVER['HTTP_USER_AGENT'])){
		echo "User-Agent: " . $_SERVER['HTTP_USER_AGENT'];
		echo "<br>";
	}
	echo "IP: " . $_SERVER['REMOTE_ADDR'];
?>
