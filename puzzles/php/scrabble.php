<?php
function getScore($letter) {
  $arr = array(
    'e' => 1, 'a' => 1, 'i' => 1, 'o' => 1, 'n' => 1, 'r' => 1, 't' => 1, 'l' => 1, 's' => 1,'u' => 1,
    'd' => 2, 'g' => 2,
    'b' => 3, 'c' => 3, 'm' => 3, 'p' => 3,
    'f' => 4, 'h' => 4, 'v' => 4, 'w' => 4, 'y' => 4,
    'k' => 5,
    'j' => 8, 'x' => 8,
    'q' => 10, 'z' => 10
  );

  return $arr[$letter];
}

$bestWord = "";
$highScore = 0;
$dictionary = [];

fscanf(STDIN, "%d", $nbWords);
for ($i = 0; $i < $nbWords; ++$i) {
  $dictionary[] = stream_get_line(STDIN, 31, "\n");
}
$letters = stream_get_line(STDIN, 9, "\n");

for ($i = 0; $i < $nbWords; ++$i) {
  $letters2 = $letters;
  $word = $dictionary[$i];
  $isValid = true;
  $currentScore = 0;

  // calculate the total score for one word
  for ($j = 0; $j < strlen($word); ++$j) {
    $character = $word[$j];
    $pos = strpos($letters2, $character);
    if ($pos !== false) {
      $letters2 = substr_replace($letters2, "", $pos, strlen($character)); // remove the letter  
      $currentScore += getScore($character);
    } else {
      $isValid = false; // unavailable letter
      break;
    }
  }

  if ($isValid && ($currentScore > $highScore)) {
    $highScore = $currentScore;
    $bestWord = $word;
  }
}

echo("$bestWord\n");
?>
