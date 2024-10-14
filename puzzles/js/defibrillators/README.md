# Defibrillators

## Problem Description

The city of Montpellier has equipped its streets with defibrillators, and the data corresponding to their positions is available. The task is to write a program that helps users find the nearest defibrillator to their current location.

### Inputs

1. **User Location:**
   - Line 1: User's longitude (in degrees, comma-separated).
   - Line 2: User's latitude (in degrees, comma-separated).
   - Line 3: The number `N` of defibrillators in the city.
   
2. **Defibrillators Data:**
   Each of the next `N` lines contains the following fields separated by semicolons (`;`):
   - A number identifying the defibrillator.
   - Name of the defibrillator.
   - Address.
   - Contact Phone number.
   - Longitude (degrees, comma-separated).
   - Latitude (degrees, comma-separated).

### Output

The program should display the **name** of the defibrillator that is **closest** to the user’s current position.

### Distance Formula

The distance `d` between the user and a defibrillator is calculated as:

```
x = (longitudeB - longitudeA) * cos((latitudeA + latitudeB) / 2)
y = latitudeB - latitudeA
distance = hypot(x, y) * 6371
```

### Constraints

- 0 < `N` < 10,000

### Example

#### Input
```
3,879483
43,608177
3
1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217
2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849
3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854
```

#### Output
```
Maison de la Prevention Sante
```

## Code Example

```javascript
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

```
