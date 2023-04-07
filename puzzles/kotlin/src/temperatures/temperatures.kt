import java.util.*

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val n = input.nextInt() // the number of temperatures to analyse
  var min = 5526
  for (i in 0 until n) {
    val temp = input.nextInt() // a temperature expressed as an integer ranging from -273 to 5526
    if (Math.abs(temp) < Math.abs(min) || Math.abs(temp) == Math.abs(min) && temp > min) {
      min = temp
    }
  }

  val result = if (n == 0) 0 else min
  println(result)
}
