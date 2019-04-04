'use strict'

let nbHorses = parseInt(readline()); // number of horses
let strengths = []; // the strengths of each horse
let minDiff = Number.MAX_SAFE_INTEGER;
for (let i = 0; i < nbHorses; ++i)
  strengths.push(parseInt(readline()));

// Sort the array to easily find the minimum difference
strengths.sort((strength1, strength2) => (strength1 - strength2));

for (let i = 0; i < (nbHorses - 1); ++i) {
  let difference = strengths[i + 1] - strengths[i];
  minDiff = Math.min(minDiff, difference);
}

print(minDiff);
