import java.util.*

fun append(streak: Int, output: StringBuilder, array: List<Int>, beginIndex:Int, endIndex: Int, i: Int) {
  when {
    streak > 2 -> output.append(array[beginIndex], '-', array[endIndex])
    streak == 2 -> output.append(array[beginIndex], ',', array[endIndex])
    else -> output.append(array[i])
  }
  if (i != array.size - 1) {
    output.append(',')
  }
}

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val line = input.nextLine()
  val substring = line.substring(1, line.length - 1)
  val array = substring.split(",").map{ it.toInt() }.sorted()

  val output = StringBuilder()
  var streak = 1
  var beginIndex = 0
  var endIndex = 0

  for (i in 0 until array.size - 1) {
    if (array[i] + 1 == array[i + 1]) {
      streak++
      endIndex = i + 1
    } else {
      append(streak, output, array, beginIndex, endIndex, i)
      beginIndex = i + 1
      streak = 1
    }
  }

  // last index
  append(streak, output, array, beginIndex, endIndex, array.size - 1)

  println(output.toString())
}
