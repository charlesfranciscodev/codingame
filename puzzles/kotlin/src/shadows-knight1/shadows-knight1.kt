import java.util.*

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val width = input.nextInt() // width of the building.
  val height = input.nextInt() // height of the building.
  val n = input.nextInt() // maximum number of turns before game over.
  var x = input.nextInt()
  var y = input.nextInt()

  var minX = 0
  var maxX = width -1
  var minY = 0
  var maxY = height - 1

  // game loop
  while (true) {
    val bombDir = input.next() // the direction of the bombs from batman's current location

    when (bombDir) {
      "U" -> {
        maxY = y - 1
        minX = x
        maxX = x
      }

      "UR" -> {
        minX = x + 1
        maxY = y - 1
      }

      "R" -> {
        minX = x + 1
        minY = y
        maxY = y
      }

      "DR" -> {
        minX = x + 1
        minY = y + 1
      }

      "D" -> {
        minY = y + 1
        minX = x
        maxX = x
      }

      "DL" -> {
        maxX = x - 1
        minY = y + 1
      }

      "L" -> {
        maxX = x - 1
        minY = y
        maxY = y
      }

      // UL
      else -> {
        maxX = x - 1
        maxY = y - 1
      }
    }

    x = (minX + maxX) / 2
    y = (minY + maxY) / 2
    // the location of the next window Batman should jump to.
    println("$x $y")
  }
}
