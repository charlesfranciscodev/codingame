function conwaySequence(sequence: number[], lineNumber: number): number[] {
  while (lineNumber != 1) {
    sequence = nextSequence(sequence);
    lineNumber -= 1;
  }
  return sequence;
}

function nextSequence(sequence: number[]): number[] {
  let newSequence = [];
  let string: string = sequence.map(String).join(' ') + ' ';
  let groups: RegExpMatchArray = string.match(/(\d* )\1*/g);
  for (let group of groups) {
    let array: string[] = group.split(' ');
    let count: number = array.length - 1;
    let value: number = Number(array[0]);
    newSequence.push(count);
    newSequence.push(value);
  }
  return newSequence;
}

const originalNumber: number = Number(readline());
const lineNumber = Number(readline());

let finalSequence = conwaySequence([originalNumber], lineNumber);
let output = finalSequence.map(String).join(' ');
console.log(output);

