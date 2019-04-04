import java.util.*

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val width = input.nextInt()
  val height = input.nextInt()
  if (input.hasNextLine()) {
    input.nextLine()
  }
  val text = input.nextLine().toUpperCase()

  for (i in 0 until height) {
    val row = input.nextLine()
    val output = StringBuilder()
    for (character in text) {
      var position = character.toInt() - 'A'.toInt()
      if (position < 0 || position > 25) {
        position = 26
      }
      val start = position * width
      val end = position * width + width
      output.append(row.substring(start, end))
    }
    println(output.toString())
  }
}
