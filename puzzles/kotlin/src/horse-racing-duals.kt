import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val n = input.nextInt()
  val strengths = ArrayList<Int>()
  for (i in 0 until n) {
    strengths.add(input.nextInt())
  }

  strengths.sort()

  val min = (0 until n - 1)
      .map { strengths[it + 1] - strengths[it] }
      .min()
      ?: 10000000

  println(min)
}
