// game loop
while (true) {
  let indexHighestMountain: number = 0;
  let highestHeight: number = -1;
  for (let i: number = 0; i < 8; i++) {
    const height = parseInt(readline()); // represents the height of one mountain.
    if (height > highestHeight) {
      highestHeight = height;
      indexHighestMountain = i;
    }
  }
  console.log(indexHighestMountain); // The index of the mountain to fire on.
}
