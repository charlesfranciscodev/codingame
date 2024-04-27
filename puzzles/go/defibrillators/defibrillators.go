package main

import (
  "fmt"
  "os"
  "bufio"
  "strings"
  "strconv"
  "math"
)

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  var longitude string
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &longitude)
  var lon = toRadians(longitude)

  var latitude string
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &latitude)
  var lat = toRadians(latitude)
  
  var n int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &n)
  
  var min = math.Inf(1)
  var name = ""

  for i := 0; i < n; i++ {
    scanner.Scan()
    defib := strings.Split(scanner.Text(), ";")
    var defibLon = toRadians(defib[4])
    var defibLat = toRadians(defib[5])
    var x = (defibLon - lon) * math.Cos((lat + defibLat) / 2)
    var y = defibLat - lat
    var distance = math.Hypot(x, y) * 6371
    if distance < min {
      min = distance
      name = defib[1]
    }
  }
  
  fmt.Println(name)
}

// Convert degrees to radians
func toRadians(angle string) float64 {
  var degrees, _ = strconv.ParseFloat(strings.Replace(angle, ",", ".", -1), 64)
  return degrees * math.Pi / 180
}
