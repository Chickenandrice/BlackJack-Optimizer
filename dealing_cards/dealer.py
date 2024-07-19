import cards
import random

def new_deck(num_decks):
    play_cards = []
    for card in cards.deck: 
        play_cards.append(card)
    return play_cards*num_decks

def deal_cards(deck):
    return deck.pop(random.randint(0, len(deck)))
