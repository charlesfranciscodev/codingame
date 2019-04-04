const n: number = Number(readline()); // the number of temperatures to analyse
const inputs: string[] = readline().split(' ');

let temperatureClosestToZero: number = 5526;
for (let i = 0; i < n; i++) {
  const temperature: number = Number(inputs[i]);
  const absoluteValue = Math.abs(temperature);
  const closestAbsoluteValue = Math.abs(temperatureClosestToZero);
  if (absoluteValue < closestAbsoluteValue) {
    temperatureClosestToZero = temperature
  } else if (absoluteValue == closestAbsoluteValue && temperature > temperatureClosestToZero) {
    temperatureClosestToZero = temperature;
  }
}

if (n === 0) {
  console.log(0);
} else {
  console.log(temperatureClosestToZero);
}
