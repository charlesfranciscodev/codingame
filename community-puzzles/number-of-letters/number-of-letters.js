function numberOfLetters(number) {
  const binary = number.toString(2);
  let count = 0;
  for (let i = 0; i < binary.length; i++) {
    let c = binary.charAt(i);
    if (c == '0') {
      count += 4;
    } else {
      count += 3;
    }
  }
  return count;
}

const inputs = readline().split(' ');
let number = Number(inputs[0]);
const iterations = Number(inputs[1]);

for (let i = 0; i < iterations; i++) {
  let prevNumber = number;
  number = numberOfLetters(number);
  if (prevNumber == number) {
    break;
  }
}

print(number);

