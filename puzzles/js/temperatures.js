'use strict';

let n = parseInt(readline()); // the number of temperatures to analyse
if (n === 0) {
  print(0);
} else {
  let temps = readline().split(' ').map(n => parseInt(n, 10)); // the n temperatures expressed as integers ranging from -273 to 5526
  let absTemps = temps.map(n => [Math.abs(n), n]);
  absTemps.sort((array1, array2) => (array1[0] - array2[0]));

  // Print the temperature closest to zero
  if (n !== 1 && absTemps[0][0] === absTemps[1][0])
    print(Math.max(absTemps[0][1], absTemps[1][1]));
  else
    print(absTemps[0][1]);
}
