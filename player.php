<?php
$dbhost = getenv("MYSQL_SERVICE_HOST");
$dbport = getenv("MYSQL_SERVICE_PORT");
$dbuser = getenv("DATABASE_USER");
$dbname = getenv("DATABASE_NAME");
$dbpwd = getenv("DATABASE_PASSWORD");

echo 'host ' . $dbhost
echo 'db ' . $dbname
//echo 'host ' . $dbhost

$connection = mysqli_connect($dbhost.":".$dbport, $dbuser, $dbpwd, $dbname) or die("Error " . mysqli_error($connection));

$query = "SELECT * from soccer" or die("Error in the consult.." . mysqli_error($connection));

echo "List of footballers: <br>";

$rs = $connection->query($query);
while ($row = mysqli_fetch_assoc($rs)) {
    echo "Player: ".$row['name'] . "Club: " . $row['club'] . "<br>";
}
echo "End of the list <br>";
mysqli_close($connection);
?>
