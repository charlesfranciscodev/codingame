package main

import "fmt"
import "os"
import "bufio"

func main() {
  const EMPTY = byte('.')
  const NODE = byte('0')
  var grid []string

  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  // width: the number of cells on the X axis
  var width int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &width)
  
  // height: the number of cells on the Y axis
  var height int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &height)
  
  for i := 0; i < height; i++ {
    scanner.Scan()
    line := scanner.Text()
    grid = append(grid, line)
  }
  
  for y := 0; y < height; y++ {
    for x := 0; x < width; x++ {
      if grid[y][x] == NODE {
        // node
        fmt.Printf("%v %v ", x, y)

        // right neighbor
        var neighbor = EMPTY
        for neighborX := x + 1; neighborX < width; neighborX++ {
          neighbor = grid[y][neighborX]
          if neighbor == NODE {
            fmt.Printf("%v %v ", neighborX, y)
            break
          }
        }

        if neighbor == EMPTY {
          fmt.Print("-1 -1 ")
        }

        // bottom neighbor
        neighbor = EMPTY
        for neighborY := y + 1; neighborY < height; neighborY++ {
          neighbor = grid[neighborY][x]
          if neighbor == NODE {
            fmt.Printf("%v %v ", x, neighborY)
            break
          }
        }

        if neighbor == EMPTY {
          fmt.Print("-1 -1 ")
        }

        fmt.Println()
      }
    }
  }
}
