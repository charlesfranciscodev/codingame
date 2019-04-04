package main

import (
  "fmt"
  "os"
  "bufio"
  "strings"
)

func main() {
  var scores = map[rune]int {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1,
    'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10}
  var bestWord = ""
  var highScore = 0
  var words []string

  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  var nbWords int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &nbWords)
    
  for i := 0; i < nbWords; i++ {
    scanner.Scan()
    word := scanner.Text()
    words = append(words, word)
  }
  scanner.Scan()
  letters := scanner.Text()

  for _, word := range words {
    var letters2 = string(letters)
    var isValid = true
    var currentScore = 0

    // calculate the total score for one word
    for _, character := range word {
      var index = strings.IndexRune(letters2, character)
      if index == -1 {
        isValid = false
      } else {
        letters2 = letters2[:index] + letters2[index+1:]
        currentScore += scores[character]
      }
    }

    if isValid && currentScore > highScore {
      highScore = currentScore
      bestWord = word
    }
  }

  fmt.Println(bestWord)
}
