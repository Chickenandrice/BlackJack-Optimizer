import cards
import random
import hand 

class Dealer():
    def __init__(self):
        self.hand = hand.Hand()

    def new_deck(num_decks):
        play_cards = []
        for card in cards.deck: 
            play_cards.append(card)

        return play_cards*num_decks

    def deal_card(deck):
        deck.pop(random.randint(0, len(deck)))

    def deal_self(self, deck):
        self.hand = deck.pop(random.randint(0, len(deck)))

    def compare_hands(self, player_hand):
        if player_hand > 21:
            return "loss"
        
        if self.hand > 21: 
            return "win"
        
        if self.hand > player_hand: 
            return "loss"
        elif self.hand == player_hand: 
            return "push"
        else:
            return "win"