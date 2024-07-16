import dealing.cards as cards
import quantumrandom

def new_deck():
    play_cards = cards.deck
    return play_cards

def deal_cards(deck, num_cards): 
    return deck.pop(quantumrandom.randint(1, ))

print(quantumrandom.randint(0, 20)) 
