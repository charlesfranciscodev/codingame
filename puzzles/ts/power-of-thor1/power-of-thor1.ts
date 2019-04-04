const inputs: string[] = readline().split(' ');
const lightX: number  = Number(inputs[0]); // the X position of the light of power
const lightY: number = Number(inputs[1]); // the Y position of the light of power
let thorX: number = Number(inputs[2]); // Thor's starting X position
let thorY: number = Number(inputs[3]); // Thor's starting Y position

// game loop
while (true) {
  let move: string = "";
  if (thorY < lightY) {
    move += 'S';
    thorY += 1;
  } else if (thorY > lightY) {
    move += 'N';
    thorY -= 1;
  }
  if (thorX < lightX) {
    move += 'E';
    thorX += 1;
  } else if (thorX > lightX) {
    move += 'W';
    thorX -= 1;
  }
  // A single line providing the move to be made: N NE E SE S SW W or NW
  console.log(move);
}
