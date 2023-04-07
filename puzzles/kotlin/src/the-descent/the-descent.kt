import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)

  // game loop
  while (true) {
    var max = -1
    var indexMax = 0
    for (i in 0 until 8) {
      val height = input.nextInt() // represents the height of one mountain.
      if (height > max) {
        max = height
        indexMax = i
      }
    }

    println(indexMax) // The index of the mountain to fire on.
  }
}

