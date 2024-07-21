import cards
import random

class Dealer():
    def __init__(self, hand):
        self.hand = hand

    def new_deck(num_decks):
        play_cards = []
        for card in cards.deck: 
            play_cards.append(card)

        return play_cards*num_decks

    def deal_card(deck):
        return deck.pop(random.randint(0, len(deck)))

    def compare_hands(self, player_hand): 
        if self.hand > player_hand: 
            return "loss"
        elif self.hand == player_hand: 
            return "push"
        else:
            return "win"
    