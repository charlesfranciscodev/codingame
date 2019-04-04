<?php
fscanf(STDIN, "%d", $n);
$t = explode(" ", stream_get_line(STDIN, 257, "\n"));
usort($t, function ($w, $x) {
  return abs($w) == abs($x) ? ($w > $x ? -1 : 1) : (abs($w) < abs($x) ? -1 : 1);
});
echo $n == 0 ? "0" : "$t[0]\n";
?>