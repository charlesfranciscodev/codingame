<?php
fscanf(STDIN, "%d", $N);
$strengths = [];
for ($i = 0; $i < $N; $i++) {
  fscanf(STDIN, "%d", $Pi);
  $strengths[] = $Pi;
}

sort($strengths);

$minDiff = PHP_INT_MAX;
for ($i = 0; $i < $N - 1; $i++) {
  $diff = $strengths[$i + 1] - $strengths[$i];
  $minDiff = min($minDiff, $diff);
}

echo("$minDiff\n");
?>