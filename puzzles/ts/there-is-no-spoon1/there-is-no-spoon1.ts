const EMPTY_CELL = '.';
const width: number = parseInt(readline()); // the number of cells on the X axis
const height: number = parseInt(readline()); // the number of cells on the Y axis
let grid: string[] = [];
for (let i: number = 0; i < height; i++) {
  const row: string = readline(); // width characters, each either 0 or .
  grid.push(row);
}

for (let y: number = 0; y < height; y++) {
  for (let x: number = 0; x < width; x++) {
    let output: string = "";
    if (grid[y][x] == EMPTY_CELL) {
      continue;
    }
    // current node
    output += `${x} ${y} `;

    // right neighbor
    let x2: number = -1;
    let y2: number = -1;
    for (let i: number = x + 1; i < width; i++) {
      if (grid[y][i] != EMPTY_CELL) {
        x2 = i;
        y2 = y;
        break
      }
    }
    output += `${x2} ${y2} `;

    // bottom neighbor
    let x3: number = -1;
    let y3: number = -1;
    for (let j: number = y + 1; j < height; j++) {
      if (grid[j][x] != EMPTY_CELL) {
        x3 = x;
        y3 = j;
        break
      }
    }
    output += `${x3} ${y3}`;

    // Three coordinates: a node, its right neighbor, its bottom neighbor
    console.log(output);
  }
}
