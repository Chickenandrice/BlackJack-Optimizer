from components.player import Player
from components.cards import new_deck
from components.dealer import Dealer


"""
make your strategy in this file with some things to consider:

- hard hands
- soft hands
- changing bet amounts based on previous hands 
- different dealer rules 
- splits 

"""


def simulate_your_strategy(player: Player, dealer: Dealer, bet_amount: int): 
    """
        basic strategy implementation with out consideration of double down or surrender

        Parameters: 

        player (Player): player object that is used to simulate a game using a basic strategy
        dealer (Dealer): dealer object that is used to simulate a game using a basic strategy
        bet_amount (int): the amount of simulation money that will be risked per simulation of Blackjack 
    """
    # sets up deck with 6 different playing decks 
    deck = new_deck(6)

    # assume dealer is already created 
    dealer.deal_self(deck)
    dlr_upcard = dealer.upcard() 

    # assume player is not dealt 
    player.bet(bet_amount)
    player.initial_deal(1, deck, dealer)
    hand_vals = player.get_hand_values(1)
    should_split = None



    # TODO: Make your own strategy here, I would not recommend changing anything else in this method because they are essential for the code to compile 

    

    # this last block checks the bet, clears player and dealer hands
    player.check_bet(dealer)
    player.new_hand()
    dealer.reset()
