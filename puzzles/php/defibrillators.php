<?php
// Convert degrees to radians
function toRadians($distance) {
  return str_replace(",", ".", $distance) * M_PI / 180;
}

$min = PHP_INT_MAX;
$name = "";
fscanf(STDIN, "%s", $longitude);
fscanf(STDIN, "%s", $latitude);
fscanf(STDIN, "%d", $defibCount);

// Determine the name of the defibrillator located the closest to the user’s position.
for ($i = 0; $i < $defibCount; ++$i) {
  $arr = explode(";", stream_get_line(STDIN, 257, "\n"));
  $defibLon = toRadians($arr[4]);
  $defibLat = toRadians($arr[5]);
  $x = ($defibLon - toRadians($longitude)) * cos((toRadians($latitude) + $defibLat) / 2);
  $y = $defibLat - toRadians($latitude);
  $distance = hypot($x, $y) * 6371;
  if ($distance < $min) {
    $min = $distance;
    $name = $arr[1];
  }
}

echo("$name\n");
?>
