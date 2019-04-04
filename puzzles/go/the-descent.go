package main

import "fmt"

func main() {
  for {
    var max = -1
    var indexMax int
    for i := 0; i < 8; i++ {
      var height int // represents the height of one mountain.
      fmt.Scan(&height)
      if height > max {
        max = height
        indexMax = i
      }
    }
    
    fmt.Println(indexMax) // The index of the mountain to fire on.
  }
}
