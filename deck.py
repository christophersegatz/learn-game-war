import random
import card

#Global variables
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

class Deck:
    def __init__(self):
        #Create a deck of 52 cards
        self.all_cards = list
        for suit in suits:
            for rank in ranks:
                #create a card Object
                self.all_cards.append(card.Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()