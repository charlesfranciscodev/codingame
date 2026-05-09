const width: number = Number(readline());
const height: number = Number(readline());
const text: string = readline().toUpperCase();

for (let i: number = 0; i < height; i++) {
  const row: string = readline();
  let output: string = "";
  for (let letter of text) {
    let alphabetPosition = letter.charCodeAt(0) - 'A'.charCodeAt(0);
    if (alphabetPosition < 0 || alphabetPosition > 25) {
      alphabetPosition = 26;
    }
    let column = alphabetPosition * width;
    output += row.substring(column, column + width);
  }
  console.log(output);
}
