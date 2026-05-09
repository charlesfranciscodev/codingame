package main

import "fmt"
import "os"
import "bufio"
import "strings"

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  var width int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &width)
  
  var height int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &height)
  
  scanner.Scan()
  var text = strings.ToUpper(scanner.Text())
  for i := 0; i < height; i++ {
    scanner.Scan()
    var row = scanner.Text()
    var output = "" // could use strings.Builder instead
    for _, r := range text {
      var position = int(r - 'A')
      if (position < 0 || position > 25) {
        position = 26
      }
      var start = position * width
      var end = start + width
      output += row[start:end] // ASCII substring
    }
    fmt.Println(output)
  }
}
