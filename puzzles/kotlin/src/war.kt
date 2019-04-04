import java.util.Scanner
import kotlin.system.exitProcess

fun main(args : Array<String>) {
  val game = Game()
  game.play()
}

/**
 * Represents the result of one game turn:
 * PLAYER1 if player 1 wins this round,
 * PLAYER2 if player 2 wins this round,
 * WAR if the two cards played are of equal value
 * */
enum class Result {
  PLAYER1,
  PLAYER2,
  WAR
}

class Card(val value: String, val suit: String) : Comparable<Card> {
  companion object {
    val intValues: HashMap<String, Int> = hashMapOf(
        "2" to 2, "3" to 3, "4" to 4, "5" to 5, "6" to 6, "7" to 7, "8" to 8, "9" to 9, "10" to 10,
        "J" to 11,  "Q" to 12, "K" to 13, "A" to 14
    )
  }

  override fun compareTo(other: Card): Int {
    val value1 = intValues.getOrDefault(value, 0)
    val value2 = intValues.getOrDefault(other.value, 0)
    return value1 - value2
  }
}

class Game {
  val input = Scanner(System.`in`)
  var deck1 = readGameInput()
  var deck2 = readGameInput()
  var nbRounds = 0

  fun readGameInput(): List<Card> {
    val n = input.nextInt() // the number of cards for the player
    val cards = ArrayList<Card>(n)
    for (i in 0 until n) {
      val valueSuit = input.next()
      val value = valueSuit.substring(0, valueSuit.length - 1)
      val suit = valueSuit.substring(valueSuit.length - 1)
      cards.add(Card(value, suit))
    }
    return cards
  }

  fun play() {
    var index = 0
    while (true) {
      val result = playTurn(index)
      val rotateIndex = index + 1
      if (result == Result.PLAYER1) {
        nbRounds++
        deck1 = rotate(deck1, rotateIndex)
        deck1 += deck2.take(rotateIndex) // take other player's cards
        deck2 = deck2.drop(rotateIndex) // remove other player's cards
        index = 0
      } else if (result == Result.PLAYER2) {
        nbRounds++
        deck2 += deck1.take(rotateIndex) // take other player's cards
        deck1 = deck1.drop(rotateIndex) // remove other player's cards
        deck2 = rotate(deck2, rotateIndex)
        index = 0
      } else {
        // WAR
        index += 4
      }
    }
  }

  fun rotate(deck: List<Card>, index: Int): List<Card> {
    return deck.drop(index) + deck.take(index)
  }

  /** Returns the result of one game turn */
  fun playTurn(index: Int): Result {
    if (index > deck1.size || index > deck2.size) {
      println("PAT")
      exitProcess(0)
    }

    checkGameOver()

    val card1 = deck1[index]
    val card2 = deck2[index]

    return when {
      card2 < card1 -> Result.PLAYER1
      card1 < card2 -> Result.PLAYER2
      else -> Result.WAR
    }
  }

  fun checkGameOver() {
    if (deck1.isEmpty()) {
      println("2 $nbRounds")
      exitProcess(0)
    }

    if (deck2.isEmpty()) {
      println("1 $nbRounds")
      exitProcess(0)
    }
  }
}
