const N = parseInt(readline(), 10);
const strengths = [];

for (let i = 0; i < N; i++) {
  const pi = parseInt(readline(), 10);
  strengths.push(pi);
}

strengths.sort((a, b) => a - b);

let minDiff = Infinity;

for (let i = 1; i < N; i++) {
  const diff = strengths[i] - strengths[i - 1];
  if (diff < minDiff) {
    minDiff = diff;
  }
}

console.log(minDiff);
