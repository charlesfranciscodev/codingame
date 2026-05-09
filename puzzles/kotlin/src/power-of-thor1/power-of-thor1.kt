import java.util.*

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val lightX = input.nextInt() // the X position of the light of power
  val lightY = input.nextInt() // the Y position of the light of power
  var x = input.nextInt() // Thor's starting X position
  var y = input.nextInt() // Thor's starting Y position

  // game loop
  while (true) {
    val remainingTurns = input.nextInt() // The remaining amount of turns Thor can move. Do not remove this line.
    var move = StringBuilder()

    if (y < lightY) {
      move.append("S")
      y++
    } else if (y > lightY) {
      move.append("N")
      y--
    }

    if (x < lightX) {
      move.append("E")
      x++
    } else if (x > lightX) {
      move.append("W")
      x--
    }

    // A single line providing the move to be made: N NE E SE S SW W or NW
    println(move)
  }
}
