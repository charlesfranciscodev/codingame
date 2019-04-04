<?php
fscanf(STDIN, "%d %d %d %d",
  $lightX, // the X position of the light of power
  $lightY, // the Y position of the light of power
  $thorX, // Thor's starting X position
  $thorY // Thor's starting Y position
);

// game loop
while (TRUE) {
  fscanf(STDIN, "%d", $remainingTurns);
  $direction = "";

  if ($thorY > $lightY) {
    $direction .= "N";
    --$thorY;
  } else if ($thorY < $lightY) {
    $direction .= "S";
    ++$thorY;
  }

  if ($thorX > $lightX) {
    $direction .= "W";
    --$thorX;
  } else if ($thorX < $lightX) {
    $direction .= "E";
    ++$thorX;
  }

  // A single line providing the move to be made: N NE E SE S SW W or NW
  echo("$direction" . "\n");
}
?>
