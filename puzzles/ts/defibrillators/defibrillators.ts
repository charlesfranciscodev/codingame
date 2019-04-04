// Convert degrees to radians
function convertToRadians(angle: string): number {
  let degrees: number = Number(angle.replace(',', '.'));
  return degrees * Math.PI / 180;
}

const lon: number = convertToRadians(readline());
const lat: number = convertToRadians(readline());
const n: number = parseInt(readline());

let minDistance: number = Infinity;
let defibName: string = "";
for (let i: number = 0; i < n; i++) {
  const defib: string = readline().split(';');
  const defibLon: number = convertToRadians(defib[4]);
  const defibLat: number = convertToRadians(defib[5]);
  const x: number = (defibLon - lon) * Math.cos((lat + defibLat) / 2)
  const y: number = defibLat - lat;
  const distance: number = Math.hypot(x, y) * 6371;
  if (distance < minDistance) {
    minDistance = distance;
    defibName = defib[1];
  }
}

console.log(defibName);
