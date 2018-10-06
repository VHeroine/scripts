<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Binary search</title>
			<style>
				body {
				font-size: 20px;
				}
			</style>
	</head>
<body>
	<form name="myform" action="<?=$_SERVER["PHP_SELF"]?>" method="post">
		<label for="key">Key:</label>
		<input type="text" name="key" required="required" /><br />
		<label for="file_name">File:</label>
		<input type="file" name="file_name" /><br />
		<input type="submit" name="myform" value="Submit" />
	</form>
<?php

if (isset($_POST['myform'])) {
	$key = $_POST['key']??false;
	$file_name = $_POST['file_name']??false;
	if ($key !== false && $file_name !== false) {
		echo binary_search($file_name, $key);
		}
}

function binary_search($file_name, $key) {
	$spl = new SplFileObject($file_name);
	$left = 0;
	$right = 0;
	foreach ($spl as $line) {$right++;}
	while ($left < $right) {
		$mid = $left + floor(($right - $left) / 2);
		$spl -> seek($mid);
		$str_mid = strpos($spl -> current(), "\t");
		$src_key = substr($spl -> current(), 0, $str_mid);
		if ($src_key >= $key) $right = $mid;
		else $left = $mid + 1;
	}
	$str_mid = strpos($spl -> current(), "\t");
	$src_key = substr($spl -> current(), 0, $str_mid);
	$str_end = strpos($spl -> current(), "\x0A");
	$value = substr($spl -> current(), $str_mid, $str_end);
	if ($src_key == $key) return $value;
	else return 'undef';
}

?>
</body>
</html>