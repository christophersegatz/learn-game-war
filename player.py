
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = list
    
    def remove_one(self):
        return self.all_cards.pop()
    
    def add_cards(self, new_cards):
        #Append the new cards to the existing list of cards
        #if new_cards is a list, add each card to the list
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        #if new_cards is a single card, add it to the list
        else:
            self.all_cards.extend(new_cards)
    
    def __str__(self):
        return "Player {player} has {cards} cards.".format(player = self.name, cards = len(self.all_cards))