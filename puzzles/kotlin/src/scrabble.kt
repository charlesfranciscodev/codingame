import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val n = input.nextInt()
  if (input.hasNextLine()) {
    input.nextLine()
  }
  var bestWord = ""
  var highScore = 0
  val words = ArrayList<String>(n)

  for (i in 0 until n) {
    val word = input.nextLine()
    words.add(word)
  }
  val letters = input.nextLine()

  for (word in words) {
    val letters2 = letters.toMutableList()
    var isValid = true
    var currentScore = 0

    // calculate the total score for one word
    for (character in word) {
      val index = letters2.indexOf(character)
      if (index == -1) {
        isValid = false
        break
      }
      letters2.removeAt(index)
      currentScore += getScore(character)
    }

    if (isValid && currentScore > highScore) {
      highScore = currentScore
      bestWord = word
    }
  }

  println(bestWord)
}

fun getScore(letter:Char): Int {
  return when(letter) {
    'e', 'a', 'i', 'o','n', 'r', 't', 'l', 's','u' -> 1
    'd', 'g' -> 2
    'b', 'c', 'm', 'p' -> 3
    'f', 'h', 'v', 'w', 'y' -> 4
    'k' -> 5
    'j', 'x' -> 8
    else -> 10
  }
}
