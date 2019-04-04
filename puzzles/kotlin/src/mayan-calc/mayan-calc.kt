import java.util.Scanner

const val BASE = 20
val input = Scanner(System.`in`)

fun main(args : Array<String>) {
  val width = input.nextInt()
  val height = input.nextInt()
  val numerals = ArrayList<String>() // mayan numerals
  val numeralMap = HashMap<String, Long>() // mayan numeral -> base 20 number

  for (i in 0 until height) {
    val row = input.next()
    numerals.add(row)
  }

  // Store the mayan numerals in a map
  for (i in 0 until BASE) {
    val numeral = StringBuilder()
    val column = i * width

    for (row in numerals) {
      for (j in column until column + width) {
        numeral.append(row[j])
      }
      numeral.append('\n')
    }

    numeralMap[numeral.toString()] = i.toLong()
  }

  // Read the first and second number
  val numArray1 = readNum(numeralMap, height)
  val numArray2 = readNum(numeralMap, height)
  val num1 = convertBase20To10(numArray1)
  val num2 = convertBase20To10(numArray2)

  val operation = input.next()

  // Calculate the result of the operation in base 10
  val result = when (operation) {
    "+" -> num1 + num2
    "-" -> num1 - num2
    "*" -> num1 * num2
    else -> num1 / num2
  }

  // Convert the result back to the original base
  val numArray = convertBase10To20(result)
  for (number in numArray) {
    for ((numeral, n) in numeralMap) {
      if (n == number) {
        print(numeral)
      }
    }
  }
}

fun readNum(numeralMap: HashMap<String, Long>, height: Int): List<Long> {
  var numeral = StringBuilder()
  val numArray = ArrayList<Long>()

  val nbLines = input.nextInt()
  for (i in 0 until nbLines) {
    val numLine = input.next()
    numeral.append(numLine)
    numeral.append('\n')
    if (i % height == height - 1) {
      // last column
      val number = numeralMap.getOrDefault(numeral.toString(), 0L)
      numArray.add(number)
      numeral = StringBuilder() // reset
    }
  }

  return numArray.reversed()
}

fun convertBase20To10(numArray: List<Long>): Long {
  return numArray.mapIndexed { i, num -> num * Math.pow(BASE.toDouble(), i.toDouble()).toLong() }.sum()
}

fun convertBase10To20(num: Long): List<Long>  {
  var number = num
  val numArray = ArrayList<Long>()

  // avoid division by 0
  if (number == 0L) {
    numArray.add(0L)
    return numArray
  }

  while (number != 0L) {
    numArray.add(number % BASE)
    number /= BASE
  }

  return numArray.reversed()
}
