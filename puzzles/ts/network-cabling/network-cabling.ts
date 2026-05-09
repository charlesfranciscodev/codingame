const nb_buildings: number = parseInt(readline());

const y_coordinates: number[] = [];
let min_x: number = Math.pow(2, 30);
let max_x: number = -Math.pow(2, 30);

for (let i = 0; i < nb_buildings; i++) {
  const [x, y] = readline().split(' ').map(Number);
  y_coordinates.push(y);
  if (x < min_x) {
    min_x = x;
  }
  if (x > max_x) {
    max_x = x;
  }
}

// length of horizontal cable
let cable_length: number = max_x - min_x;

// calculate y median to minimize the length of vertical cable(s)
y_coordinates.sort((y1, y2) => y1 - y2);
let y_median: number = y_coordinates[Math.floor(nb_buildings / 2)];

// length of vertical cable(s)
for (const y of y_coordinates) {
  cable_length += Math.abs(y_median - y);
}

console.log(cable_length);
