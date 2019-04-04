package main

import (
  "fmt"
  "strings"
  "strconv"
)

func main() {
  var original int
  fmt.Scan(&original)
  var lineNumber int
  fmt.Scan(&lineNumber)
  var conway_sequence = []string{strconv.Itoa(original)}
  
  for line := 1; line < lineNumber; line++ {
    var temp_sequence []string
    var count = 0
    var previous = conway_sequence[0]
    for _, number := range conway_sequence {
      if number == previous {
        count++
      } else {
        temp_sequence = append(temp_sequence, strconv.Itoa(count), previous)
        previous = number
        count = 1
      }
    }

    temp_sequence = append(temp_sequence, strconv.Itoa(count), previous)
    conway_sequence = temp_sequence
  }

  fmt.Println(strings.Join(conway_sequence, " "))
}
