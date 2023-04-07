import java.util.*

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val surfaceN = input.nextInt() // the number of points used to draw the surface of Mars.
  for (i in 0 until surfaceN) {
    val landX = input.nextInt() // X coordinate of a surface point.
    val landY = input.nextInt() // Y coordinate of a surface point.
  }

  // game loop
  while (true) {
    val X = input.nextInt()
    val Y = input.nextInt()
    val hSpeed = input.nextInt() // the horizontal speed (in m/s), can be negative.
    val vSpeed = input.nextInt() // the vertical speed (in m/s), can be negative.
    val fuel = input.nextInt() // the quantity of remaining fuel in liters.
    val rotate = input.nextInt() // the rotation angle in degrees (-90 to 90).
    var power = input.nextInt() // the thrust power (0 to 4).

    if (vSpeed <= -40) {
      power = Math.min(4, power + 1)
    } else {
      power = Math.max(0, power - 1)
    }

    // 2 integers: rotate power.
    // rotate is the desired rotation angle (should be 0 for level 1)
    // power is the desired thrust power (0 to 4).
    println("0 $power")
  }
}
