let nbHorses: number = Number(readline()); // number of horses
let strengths: number[] = []; // the strengths of each horse
let minDiff = Infinity;
for (let i: number = 0; i < nbHorses; ++i) {
  strengths.push(Number(readline()));
}

// Sort the array to easily find the minimum difference
strengths.sort((strength1, strength2) => (strength1 - strength2));

for (let i: number = 0; i < (nbHorses - 1); ++i) {
  let difference: number = strengths[i + 1] - strengths[i];
  minDiff = Math.min(minDiff, difference);
}

console.log((minDiff));
