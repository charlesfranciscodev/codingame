const surfaceN: number = parseInt(readline()); // the number of points used to draw the surface of Mars.
for (let i = 0; i < surfaceN; i++) {
  readline().split(' ');
}

// game loop
while (true) {
  const inputs: string[] = readline().split(' ');
  const vSpeed: number = parseInt(inputs[3]); // the vertical speed (in m/s), can be negative.
  let power: number = parseInt(inputs[6]); // the thrust power (0 to 4).

  let rotationAngle = 0;
  if (vSpeed <= -40) {
    power = 4;
  } else {
    power = 0;
  }

  // 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
  console.log(`${rotationAngle} ${power}`);
}
