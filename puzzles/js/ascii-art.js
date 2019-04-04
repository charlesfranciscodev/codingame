'use strict';

const ALPHABET_SIZE = 27;
const width = parseInt(readline());
const height = parseInt(readline());
const text = readline().toUpperCase();
const totalWidth = width * ALPHABET_SIZE;
let asciiArt = [];

// Fill the ASCII ART array
for (let i = 0; i < height; ++i)
  asciiArt.push(readline());

// Print the letter for each height level
asciiArt.forEach((row) => {
  let output = "";
  for (let i = 0; i < text.length; ++i) {
    let asciiCode = text[i].charCodeAt(0);
    let position = asciiCode - 'A'.charCodeAt(0);
    if (position < 0 || position > 25)
      position = 26;
    let column = position * width;
    for (let i = column; i < (column + width); ++i)
      output += row[i];
  } // for
  print(output);
}); // forEach()
