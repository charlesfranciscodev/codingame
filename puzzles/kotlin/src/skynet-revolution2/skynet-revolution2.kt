import java.util.Scanner
import java.util.ArrayDeque

fun main(args : Array<String>) {
  val graph = Graph()
  graph.readInitInput()
  graph.gameLoop()
}

class Node(val index:Int) {
  val links = ArrayList<Node>()
  var isGateway = false
  var isMarked = false

  fun nbGatewayLinks() : Int {
    return links.count { it.isGateway }
  }

  fun gatewayLink(): Node? {
    return links.firstOrNull { it.isGateway }
  }
}

class Graph {
  val input = Scanner(System.`in`)
  val nodes = ArrayList<Node>()
  val targetGateways = ArrayList<Node>()

  fun updateTargets(gateway: Node) {
    if (gateway.links.isEmpty()) {
      targetGateways.remove(gateway)
    }
  }

  fun reset() {
    for (node in nodes) {
      node.isMarked = false
    }
  }

  /** n1 and n2 are the indices of the nodes you wish to sever the link between */
  fun sever(n1: Int, n2: Int) {
    val builder = StringBuilder()
    builder.append(n1)
    builder.append(" ")
    builder.append(n2)
    println(builder.toString())
  }

  fun readInitInput() {
    val nbNodes = input.nextInt() // the total number of nodes in the level, including the gateways
    val nbLinks = input.nextInt() // the number of links
    val nbGateways = input.nextInt() // the number of exit gateways

    (0 until nbNodes).mapTo(nodes) { Node(it) }

    for (i in 0 until nbLinks) {
      val n1 = input.nextInt() // n1 and n2 defines a link between these nodes
      val n2 = input.nextInt()
      val node1 = nodes[n1]
      val node2 = nodes[n2]
      node1.links.add(node2)
      node2.links.add(node1)
    }

    for (i in 0 until nbGateways) {
      val index = input.nextInt() // the index of a gateway node
      val gateway = nodes[index]
      gateway.isGateway = true
      targetGateways.add(gateway)
    }
  }

  fun gameLoop() {
    while (true) {
      val agentIndex = input.nextInt() // The index of the node on which the Skynet agent is positioned this turn
      if (!blockNearbyAgent(agentIndex)) {
        if (!blockDoubleGateway(agentIndex)) {
          blockGateway()
        }
      }
    }
  }

  /** If the agent is linked to an exit, sever the link and return True. Otherwise, return False */
  fun blockNearbyAgent(agentIndex: Int): Boolean {
    val agentNode = nodes[agentIndex]
    for (node in agentNode.links) {
      if (node.isGateway) {
        sever(agentIndex, node.index)
        agentNode.links.remove(node)
        node.links.remove(agentNode)
        updateTargets(node)
        return true
      }
    }
    return false
  }

  /**
   * Slice the last link on the shortest path between the virus and a gateway using BFS.
   * Only danger nodes are considered in possible paths.
   * A danger node is a node with 1 or more gateway links.
   * The link is severed if the node is linked to 2 gateways.
   * */
  fun blockDoubleGateway(agentIndex: Int): Boolean {
    val agentNode = nodes[agentIndex]
    val queue = ArrayDeque<Node>()
    reset()
    agentNode.isMarked = true
    queue.add(agentNode)

    while(!queue.isEmpty()) {
      val currentNode = queue.pollFirst()
      for (neighbor in currentNode.links) {
        val nbGatewayLinks = neighbor.nbGatewayLinks()
        if (!neighbor.isGateway && nbGatewayLinks >= 1 && !neighbor.isMarked) {
          neighbor.isMarked = true
          if (nbGatewayLinks == 2) {
            val gateway = neighbor.gatewayLink()
            if (gateway != null) {
              sever(neighbor.index, gateway.index)
              neighbor.links.remove(gateway)
              gateway.links.remove(neighbor)
              updateTargets(gateway)
              return true
            }
          } else {
            queue.add(neighbor)
          }
        }
      }
    }
    return false
  }

  /** Slice a random gateway link. */
  fun blockGateway() {
    val gateway = targetGateways[0]
    val node = gateway.links[0]
    sever(gateway.index, node.index)
    gateway.links.remove(node)
    node.links.remove(gateway)
    updateTargets(gateway)
  }
}
