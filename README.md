# Blackjack-Optimizer

This is a project that assists BlackJack players by allowing custom simulations to test and implement certain strategies using a Blackjack simulation I created. 

## Important Aspects: 

1.  a testing platform that allows users to modify and test their strategy

    - Users can backtest their strategy by using the simulate_game.py script to test their strategy and see it visualized on a plot, which gets created from a database.
    - Users can see information about each hand that is played as well as overall statistics regarding a simulation. 

2.  a real game simulation 

    - This is a stand alone part of the project that just tests certain player methods to ensure it works; it doubles as a fully functional blackjack game you can play in the command line.


## General Assumptions:   

1. 3 to 2 payout odds 

2. 6-8 deck games  
    
3. player starting balance of $100,000

4. insurance bets are not counted or recorded

5. dealer hits under 17, and dealer stands 17 and above 

6. Player does not explictedly chose the value of an Ace, the most advantage value will be selected for based on the current hand of a player

7. Doubling Down and Surrendering are not included in the simulation

8. dealer doesn't hit on soft 17

## Testing Strategies: 



## Potential Future Improvements: 
1. adding ability to double down 
2. adding ability to surrender
3. implementing option for dealer hitting on soft 17
4. more statistics 
5. adding a gui 



