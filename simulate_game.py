import strategies.default as df
import strategies.strategies as st
from components.player import Player
from components.dealer import Dealer
from plot_data import plot_trial_balance


def simulate_default_trials(number_trials: int, player_name: str, player_balance: int, bet_amount: int):
    """ 
    This method simulates a basic default strategy over many different trials, creates a database, and plots the results 

    Parameters: 

    number_trials (int): the number of individual games that will be simulated at one time. 
    player_name (str): the name of the simulation 
    player_balance (int): the starting balance of the simulation 
    bet_amount (int): the starting bet amount, which will remain constant unless a strategy requires it to change 

    """
    # sets up dealer 
    dlr = Dealer()
    
    # sets up player 
    player = Player(player_name, player_balance) 

    i = 1
    while number_trials > 0: 
        print(f'\nsimulation # {i}')
        df.simulate_default(player, dlr, bet_amount)
        number_trials -= 1
        i += 1
    
    # this line plots the data 
    plot_trial_balance(player)


def simulate_your_strategy(number_trials, player_name, player_balance, bet_amount):
    """ 
    This method simulates a basic default strategy over many different trials, creates a database, and plots the results 

    Parameters: 

    number_trials (int): the number of individual games that will be simulated at one time. 
    player_name (str): the name of the simulation 
    player_balance (int): the starting balance of the simulation 
    bet_amount (int): the starting bet amount, which will remain constant unless a strategy requires it to change 

    """
    # sets up dealer 
    dlr = Dealer()
    
    # sets up player 
    player = Player(player_name, player_balance) 

    i = 1
    while number_trials > 0: 
        print(f'\nsimulation # {i}')
        st.simulate_your_strategy(player, dlr, bet_amount) # THIS IS WHERE YOUR STRATEGY IS IMPLEMENTED**
        number_trials -= 1
        i += 1
    
    # this line plots the data 
    plot_trial_balance(player) 




# sample simulation run
simulate_default_trials(1000, "example", 10000, 100)

# RUNNING YOUR STRATEGY**
#simulate_your_strategy(1000, "custom_strategy", 1000, 100)
