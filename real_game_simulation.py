import strategies.default as df
import strategies.strategies as st
from components.player import Player
from components.cards import new_deck
from components.dealer import Dealer

# helper method
def splits(num_hand: int, player: Player, deck: list[tuple[str,str]] , dlr: Dealer) -> None: 
    if player.get_hand_values(num_hand)[0] == player.get_hand_values(num_hand)[1]: 
        splitz = input("Do you wish to split your hand? (Y/N)")
        if splitz == "Y":
            player.split(1, deck, dlr)
            for i in range(len(player.hands)):
                print(f'Player\'s hand {i}: {player.get_hand(i)}')
            splits(num_hand, player)
            splits(num_hand+1, player)

def real_simulation():
    print("This script simulates a real game of BlackJack.")
    player_name = input("Please input a name: ")
    player_balance = input("Please input a starting balance: ") 
    Plyer = Player(player_name, int(player_balance)) 
    dlr = Dealer()
    player_wants_to_play = input("Do you wish to play a game of BlackJack? (Y/N): ")
    while player_wants_to_play != "Y" and player_wants_to_play != "N":
        player_wants_to_play = input("please input 'Y' or 'N' ")
    while player_wants_to_play == "Y": 
        deck = new_deck(6)
        bet_amount = input("Please input a starting bet_amount: ")
        Plyer.bet(int(bet_amount))
        Plyer.initial_deal(1, deck, dlr)
        hand, dlr_total = dlr.deal_self(deck)

        print(f'Dealer\'s hand: [{dlr.upcard()}, (hidden, hidden)]')
        print(f'Player\'s hand 1: {Plyer.get_hand(1)}')
        splits(1, Plyer, deck, dlr)

        player_hit = input("Do you wish to hit? (Y/N): ")
        while player_hit != "Y" and player_hit != "N":
            player_hit = input("please input 'Y' or 'N' ")

        while player_hit == "Y":
            hit_hand = 1
            if len(Plyer.hands) > 1: 
                hit_hand = input("Which hand would you like to hit? (number): ")
            Plyer.hit(int(hit_hand), deck, dlr) 
            for i in range(len(Plyer.hands)):
                print(f'Player\'s hand {i+1}: {Plyer.get_hand(i+1)}')
                if Plyer.sum_player_hand(i) > 21: 
                    player_hit = "N"
                    print("Player hand busts, the player lost game")
                else:
                    player_hit = input("Do you still wish to hit? (Y/N): ")
            while player_hit != "Y" and player_hit != "N":
                player_hit = input("please input 'Y' or 'N'")
        Plyer.check_bet(int(dlr_total))
    
        for i in Plyer.prev_hands[len(Plyer.prev_hands)-len(Plyer.hands):]: 
            if i == "win":
                print(f'you won one hand worth, balance is now ${Plyer.balance}')
            elif i == "loss":
                print(f'you loss one hand, balance is now ${Plyer.balance}')
            else:
                print(f'push, nothing loss and nothing gained, balance is now ${Plyer.balance}') 

        player_wants_to_play = input("Do you still wish to play? (Y/N): ")
    
    
real_simulation()