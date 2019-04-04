let inputs: string[] = readline().split(' ');
const width: number = Number(inputs[0]); // width of the building.
const height: number = Number(inputs[1]); // height of the building.
const n: number = Number(readline()); // maximum number of turns before game over.
inputs = readline().split(' ');
let x: number = Number(inputs[0]);
let y: number = Number(inputs[1]);

let minBombX = 0;
let maxBombX = width - 1;
let minBombY = 0;
let maxBombY = height - 1;

// game loop
while (true) {
  const direction = readline(); // the direction of the bombs from batman"s current location (U, UR, R, DR, D, DL, L or UL)

  switch (direction) {
    case "U":
      minBombX = maxBombX = x;
      maxBombY = y - 1;
      break;
    case "R":
      minBombY = maxBombY = y;
      minBombX = x + 1;
      break;
    case "D":
      minBombX = maxBombX = x;
      minBombY = y + 1;
      break;
    case "L":
      minBombY = maxBombY = y;
      maxBombX = x - 1;
      break;
    case "UR":
      minBombX = x + 1;
      maxBombY = y - 1;
      break;
    case "UL":
      maxBombX = x - 1;
      maxBombY = y - 1;
      break;
    case "DR":
      minBombX = x + 1;
      minBombY = y + 1;
      break;
    case "DL":
      maxBombX = x - 1;
      minBombY = y + 1;
      break;
  }

  x = Math.floor((minBombX + maxBombX) / 2);
  y = Math.floor((minBombY + maxBombY) / 2);

  // the location of the next window Batman should jump to.
  console.log(`${x} ${y}`);
}
