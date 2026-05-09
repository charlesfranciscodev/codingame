/* jshint esversion: 6 */
const PLAYER1 = "PLAYER1";
const PLAYER2 = "PLAYER2";
const WAR = "WAR";
const GAME_OVER = "GAME_OVER";

const CARD_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
               "J": 11, "Q": 12, "K": 13, "A": 14};
       
class Card {
  constructor(value, suit) {
    this.value = value;
    this.suit = suit;
  }

  intValue() {
    return Number(CARD_VALUES[this.value]);
  }

  isLessThan(other) {
    return this.intValue() < other.intValue();
  }

  toString() {
    return this.value + this.suit;
  }
}

class Game {
  constructor() {
    this.deck1 = this.read_game_input();
    this.deck2 = this.read_game_input();
    this.nbRounds = 0;
  }

  read_game_input() {
    let cards = [];
    let nbCardsPlayer = parseInt(readline());

    for (let i = 0; i < nbCardsPlayer; ++i) {
      let valueSuit = readline();
      let value = valueSuit.substring(0, valueSuit.length - 1);
      let suit = valueSuit.charAt(valueSuit.length - 1);
      cards.push(new Card(value, suit));
    }

    return cards;
  }

  play() {
    let index = 0;
    let result = "";
    while (result !== GAME_OVER) {
      result = this.play_turn(index);
      let rotate_index = index + 1;
      if (result === PLAYER1) {
        this.nbRounds += 1;
        this.deck1 = this.rotate(this.deck1, rotate_index);
        this.deck1 = this.add(this.deck1, this.slice(this.deck2, 0, rotate_index)); // take other player's cards
        this.deck2 = this.slice(this.deck2, rotate_index, this.deck2.length); // remove other player's cards
        index = 0;
      } else if (result === PLAYER2) {
        this.nbRounds += 1;
        this.deck2 = this.add(this.deck2, this.slice(this.deck1, 0, rotate_index)); // take other player's cards
        this.deck1 = this.slice(this.deck1, rotate_index, this.deck1.length); // remove other player's cards
        this.deck2 = this.rotate(this.deck2, rotate_index);
        index = 0;
      } else if (result === WAR) {
        index += 4;
      }
    }
  }

  rotate(deck, index) {
    let slice1 = this.slice(deck, index, deck.length);
    let slice2 = this.slice(deck, 0, index);
    let newDeck = this.add(slice1, slice2);
    return newDeck;
  }

  slice(deck, start_index, end_index) {
    let newDeck = [];
    for (let i = start_index; i < end_index; ++i) {
      let card = deck[i];
      newDeck.push(new Card(card.value, card.suit));
    }
    return newDeck;
  }

  add(deck1, deck2) {
    for (let i = 0; i < deck2.length; ++i) {
      let card = deck2[i];
      deck1.push(new Card(card.value, card.suit));
    }
    return deck1;
  }

  /* Returns the result of one game turn:
  PLAYER1 if player 1 wins this round,
  PLAYER2 if player 2 wins this round,
  WAR if the two cards played are of equal value
  GAME_OVER if the game is over*/
  play_turn(index) {
    if (index > this.deck1.length || index > this.deck2.length) {
      print("PAT");
      return GAME_OVER;
    }
    if (this.check_game_over() === GAME_OVER) {
      return GAME_OVER;
    }

    let card1 = this.deck1[index];
    let card2 = this.deck2[index];
    if (card2.isLessThan(card1)) {
      return PLAYER1;
    } else if (card1.isLessThan(card2)) {
      return PLAYER2;
    } else {
      return WAR;
    } 
  }

  check_game_over() {
    if (this.deck1.length === 0) {
      print("2 " + this.nbRounds);
      return GAME_OVER;
    }
    if (this.deck2.length === 0) {
      print("1 " + this.nbRounds);
      return GAME_OVER;
    }
    return "";
  }
}

let game = new Game();
game.play();
