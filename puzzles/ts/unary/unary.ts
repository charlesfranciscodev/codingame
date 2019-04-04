function toBinary(message: string): string {
  let binary = "";
  for (let character of message) {
    binary += character.charCodeAt(0).toString(2).padStart(7, '0');
  }
  return binary;
}

function toUnary(binary: string): string {
  let allSeries: string[] = [];
  let groups : RegExpMatchArray = binary.match(/(.)\1*/g);
  for (let group of groups) {
    let firstBlock = group[0] === '1' ? "0" : "00";
    let secondBlock = '0'.repeat(group.length);
    let series = firstBlock + ' ' + secondBlock;
    allSeries.push(series);
  }
  return allSeries.join(' ');
}

const message = readline();

let binary = toBinary(message);
let unary = toUnary(binary);
console.log(unary);
