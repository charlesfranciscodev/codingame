package main

import (
  "fmt"
  "sort"
)

func main() {
  var n int
  fmt.Scan(&n)
  var horses []int
  var min = 10000000
  
  for i := 0; i < n; i++ {
    var horse int
    fmt.Scan(&horse)
    horses = append(horses, horse)
  }
  
  sort.Ints(horses)

  for i := 0; i < n - 1; i++ {
    var diff = horses[i + 1] - horses[i]
    if (diff < min) {
      min = diff
    }
  }
  
  fmt.Println(min)
}
