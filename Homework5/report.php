<?php
	include_once "armbook/common.php";

	$logfile = "/tmp/violations.log";
	
	$json_data = file_get_contents('php://input');
	if($json_data = json_decode($json_data, true)){
		foreach($json_data as $json){
			$stmt = $mysqli->prepare("INSERT INTO violations VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
			$stmt->bind_param("sssssssssss", $json['document-uri'], $json['referrer'], $json['violdated-directive'], $json['effective-directive'], $json['original-policy'], $json['disposition'], $json['blocked-uri'], $json['line-number'], $json['column-number'], $json['source-file'], $json['status-code']);
			$stmt->execute();
			$stmt->close();
			$json_data = json_encode($json_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
			file_put_contents($logfile, $json_data, FILE_WRITE | LOCK_EX);
		}
	}
?>
