let elevators = [];

let inputs = readline().split(' ');
let nbFloors = parseInt(inputs[0]); // number of floors
let width = parseInt(inputs[1]); // width of the area
let nbRounds = parseInt(inputs[2]); // maximum number of rounds
let exitFloor = parseInt(inputs[3]); // floor on which the exit is found
let exitPos = parseInt(inputs[4]); // position of the exit on its floor
let nbTotalClones = parseInt(inputs[5]); // number of generated clones
let nbAdditionalElevators = parseInt(inputs[6]); // ignore (always zero)
let nbElevators = parseInt(inputs[7]); // number of elevators
for (let i = 0; i < nbElevators; i++) {
  let inputs = readline().split(' ');
  let elevatorFloor = parseInt(inputs[0]); // floor on which this elevator is found
  let elevatorPos = parseInt(inputs[1]); // position of the elevator on its floor
  elevators[elevatorFloor] = elevatorPos;
}
// For the last floor, we use the exit instead of an elevator.
elevators[exitFloor] = exitPos;

// game loop
while (true) {
    let inputs = readline().split(' ');
    let cloneFloor = parseInt(inputs[0]); // floor of the leading clone
    let clonePos = parseInt(inputs[1]); // position of the leading clone on its floor
    let direction = inputs[2]; // direction of the leading clone: LEFT or RIGHT

    if (cloneFloor === -1) {
      print('WAIT');
    } else if (direction === "LEFT" && clonePos < elevators[cloneFloor]) {
      print('BLOCK');
    } else if (direction === "RIGHT" && clonePos > elevators[cloneFloor]) {
      print('BLOCK');
    } else {
      print('WAIT');
    }
}
