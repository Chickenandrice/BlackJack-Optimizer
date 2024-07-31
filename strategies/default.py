import strategies.default as df
import strategies.strategies as st
from components.player import Player
from components.cards import new_deck
from components.dealer import Dealer



def simulate_default(player: Player, dealer: Dealer, bet_amount: int): 
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

    # checks if a hand should be split based off a value 
    should_split = None
    if hand_vals[0] == hand_vals[1]:
        if hand_vals[0] in ['Ace', '8']:
            should_split = True
        elif hand_vals[0] in ['2', '3'] and dlr_upcard[0] in ['4', '5','6','7']:
            should_split = True
        elif hand_vals[0] == '6' and dlr_upcard[0] in ['3', '4', '5','6']:
            should_split = True 
        elif hand_vals[0] == '7' and dlr_upcard[0] in ['2', '3', '4', '5','6']:
            should_split = True
        elif hand_vals[0] == '9' and dlr_upcard[0] in ['2', '3', '4', '5','6', '8', '9']:
            should_split = True
        else: 
            should_split = False

    if should_split: 
        player.split(1, deck, dealer)


    # for case where there are multiple hands 
    for i in range(len(player.hands)):
        hand_vals = player.get_hand_values(i+1)
        hand_total = player.sum_player_hand(i+1)

        # hard hands
        if 'Ace' not in hand_vals:
            if hand_total >= 17: 
                player.stand(i+1)
            elif hand_total in [13, 14, 15, 16]:
                if dlr_upcard[0] in ['2', '3', '4', '5', '6']:
                    player.stand(i+1)
                else: 
                    player.hit(i+1, deck, dealer)
            elif hand_total == 12: 
                if dlr_upcard[0] in ['4', '5', '6']:
                    player.stand(i+1)
                else: 
                    player.hit(i+1, deck, dealer)
            else:
                player.hit(i+1, deck, dealer)

        # soft hands 
        else: 
            if hand_total >= 19: 
                player.stand(i+1)
            elif hand_total in [18]:
                if dlr_upcard[0] in ['2', '3', '4', '5', '6', '7', '8']:
                    player.stand(i+1)
                else:
                    player.hit(i+1, deck, dealer)
            else: 
                player.hit(i+1, deck, dealer) 

        hand_total = player.sum_player_hand(i+1)

        # ensures hand is greater than 11
        if hand_total <= 11: 
            player.hit(i+1, deck, dealer)
        elif hand_total >= 17: 
            player.stand(i+1)
        elif dlr_upcard[0] in ['4', '5', '6'] and hand_total == 12:
            player.stand(i+1)
        elif hand_total > 12 and hand_total <= 16: 
            if dlr_upcard[0] in ['2', '3', '4', '5', '6'] and hand_total != 12:
                player.stand(i+1)
        else: 
            player.hit(i+1, deck, dealer)
    
    # this last block checks the bet, clears player and dealer hands
    player.check_bet(dealer)
    player.new_hand()
    dealer.reset()
