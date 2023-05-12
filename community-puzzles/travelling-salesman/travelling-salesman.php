<?php

function distance($point1, $point2) {
    $dx = $point2[0] - $point1[0];
    $dy = $point2[1] - $point1[1];
    return hypot($dx, $dy);
}

$unvisited = array();
$total_dist = 0;
$current_index = 0;
$points = array();

fscanf(STDIN, "%d", $n);
for ($i = 0; $i < $n; $i++) {
    fscanf(STDIN, "%d %d", $X, $Y);
    $point = array($X, $Y);
    $points[] = $point;
    $unvisited[] = $i;
}

while (count($unvisited) != 0) {
    $min_index = 0;
    $min_dist = INF;
    $current_point = $points[$current_index];
    foreach ($unvisited as $i) {
        if ($i != 0) {
            $dist = distance($current_point, $points[$i]);
            if ($dist < $min_dist) {
                $min_dist = $dist;
                $min_index = $i;
            }
        }
    }
    if ($min_index == 0) {
        $min_dist = distance($current_point, $points[0]);
    }
    $total_dist += $min_dist;
    $key = array_search($min_index, $unvisited);
    unset($unvisited[$key]);
    $current_index = $min_index;
}

echo round($total_dist);

?>
