import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val original = input.nextInt()
  val lineNumber = input.nextInt()
  var conwaySequence = ArrayList<Int>()
  conwaySequence.add(original)

  for (line in 1 until lineNumber) {
    val tempSequence = ArrayList<Int>()
    var count = 0
    var previous = conwaySequence[0]
    for (number in conwaySequence) {
      if (number == previous) {
        count++
      } else {
        tempSequence.add(count)
        tempSequence.add(previous)
        previous = number
        count = 1
      }
    }

    tempSequence.add(count)
    tempSequence.add(previous)
    conwaySequence = tempSequence
  }

  println(conwaySequence.joinToString(" "))
}
