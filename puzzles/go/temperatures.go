package main

import "fmt"
import "os"
import "bufio"
import "strings"
import "strconv"
import "math"

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  // n: the number of temperatures to analyse
  var n int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &n)
  var minT = 5526.0

  scanner.Scan()
  inputs := strings.Split(scanner.Text(), " ")
  for i := 0; i < n; i++ {
    // t: a temperature expressed as an integer ranging from -273 to 5526
    t, _ := strconv.ParseFloat(inputs[i], 32)
    if math.Abs(t) < math.Abs(minT) || math.Abs(t) == math.Abs(minT) && t > minT {
      minT = t
    }
  }
  
  if n == 0 {
    fmt.Println(0)
  } else {
    fmt.Println(int(minT))
  }
}
