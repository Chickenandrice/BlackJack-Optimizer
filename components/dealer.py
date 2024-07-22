import cards 
import random
from hand import Hand

# fix this by adding up all the numbers and then comparing 
def compare_hands(dealer_hand, player_hand):
    if player_hand[0] > 21:
        return "loss"
        
    if dealer_hand[0] > 21: 
        return "win"
        
    if dealer_hand[0] > player_hand[0]: 
        return "loss"
    elif dealer_hand[0] == player_hand[0]: 
        return "push"
    else: 
        return "win"

class Dealer():
    def __init__(self):
        self.hand = []

    def deal_player(self, deck): 
        return deck.pop(random.randint(0, len(deck)))

    def deal_self(self, deck):
        self.hand.append(deck.pop(random.randint(0, len(deck))))
    
    def first_card():
        pass
    def facedown_cards():
        pass
    
    def get_hand(self):
        return self.hand