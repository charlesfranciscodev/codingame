package main

import "fmt"

func main() {
  var elevators = make(map[int]int)

  var n1, width, n2, exitFloor, exitPos, n3, n4, nbElevators int
  fmt.Scan(&n1, &width, &n2, &exitFloor, &exitPos, &n3, &n4, &nbElevators)
  
  for i := 0; i < nbElevators; i++ {
    var elevatorFloor, elevatorPos int
    fmt.Scan(&elevatorFloor, &elevatorPos)
    elevators[elevatorFloor] = elevatorPos
  }
  // For the last floor, we use the exit instead of an elevator.
  elevators[exitFloor] = exitPos

  // game loop
  for {
    var cloneFloor, clonePos int
    var direction string
    fmt.Scan(&cloneFloor, &clonePos, &direction)
    if cloneFloor == -1 {
      fmt.Println("WAIT")
    } else if direction == "LEFT" && clonePos < elevators[cloneFloor] {
      fmt.Println("BLOCK")
    } else if direction == "RIGHT" && clonePos > elevators[cloneFloor] {
      fmt.Println("BLOCK")
    } else {
      fmt.Println("WAIT")
    }
  }
}
