'use strict';

let inputs = readline().split(' ');
let lightX = parseInt(inputs[0]); // the X position of the light of power
let lightY = parseInt(inputs[1]); // the Y position of the light of power
let thorX = parseInt(inputs[2]); // Thor's starting X position
let thorY = parseInt(inputs[3]); // Thor's starting Y position

// game loop
while (true) {
  readline(); // The remaining amount of turns Thor can move. Do not remove this line.
  let direction = '';

  if (thorY > lightY) {
    direction += 'N';
    --thorY;
  } else if (thorY < lightY) {
    direction += 'S';
    ++thorY;
  }

  if (thorX > lightX) {
    direction += 'W';
    --thorX;
  } else if (thorX < lightX) {
    direction += 'E';
    ++thorX;
  }
  
  // A single line providing the move to be made: N NE E SE S SW W or NW
  print(direction);
}
