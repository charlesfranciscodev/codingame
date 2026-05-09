Here is the Markdown documentation for the Kotlin file `war.kt` located in the `puzzles/kotlin/src` directory of the `charlesfranciscodev/codingame` GitHub repository:

---

# War Game Simulation

This is a Kotlin implementation of the War card game simulation. The War card game is a simple two-player card game where each player gets half of the deck and then they take turns playing the top card from their hand. The player with the highest card wins the round and takes both cards. If both players play cards of the same value, then a "war" is declared and each player plays three additional cards. The winner of the "war" round takes all the cards played in that round.

## Code Structure

The code is divided into the following classes:

### Card

This class represents a single playing card in the game. It has two properties: `value` and `suit`. The `value` property is an integer value from 2 to 14 representing the card value, and the `suit` property is a string representing the card suit.

### Deck

This class represents a deck of playing cards. It has a list of `Card` objects and functions for shuffling the deck and dealing cards to players.

### Player

This class represents a player in the game. It has a list of `Card` objects representing the player's hand and functions for playing cards, adding cards to the player's hand, and checking if the player has any cards left.

### Game

This class represents the game itself. It has two `Player` objects, a `Deck` object, and functions for playing the game and determining the winner.
