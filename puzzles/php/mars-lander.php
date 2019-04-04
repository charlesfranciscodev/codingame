<?php
fscanf(STDIN, "%d",
  $surfaceN // the number of points used to draw the surface of Mars.
);
for ($i = 0; $i < $surfaceN; $i++) {
  fscanf(STDIN, "%d %d",
    $landX, // X coordinate of a surface point. (0 to 6999)
    $landY // Y coordinate of a surface point.
  );
}

// game loop
while (TRUE) {
  fscanf(STDIN, "%d %d %d %d %d %d %d",
    $X,
    $Y,
    $hSpeed, // the horizontal speed (in m/s), can be negative.
    $vSpeed, // the vertical speed (in m/s), can be negative.
    $fuel, // the quantity of remaining fuel in liters.
    $rotate, // the rotation angle in degrees (-90 to 90).
    $power // the thrust power (0 to 4).
  );

  // 2 integers: rotate power.
  echo("0 ");
  if ($vSpeed <= -40) {
    echo min(4, $power + 1);
  } else {
    echo max(0, $power - 1);
  }
  echo "\n";
}
?>
