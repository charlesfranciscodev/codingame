import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val nbElements = input.nextInt() // Number of elements which make up the association table.
  val nbNames = input.nextInt() // Number of file names to be analyzed.
  val table = HashMap<String, String>()
  for (i in 0 until nbElements) {
    val extension = input.next().toLowerCase() // file extension
    val type = input.next() // MIME type.
    table.put(extension, type)
  }
  input.nextLine()

  for (i in 0 until nbNames) {
    val name = input.nextLine().toLowerCase() // One file name per line.
    val dotIndex = name.lastIndexOf('.')
    if (dotIndex == -1 || dotIndex == name.length - 1) {
      println("UNKNOWN")
    } else {
      val extension = name.substring(dotIndex + 1).toLowerCase()
      if (table.contains(extension)) {
        println(table[extension])
      } else {
        println("UNKNOWN")
      }
    }
  }
}
