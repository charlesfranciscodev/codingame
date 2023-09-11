function readSurfacePoints(surfaceN: number): void {
  for (let i = 0; i < surfaceN; i++) {
    readline().split(' ');
  }
}

function calculateThrustPower(vSpeed: number): number {
  if (vSpeed <= -40) {
    return 4;
  } else {
    return 0;
  }
}

function gameLoop(): void {
  while (true) {
    const inputs: string[] = readline().split(' ');
    const vSpeed: number = parseInt(inputs[3]); // the vertical speed (in m/s), can be negative.

    const power: number = calculateThrustPower(vSpeed);
    const rotationAngle = 0;

    // 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    console.log(`${rotationAngle} ${power}`);
  }
}

const surfaceN: number = parseInt(readline()); // the number of points used to draw the surface of Mars.
readSurfacePoints(surfaceN);

// Start the game loop
gameLoop();
