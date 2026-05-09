package main

import (
  "fmt"
  "os"
  "bufio"
  "strings"
)

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  // dictionary to map file extensions to mime types
  var table = make(map[string]string)
  var nbElements int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &nbElements)
  
  var nbNames int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &nbNames)
  
  for i := 0; i < nbElements; i++ {
    var extension, mimeType string
    scanner.Scan()
    fmt.Sscan(scanner.Text(), &extension, &mimeType)
    table[strings.ToLower(extension)] = mimeType
  }

  for i := 0; i < nbNames; i++ {
    scanner.Scan()
    name := strings.ToLower(scanner.Text())
    var dotIndex = strings.LastIndex(name, ".")
    if dotIndex == -1 || dotIndex == len(name) - 1 {
      fmt.Println("UNKNOWN")
    } else {
      var extension = name[dotIndex + 1:]
      mimeType, ok := table[extension]
      if ok {
        fmt.Println(mimeType)
      } else {
        fmt.Println("UNKNOWN")
      }
    }
  }
}
