<?php
	$file = fopen("/tmp/info.txt", "a+");
	if(isset($_POST['data'])){
		fwrite($file, $_POST['data'] . "\n");
	}
	fclose($file);
?>
