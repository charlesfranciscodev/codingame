function printNextRoom(roomType, x, y, entrance) {
  switch (roomType) {
    case 2:
    case 6:
      entrance === "LEFT" ? x++ : x--;
      break;
    case 4:
      entrance === "TOP" ? x-- : y++;
      break;
    case 5:
      entrance === "TOP" ? x++ : y++;
      break;
    case 10:
      x--;
      break;
    case 11:
      x++;
      break;
    default:
      y++;
  }
  console.log(`${x} ${y}`);
}

let rooms = [];
let inputs = readline().split(' ');
const nbColumns = Number(inputs[0]);
const nbRows = Number(inputs[1]);
for (let i = 0; i < nbRows; i++) {
  let line = readline().split(' ').map(Number);
  rooms.push(line);
}
readline();
// game loop
while (true) {
  const inputs = readline().split(' ');
  const x = Number(inputs[0]);
  const y = Number(inputs[1]);
  const entrance = inputs[2];
  printNextRoom(rooms[y][x], x, y, entrance);
}
