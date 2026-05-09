package main

import "fmt"

func main() {
  var surfaceN int
  fmt.Scan(&surfaceN)
  
  for i := 0; i < surfaceN; i++ {
    var landX, landY int
    fmt.Scan(&landX, &landY)
  }
  for {
    // vSpeed: the vertical speed (in m/s), can be negative.
    // power: the thrust power (0 to 4).
    var X, Y, hSpeed, vSpeed, fuel, angle, power int
    fmt.Scan(&X, &Y, &hSpeed, &vSpeed, &fuel, &angle, &power)
    
    if (vSpeed <= -40) {
      power = 4
    } else {
      power = 0
    }
    
    fmt.Printf("%v %v\n", angle, power)
  }
}
