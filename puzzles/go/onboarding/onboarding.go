package main

import "fmt"

func main() {
  // game loop
  for {
    var enemy1 string  // name of enemy 1
    fmt.Scan(&enemy1)
    var dist1 int // distance to enemy 1
    fmt.Scan(&dist1)
    var enemy2 string // name of enemy 2
    fmt.Scan(&enemy2)
    var dist2 int // distance to enemy 2
    fmt.Scan(&dist2)
    
    // Display enemy1's name when enemy1 is the closest, enemy2's name otherwise
    if dist1 < dist2 {
        fmt.Println(enemy1)
    } else {
        fmt.Println(enemy2)
    }
  }
}
