let elevators = new Map();

const inputs: string[] = readline().split(" ");
const exitFloor: number = Number(inputs[3]); // floor on which the exit is found
const exitPos: number = Number(inputs[4]); // position of the exit on its floor
const nbElevators: number = Number(inputs[7]);
for (let i: number = 0; i < nbElevators; i++) {
  const inputs: string[] = readline().split(" ");
  const elevatorFloor: number = Number(inputs[0]);
  const elevatorPos: number = Number(inputs[1]);
  elevators.set(elevatorFloor, elevatorPos);
}
// For the last floor, we use the exit instead of an elevator.
elevators.set(exitFloor, exitPos);

// game loop
while (true) {
  const inputs: string[] = readline().split(" ");
  const cloneFloor: number = Number(inputs[0]);
  const clonePos: number = Number(inputs[1]);
  const direction: string = inputs[2];

  // determine action to take based on current state
  if (cloneFloor === -1) {
    console.log("WAIT");
  } else if (direction === "LEFT" && clonePos < elevators.get(cloneFloor)) {
    console.log("BLOCK");
  } else if (direction === "RIGHT" && clonePos > elevators.get(cloneFloor)) {
    console.log("BLOCK");
  } else {
    console.log("WAIT");
  }
}
