<?php
$elevators = [];

fscanf(STDIN, "%d %d %d %d %d %d %d %d",
  $nbFloors, // number of floors
  $width, // width of the area
  $nbRounds, // maximum number of rounds
  $exitFloor, // floor on which the exit is found
  $exitPos, // position of the exit on its floor
  $nbTotalClones, // number of generated clones
  $nbAdditionalElevators, // ignore (always zero)
  $nbElevators // number of elevators
);

for ($i = 0; $i < $nbElevators; $i++) {
  fscanf(STDIN, "%d %d",
    $elevatorFloor, // floor on which this elevator is found
    $elevatorPos // position of the elevator on its floor
  );
  $elevators[$elevatorFloor] = $elevatorPos;
}

$elevators[$nbFloors - 1] = $exitPos;

// game loop
while (true) {
  fscanf(STDIN, "%d %d %s",
    $cloneFloor, // floor of the leading clone
    $clonePos, // position of the leading clone on its floor
    $direction // direction of the leading clone: LEFT or RIGHT
  );

  if ($cloneFloor == -1) {
    echo("WAIT\n");
  } else if ($direction == "LEFT" && $clonePos < $elevators[$cloneFloor]) {
    echo("BLOCK\n");
  } else if ($direction == "RIGHT" && $clonePos > $elevators[$cloneFloor]) {
    echo("BLOCK\n");
  } else {
    echo("WAIT\n");
  }
}
?>