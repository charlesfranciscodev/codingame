package main

import "fmt"

func main() {
  var lightX, lightY, thorX, thorY int
  fmt.Scan(&lightX, &lightY, &thorX, &thorY)

  // game loop
  for {
    var direction string

    if thorY > lightY  {
      direction += "N"
      thorY--
    } else if thorY < lightY {
      direction += "S"
      thorY++
    }

    if thorX > lightX  {
      direction += "W"
      thorX--
    } else if thorX < lightX {
      direction += "E"
      thorX++
    }

    // A single line providing the move to be made: N NE E SE S SW W or NW
    fmt.Println(direction)
  }
}
