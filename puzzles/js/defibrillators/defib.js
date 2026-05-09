function toRadians(degrees) {
    return degrees * Math.PI / 180;
}

// Parse the user's longitude and latitude
const LON = parseFloat(readline().replace(',', '.'));
const LAT = parseFloat(readline().replace(',', '.'));

// Number of defibrillators
const N = parseInt(readline());

let closestDefibName = '';
let closestDistance = Infinity;

// Loop over each defibrillator to calculate the distance
for (let i = 0; i < N; i++) {
    const DEFIB = readline().split(';');
    const defibLon = parseFloat(DEFIB[4].replace(',', '.'));
    const defibLat = parseFloat(DEFIB[5].replace(',', '.'));

    // Calculate the distance using the provided formula
    const x = (defibLon - LON) * Math.cos(toRadians((LAT + defibLat) / 2));
    const y = defibLat - LAT;
    const distance = Math.hypot(x, y) * 6371;  // Earth's radius in kilometers

    // Check if this defibrillator is closer than the current closest
    if (distance < closestDistance) {
        closestDistance = distance;
        closestDefibName = DEFIB[1];
    }
}

// Output the name of the closest defibrillator
console.log(closestDefibName);
