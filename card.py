import random

class Card:
    def __init__(self, suit, rank):
         #Define the Values of the cards
        values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
            'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

