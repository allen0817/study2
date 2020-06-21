<?php
set_time_limit(0);

/*
$f= fopen("./3.txt","r");
$i = 1;
while (!feof($f))
{
  echo '正在刷序号：'.$i,"\t";
  $i++;
  $line = fgets($f);
  echo $line,PHP_EOL;
  trap($line);
}
fclose($f);

*/


trap('192.168.33.80',$h);


function trap($ip){
	$user = 'admin';
	$pass = 'ITCloud123!';
	$connection=ssh2_connect($ip,22);
	ssh2_auth_password($connection,$user,$pass);
	$shell = ssh2_shell($connection);


	$cmd="system-view";
	fwrite( $shell, $cmd.PHP_EOL);
	sleep(1);

	$cmd="snmp-agent target-host trap address udp-domain  10.142.88.5 vpn-instance MGMT params securityname ITCloud123 v2c";
	fwrite( $shell, $cmd.PHP_EOL);
	sleep(1);

	$cmd="quit";
	fwrite( $shell, $cmd.PHP_EOL);
	sleep(1);
	$cmd="quit";
	fwrite( $shell, $cmd.PHP_EOL);
	sleep(1);

	echo "\n=============完成==================\n";
}



$conn = ssh2_connect($ip,22);
ssh2_auth_password($conn,$user,$pass);
$shell = ssh2_shell($conn);


fwrite( $shell, $cmd.PHP_EOL);

$result = stream_get_contents($shell);




