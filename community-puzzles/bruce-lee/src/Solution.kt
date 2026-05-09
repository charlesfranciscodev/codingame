import java.util.*

fun main(args: Array<String>) {
  val `in` = Scanner(System.`in`)
  val unary = `in`.nextLine()
  val binary = toBinary(unary)
  System.err.println(binary)
  val ascii = toAscii(binary)
  System.out.println(ascii)
}

fun toBinary(unary: String): String {
  var binary = ""
  val array = unary.split(" ")
  var digit = false // false -> 0, true -> 1
  for (i in array.indices) {
    val s = array[i]
    if (i % 2 == 0) {
      // first sequence
      when (s) {
        "00" -> digit = false
        "0" -> digit = true
        else -> {
          System.out.println("INVALID")
          System.exit(0)
        }
      }
    } else {
      // second sequence
      val c = if (digit) '1' else '0'
      for (j in 0 until s.length) {
        if (s[j] != '0') {
          System.out.println("INVALID")
          System.exit(0)
        }
        binary += c
      }
    }
  }
  return binary
}

fun toAscii(binary: String): String {
  val length = 7
  var ascii = ""

  if (binary.length % 7 != 0) {
    System.out.println("INVALID")
    System.exit(0)
  }

  var i = 0
  while (i < binary.length) {
    val sub = binary.substring(i, i + length)
    val x = Integer.parseInt(sub, 2)
    val c = x.toChar()
    ascii += c
    i += length
  }
  return ascii
}
