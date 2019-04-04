<?php
$grid = [];

fscanf(STDIN, "%d",$width);
fscanf(STDIN, "%d", $height);
for ($y = 0; $y < $height; $y++) {
  $line = stream_get_line(STDIN, 31 + 1, "\n");
  $grid[$y] = $line;
}

for ($y = 0; $y < $height; $y++) {
  for ($x = 0; $x < $width; $x++) {
    if ($grid[$y][$x] == "0") {
      $output = $x . " " . $y . " ";

      // right neighbor
      $neighbor = ".";
      $neighborX = $x + 1;
      while ($neighbor == "." && $neighborX < $width) {
        $neighbor = $grid[$y][$neighborX];
        if ($neighbor == "0") {
          $output .= $neighborX . " " . $y . " ";
        }
        $neighborX++;
      }

      if ($neighbor == ".") {
        $output .= "-1 -1 ";
      }

      // bottom neighbor
      $neighbor = ".";
      $neighborY = $y + 1;
      while ($neighbor == "." && $neighborY < $height) {
        $neighbor = $grid[$neighborY][$x];
        if ($neighbor == "0") {
          $output .= $x . " " . $neighborY . " ";
        }
        $neighborY++;
      }

      if ($neighbor == ".") {
        $output .= "-1 -1 ";
      }

      echo($output . "\n");
    }
  }
}
?>