import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val lon = toRadians(input.next())
  val lat = toRadians(input.next())
  val n = input.nextInt()
  if (input.hasNextLine()) {
    input.nextLine()
  }
  var min = Double.POSITIVE_INFINITY
  var name = ""

  for (i in 0 until n) {
    val defib = input.nextLine().split(";")
    val defibLon = toRadians(defib[4])
    val defibLat = toRadians(defib[5])
    val x = (defibLon - lon) * Math.cos((lat + defibLat) / 2)
    val y = defibLat - lat
    val distance = Math.hypot(x, y) * 6371
    if (distance < min) {
      min = distance
      name = defib[1]
    }
  }

  println(name)
}

// Convert degrees to radians
fun toRadians(angle: String): Double {
  return Math.toRadians(angle.replace(',', '.').toDouble())
}
