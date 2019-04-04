'use strict';

const EARTH_RADIUS = 6371;
const NAME = 1;
const LONGITUDE = 4;
const LATITUDE = 5;

// Convert degrees to radians
function toRadians(distance) {
  let degrees = distance.replace(",", ".");
  return degrees * Math.PI / 180;
}

let min = Number.MAX_SAFE_INTEGER;
let name = "";

let longitude = toRadians(readline());
let latitude = toRadians(readline());
let defibCount = parseInt(readline());

// Determine the name of the defibrillator located the closest to the user’s position.
for (let i = 0; i < defibCount; ++i) {
  let defib = readline();
  let defibArray = defib.split(";");
  let defibLon = toRadians(defibArray[LONGITUDE]);
  let defibLat = toRadians(defibArray[LATITUDE]);
  let x = (defibLon - longitude) * Math.cos((latitude + defibLat) / 2);
  let y = defibLat - latitude;
  let distance = Math.hypot(x, y) * EARTH_RADIUS;
  if (distance < min) {
    min = distance;
    name = defibArray[NAME];
  }
}

print(name);
