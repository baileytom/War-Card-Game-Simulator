import random
import time
from enum import Enum

class Game:
    """ This class represents a game of War."""
    def __init__(self):
    
        # Create players
        self.player1 = Player('player1')
        self.player2 = Player('player2')
        
        # Create the deck
        self.deck = Deck()
        
        # List for cards on the table
        self.table = []
    
    def dealHand(self):
    
        # Shuffle the deck
        self.deck.shuffle()
        
        # Give each player 26 cards
        while len(self.deck.cards) > 0:
            self.player1.takeCard(self.deck.drawCard())
            self.player2.takeCard(self.deck.drawCard())
            
            
        
    def play(self):
        
        print("_____________")
        # Line to make it easier to read
        
        # Play the game
        
        # Draw a card
        player1Card = self.player1.pullCard()
        print("Player 1 draws", player1Card)
        # Put the card on the table
        self.table.append(player1Card)
        
        # Draw a card
        player2Card = self.player2.pullCard()
        print("Player 2 draws", player2Card)
        # Put the card on the table
        self.table.append(player2Card)

        # Create variables to value the cards
        card1val = self.val(player1Card)
        card2val = self.val(player2Card)
        
        while card1val == card2val:

            print("WAR!")
            
            if self.player1.getCardAmount() == 0 or self.player2.getCardAmount() == 0:
                break
            
            #self.pause()
            player1Card = self.player1.pullCard()
            print("Player 1 draws", player1Card)
            
            self.table.append(player1Card)
            
            player2Card = self.player2.pullCard()
            print("Player 2 draws", player2Card)
            
            self.table.append(player2Card)
            
            card1val = self.val(player1Card)
            card2val = self.val(player2Card)
            
        if card1val > card2val:
            print("Player 1 takes the pile!")
            for card in self.table:
                self.player1.cards.append(card)
            self.table = []
        else:
            print("Player 2 takes the pile!")
            for card in self.table:
                self.player2.cards.append(card)
            self.table = []
            
        print("Player 1's cards:", self.player1.getCardAmount())
        print("Player 2's cards:", self.player2.getCardAmount())
        
        #self.pause()
        

    def val(self, card):
        # returns numerical value of card for comparison
        return self.deck.ranks.index(card.rank)+1
        
    def pause(self):
        time.sleep(.5)
        
class Deck:
    """ This class represents a deck of cards. """
    def __init__(self):
        self.suits = 'cdhs'
        self.ranks = '23456789TJQKA'
        self.cards = [] # List containing all cards (instances) in the deck
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        # Shuffles the contents of the deck.
        random.shuffle(self.cards)
    
    def drawCard(self):
        # Returns a card from the contents of the deck & removes said card from the deck.
        random_index = random.randint(0, len(self.cards)-1)
        return self.cards.pop(random_index)
        
    def showCards(self):
        # Prints each card in the deck, for debugging/testing.
        for card in self.cards:
            print(card)
        
class Card:
    """ This class represents a card. """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __repr__(self):
        return self.rank + self.suit
            
class Player:
    """ This class represents a player. """
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def getCardAmount(self):
        return len(self.cards)
        
    def takeCard(self, card):
        self.cards.append(card)
        
    def pullCard(self):
        random_index = random.randint(0, len(self.cards)-1)
        return self.cards.pop(random_index)
        
game = Game()
game.dealHand()
run = True
rounds = 0
while run:
    rounds += 1
    if game.player1.getCardAmount() >= 52:
        print("Player 1 wins!")
        break
    if game.player2.getCardAmount() >= 52:
        print("Player 2 wins!")
        break
    game.play()
print(rounds, "rounds")