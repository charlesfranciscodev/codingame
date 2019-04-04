<?php
fscanf(STDIN, "%d %d", $width, $height);
fscanf(STDIN, "%d", $nbTurns);
fscanf(STDIN, "%d %d", $x, $y);

// Indicates the search area coordinates
$minX = 0; // minimum x value
$maxX = $width - 1; // maximum x value
$minY = 0; // minimum y value
$maxY = $height - 1; // maximum y value

// game loop
while (true) {
  fscanf(STDIN, "%s", $bombDir);

  if ($bombDir == "U") { // UP
    $maxY = $y - 1;
    $y = ($minY + $maxY) / 2;
  } else if ($bombDir == "UR") { // UP-RIGHT
    $minX = $x + 1;
    $maxY = $y - 1;
    $x = ($minX + $maxX) / 2;
    $y = ($minY + $maxY) / 2;
  } else if ($bombDir == "R") { // RIGHT
    $minX = $x + 1;
    $x = ($minX + $maxX) / 2;
  } else if ($bombDir == "DR") { // DOWN-RIGHT
    $minX = $x + 1;
    $minY = $y + 1;
    $x = ($minX + $maxX) / 2;
    $y = ($minY + $maxY) / 2;
  } else if ($bombDir == "D") { // DOWN
    $minY = $y + 1;
    $y = ($minY + $maxY) / 2;
  } else if ($bombDir == "DL") { // DOWN-LEFT
    $maxX = $x - 1;
    $minY = $y + 1;
    $x = ($minX + $maxX) / 2;
    $y = ($minY + $maxY) / 2;
  } else if ($bombDir == "L") { // LEFT
    $maxX = $x - 1;
    $x = ($minX + $maxX) / 2;
  } else { // UL or UP-LEFT
    $maxX = $x - 1;
    $maxY = $y - 1;
    $x = ($minX + $maxX) / 2;
    $y = ($minY + $maxY) / 2;
  } // else

  $x = (int) $x;
  $y = (int) $y;

  // the location of the next window Batman should jump to.
  echo($x ." " . $y . "\n");
}
?>