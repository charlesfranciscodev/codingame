function points(letter: string) {
  if ("dg".indexOf(letter) !== -1) {
    return 2;
  } else if ("bcmp".indexOf(letter) !== -1) {
    return 3;
  } else if ("fhvwy".indexOf(letter) !== -1) {
    return 4;
  } else if ("k".indexOf(letter) !== -1) {
    return 5;
  } else if ("jx".indexOf(letter) !== -1) {
    return 8;
  } else if ("qz".indexOf(letter) !== -1) {
    return 10;
  } else {
    return 1;
  }
}

function isValidWord(word: string, lettersArray: string[]): boolean {
  for (let c of word) {
    let index: number = lettersArray.indexOf(c);
    if (index === -1) {
      return false;
    } else {
      lettersArray.splice(index, 1);
    }
  }
  return true;
}

function score(word: string) {
  let total: number = 0;
  for (let c of word) {
    total += points(c);
  }
  return total;
}

// read standard input
const nbWords: number = Number(readline());
const words: string[] = [];
for (let i: number = 0; i < nbWords; i++) {
  const word: string = readline();
  words.push(word);
}
const letters: string = readline();

// compute solution
let bestScore: number = 0;
let bestWord: string = "";
for (let i: number = 0; i < nbWords; i++) {
  const word: string = words[i];
  const lettersArray: string[] = letters.split('');
  if (isValidWord(word, lettersArray)) {
    let currentScore: number = score(word);
    if (currentScore > bestScore) {
      bestScore = currentScore;
      bestWord = word;
    }
  }
}

console.log(bestWord);
