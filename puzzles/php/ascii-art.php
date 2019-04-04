<?php
define("ALPHABET_SIZE", 27);
fscanf(STDIN, "%d", $width);
fscanf(STDIN, "%d", $height);
$text = strtoupper(stream_get_line(STDIN, 257, "\n"));
$totalWidth = $width * ALPHABET_SIZE;
$asciiArt = array();
for ($i = 0; $i < $height; ++$i)
  array_push($asciiArt, stream_get_line(STDIN, 1025, "\n"));

// Print each letter for each row in the ASCII Art alphabet
foreach($asciiArt as $row) {
  $output = "";
  for ($i = 0; $i < strlen($text); ++$i) {
    $position = ord($text[$i]) - ord("A");
    if ($position < 0 || $position > 25)
      $position = 26;
    $output .= substr($row, $position * $width, $width);
  }
  echo "$output\n";
}
?>
