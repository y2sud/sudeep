<?php
$dbhost = getenv("MYSQL_SERVICE_HOST");
$dbport = getenv("MYSQL_SERVICE_PORT");
//$dbuser = getenv("DATABASE_USER");
$dbuser = getenv("MYSQL_USER");
$dbname = getenv("MYSQL_DATABASE");
$dbpwd = getenv("MYSQL_PASSWORD");

//echo 'host ' . $dbhost

$dbuser = 'baadal_sql';
$dbpwd = 'merasql';
$dbname = 'db01';

$connection = mysqli_connect($dbhost.":".$dbport, $dbuser, $dbpwd, $dbname) or die("Error " . mysqli_error($connection));

$query = "SELECT * from soccer" or die("Error in the consult.." . mysqli_error($connection));

echo "List of footballers: <br>";

$rs = $connection->query($query) or die("Error in rs.." . mysqli_error($connection));


while ($row = mysqli_fetch_assoc($rs)) {
    echo "Player: ".$row['player'] . " Club: " . $row['club'] . "<br>";
}
echo "End of the list <br>";

mysqli_close($connection);


?>
