<?php 
set_time_limit(0);


$str = file_get_contents('/tmp/aa1');


$f= fopen("./3.txt","r");
$i = 1;
while (!feof($f))
{
  $line = fgets($f);
  search($line,$str);
}
fclose($f);


function search($ip,$str){

	$re = "/$ip\./m";

	if(preg_match($re, $str,$arr)){
		echo "SUCCESS： $ip\n";
		printf($arr);
	}else{
		echo "FALSE:$ip\n";
	}

	echo "*************************************\n";


}