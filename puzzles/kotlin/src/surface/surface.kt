import java.util.Scanner
import java.util.ArrayDeque

const val LAND = '#'
const val WATER = 'O'
const val DEFAULT_INDEX = -1

fun main(args : Array<String>) {
  val grid = Grid()
  grid.readGameInput()
  grid.test()
}

data class Square(val x: Int, val y: Int, val terrain: Char, var lakeIndex: Int = DEFAULT_INDEX)

class Grid {
  val input = Scanner(System.`in`)
  var width = 0
  var height = 0
  val nodes = ArrayList<List<Square>>()
  val lakes = HashMap<Int, Int>() // lake_index -> surface area

  fun readGameInput() {
    width = input.nextInt()
    height = input.nextInt()
    if (input.hasNextLine()) {
      input.nextLine()
    }
    for (y in 0 until height) {
      val row = input.nextLine().withIndex().map { Square(it.index, y, it.value) }
      nodes.add(row)
    }
  }

  fun test() {
    val n = input.nextInt()
    for (i in 0 until n) {
      val x = input.nextInt()
      val y = input.nextInt()
      println(area(x, y))
    }
  }

  fun area(x: Int, y: Int): Int {
    val node = nodes[y][x]
    if (node.terrain == LAND) {
      return 0
    }
    if (node.lakeIndex == DEFAULT_INDEX) {
      floodFill(node)
    }
    return lakes.getOrDefault(node.lakeIndex, 0)
  }

  // Source https://en.wikipedia.org/wiki/Flood_fill
  fun floodFill(start: Square) {
    val queue = ArrayDeque<Square>()
    var totalArea = 0
    start.lakeIndex = start.y * width + start.x
    queue.add(start)

    while (!queue.isEmpty()) {
      totalArea++
      val current = queue.poll()
      fillNeighbors(queue, current, start.lakeIndex)
    }

    lakes.put(start.lakeIndex, totalArea)
  }

  fun fillNeighbors(queue: ArrayDeque<Square>, square: Square, lakeIndex: Int) {
    if (square.x + 1 < width) {
      val rightNeighbor = nodes[square.y][square.x + 1]
      fill(queue, rightNeighbor, lakeIndex)
    }

    if (square.x > 0) {
      val leftNeighbor = nodes[square.y][square.x - 1]
      fill(queue, leftNeighbor, lakeIndex)
    }

    if (square.y + 1 < height) {
      val downNeighbor = nodes[square.y + 1][square.x]
      fill(queue, downNeighbor, lakeIndex)
    }

    if (square.y > 0) {
      val upNeighbor = nodes[square.y - 1][square.x]
      fill(queue, upNeighbor, lakeIndex)
    }
  }

  fun fill(queue: ArrayDeque<Square>, square: Square, lakeIndex: Int) {
    if (square.terrain == WATER && square.lakeIndex == DEFAULT_INDEX) {
      square.lakeIndex = lakeIndex
      queue.add(square)
    }
  }
}
