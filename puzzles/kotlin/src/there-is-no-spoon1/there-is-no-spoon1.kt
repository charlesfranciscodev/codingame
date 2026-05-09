import java.util.Scanner

fun main(args : Array<String>) {
  val empty = '.'
  val node = '0'

  val input = Scanner(System.`in`)
  val width = input.nextInt() // the number of cells on the X axis
  val height = input.nextInt() // the number of cells on the Y axis
  if (input.hasNextLine()) {
    input.nextLine()
  }
  val grid = ArrayList<String>(height)
  for (y in 0 until height) {
    val line = input.nextLine() // width characters, each either 0 or .
    grid.add(line)
  }

  for (y in 0 until height) {
    for (x in 0 until width) {
      if (grid[y][x] == node) {
        // node
        val output = StringBuilder("$x $y ")

        // right neighbor
        var neighbor = empty
        for (neighborX in x + 1 until width) {
          neighbor = grid[y][neighborX]
          if (neighbor == node) {
            output.append("$neighborX $y ")
            break
          }
        }

        if (neighbor == empty) {
          output.append("-1 -1 ")
        }

        // bottom neighbor
        neighbor = empty
        for (neighborY in y + 1 until height) {
          neighbor = grid[neighborY][x]
          if (neighbor == node) {
            output.append("$x $neighborY")
            break
          }
        }

        if (neighbor == empty) {
          output.append("-1 -1")
        }

        println(output)
      }
    }
  }
}
