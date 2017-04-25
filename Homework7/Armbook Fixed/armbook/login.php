<?php 
$email = $_POST['email'];
$password = $_POST['password'];
include_once("common.php");
if($stmt = $mysqli->prepare("SELECT password, user_id from users where email=?")){
	if($stmt->bind_param("s", $email)){
		if(!$stmt->execute()){
			die("Error - Issue executing prepared statement: " . mysqli_error($mysqli));
		}
		if($res = $stmt->get_result()){

			$row = $res->fetch_assoc();
			if($res->num_rows != 1){
				die("False - Username or password was invalid");
			}
			if($password === $row['password']){
				$active = 1;
				$timeNow = time();
				$session = sha1($username + $password + time());
				if($stmt = $mysqli->prepare("UPDATE sessions SET session_id=?, ip=?, born=?, valid=? where user_id=?")){
					if($stmt->bind_param("ssiis",$session, $_SERVER['REMOTE_ADDR'],$timeNow,$active,$row['user_id'])){
						if(!$stmt->execute()){
							die("Error - Issue executing prepared statement: " . mysqli_error($mysqli));
						}
					}else{
						die("Error - Issue binding prepared statement: " . mysqli_error($mysqli));
					}
					if($stmt->close()){
						setcookie("ARM_SESSION", $session, time()+3600);
						die("True - login successful");
					}else{
						die("Error - Failed to close prepared statement" . mysqli_error($mysqli));
					}
				}else{
						die("Error - Issue preparing statement: " . mysqli_error($mysqli));
				}
				
			}else{
				die('False - Username or password was invalid"');
			}
		}else{
			die("Error - Getting results: " . mysqli_error($mysqli));
		}
	}else{
		die("Error - Issue binding prepared statement: " . mysqli_error($mysqli));
	}
}else{
	die("Error - Issue preparing statement: " . mysqli_error($mysqli));
}
?>
