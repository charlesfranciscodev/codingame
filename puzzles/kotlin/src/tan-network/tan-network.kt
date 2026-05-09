import java.util.Scanner
import java.util.Stack

fun main(args : Array<String>) {
  val network = Network()
  network.readGameInput()
  network.solve()
}

class Stop(val id: String, val fullName: String, val latitude: Double, val longitude: Double) {
  val routes = ArrayList<String>()

  fun distance(other: Stop): Double {
    val x = (other.longitude - longitude) * Math.cos((latitude + other.latitude) / 2)
    val y = other.latitude - latitude
    return Math.hypot(x, y) * 6371
  }
}

class Network {
  var start: String = ""
  var end: String = ""
  val stops = HashMap<String, Stop>()

  fun readGameInput() {
    val input = Scanner(System.`in`)
    start = input.next() // start id
    end = input.next() // end id
    val nbStops = input.nextInt()
    if (input.hasNextLine()) {
      input.nextLine()
    }
    for (i in 0 until nbStops) {
      val line = input.nextLine().split(",")
      val id = line[0]
      val fullName = line[1].replace("\"", "")
      val latitude = Math.toRadians(line[3].toDouble())
      val longitude = Math.toRadians(line[4].toDouble())
      val stop = Stop(id, fullName, latitude, longitude)
      stops[id] = stop
    }

    val nbRoutes = input.nextInt()
    if (input.hasNextLine()) {
      input.nextLine()
    }
    for (i in 0 until nbRoutes) {
      val route = input.nextLine().split(" ")
      val id1 = route[0]
      val id2 = route[1]
      stops[id1]?.routes?.add(id2)
    }
  }

  // Compute the shortest path between start and end using A*
  // Reference: https://en.wikipedia.org/wiki/A*_search_algorithm
  fun search(startId: String, endId: String): Map<String, String>? {
    val startStop = stops[startId]
    val endStop = stops[endId]
    val closedSet = HashSet<String>() // set of ids already evaluated
    val openSet = HashSet<String>() // set of discovered ids that are not evaluated yet
    val parents = HashMap<String, String>()
    val gScores = HashMap<String, Double>()
    val fScores = HashMap<String, Double>()
    openSet.add(startId)
    gScores[startId] = 0.0
    if (startStop != null && endStop != null) fScores[startId] = hCost(startStop, endStop)

    while (openSet.isNotEmpty()) {
      val minId = min(openSet, fScores)
      if (minId == endId) return parents // search is done
      val minStop = stops[minId] ?: break
      openSet.remove(minId)
      closedSet.add(minId)

      for (neighborId in minStop.routes) {
        if (!closedSet.contains(neighborId)) {
          if (!openSet.contains(neighborId)) openSet.add(neighborId)
          val neighborStop = stops[neighborId]
          var gScore = gScores.getOrDefault(minId, Double.MAX_VALUE)
          if (neighborStop != null) gScore += minStop.distance(neighborStop)
          if (gScore < gScores.getOrDefault(neighborId, Double.MAX_VALUE)) {
            parents[neighborId] = minId
            gScores[neighborId] = gScore
            if (neighborStop != null && endStop != null) fScores[neighborId] = gScore + hCost(neighborStop, endStop)
          }
        }
      }
    }

    return null
  }

  fun min(openSet: Set<String>, fScores: Map<String, Double>): String {
    var minId = openSet.first()
    var minFScore = Double.MAX_VALUE
    for (id in openSet) {
      val fScore = fScores.getOrDefault(id, Double.MAX_VALUE)
      if (fScore < minFScore) {
        minId = id
        minFScore = fScore
      }
    }
    return minId
  }

  fun hCost(currentStop: Stop, endStop: Stop): Double {
    return currentStop.distance(endStop)
  }

  fun solve() {
    if (start == end) {
      println(stops[start]?.fullName)
      return
    }

    val parents = search(start, end)
    var currentId = end
    val stack = Stack<String>()

    if (parents == null) {
      println("IMPOSSIBLE")
      return
    }

    while (parents.containsKey(currentId)) {
      stack.push(currentId)
      currentId = parents.getOrDefault(currentId, "")
    }

    stack.push(currentId)
    while (stack.isNotEmpty()) {
      println(stops[stack.pop()]?.fullName)
    }
  }
}
