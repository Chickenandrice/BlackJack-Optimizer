import strategies.default as df
import strategies.strategies as st
from components.player import Player
from components.cards import new_deck
from components.dealer import Dealer


def simulate_three_cards_no_split(number_trials, player_name, player_balance): 
    dlr = Dealer()
    Plyer = Player(player_name, player_balance) 
    while number_trials > 0: 
        deck = new_deck(6)
        Plyer.bet(100)
        dealer_hand, dealer_total = dlr.deal_self(deck)
        Plyer.initial_deal(1, deck, dlr)
        Plyer.split(1, deck, dlr)
        Plyer.hit(1, deck, dlr)
        Plyer.check_bet(dealer_total)
        Plyer.new_hand()
        dlr.reset() 
        number_trials -= 1

def simulate_two_cards_no_split(number_trials, player_name, player_balance): 
    dlr = Dealer()
    Plyer = Player(player_name, player_balance) 
    while number_trials > 0:
        deck = new_deck(6)
        Plyer.bet(100)
        hand, total = dlr.deal_self(deck)
        Plyer.hit(1, deck, dlr)
        Plyer.hit(1, deck, dlr)
        Plyer.check_bet(total)
        Plyer.new_hand()
        dlr.reset() 
        number_trials -= 1

simulate_three_cards_no_split(100, "mark", 10000)