package main

import "fmt"

func main() {
  var width, height int
  fmt.Scan(&width, &height)
  
  var n int // maximum number of turns before game over.
  fmt.Scan(&n)
  
  var x, y int
  fmt.Scan(&x, &y)
  
  var minX = 0
  var maxX = width - 1
  var minY = 0
  var maxY = height - 1

  for {
    var bombDir string
    fmt.Scan(&bombDir)
    
    switch bombDir {
    case "U":
      minX, maxX = x, x
      maxY = y - 1
    case "UR":
      minX = x + 1
      maxY = y - 1
    case "R":
      minY, maxY = y, y
      minX = x + 1
    case "DR":
      minX = x + 1
      minY = y + 1
    case "D":
      minX, maxX = x, x
      minY = y + 1
    case "DL":
      maxX = x - 1
      minY = y + 1
    case "L":
      minY, maxY = y, y
      maxX = x - 1
    case "UL":
      maxX = x - 1
      maxY = y - 1
    }

    x = (minX + maxX) / 2
    y = (minY + maxY) / 2
    
    fmt.Printf("%v %v\n", x, y) // the location of the next window Batman should jump to.
  }
}
