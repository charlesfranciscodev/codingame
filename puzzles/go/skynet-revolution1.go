package main

import "fmt"

var links []Link
var gateways []int

type Link struct {
  n1 int
  n2 int
}

func sever(link Link) {
  fmt.Printf("%v %v\n", link.n1, link.n2)
}

func block(agentNode int) {
  for _, gateway := range gateways {
    // Check for a direct link between the agent and a gateway
    for index, link := range links {
      if link == (Link{agentNode, gateway}) || link == (Link{gateway, agentNode}) {
        sever(link)
        links[index] = links[len(links) - 1]
        links = links[:len(links) - 1]
        return
      }
    }
  }
  blockFirstLink()
}

func blockFirstLink() {
  sever(links[0])
  links[0] = links[len(links) - 1]
  links = links[:len(links) - 1]
}

func main() {
  var nbNodes, nbLinks, nbExits int
  fmt.Scan(&nbNodes, &nbLinks, &nbExits)
  
  for i := 0; i < nbLinks; i++ {
    var n1, n2 int
    fmt.Scan(&n1, &n2)
    var link = Link{n1, n2}
    links = append(links, link)
  }

  for i := 0; i < nbExits; i++ {
    var gateway int
    fmt.Scan(&gateway)
    gateways = append(gateways, gateway)
  }

  for {
    var agentNode int
    fmt.Scan(&agentNode)
    block(agentNode)
  }
}
