# Blackjack-Optimizer

This is a project that assists BlackJack players by allowing custom simulations to test and implement certain strategies using a Blackjack simulation I created. 

## Important Aspects: 

1.  a testing platform that allows users to modify and test their strategy

    - Users can backtest their strategy by using the simulate_game.py script to test their strategy and see it visualized on a plot, which gets created from a database.
    - Users can see information about each hand that is played as well as general statistics regarding a simulation. 

2.  a real game simulation 

    - This is a stand alone part of the project that just tests certain player methods to ensure it works; it doubles as a fully functional blackjack game you can play in the command line.
    - Open up a terminal and type in 'python real_game_simulation.py' to run the simulation. 

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

Steps to testing your strategy
1. write your strategy in the file strategies.py located in the strategies folder 
2. execute your strategy in simulate_game.py by navigating to the line 'simulate_your_strategy(1000, "custom_strategy", 1000, 100)'
3. customize the parameters 
4. go to command line and type python simulate_game.py to run the script 
5. view strategy's database and plot in data and data/plot folder

## Potential Future Improvements: 
1. adding ability to double down 
2. adding ability to surrender
3. implementing option for dealer hitting on soft 17
4. more statistics 
5. adding a GUI
6. Implementation of state variables and classes 

## Reflections: 

There definitely could be more improvements with writing the dealer and player classes as there were a lot of overlaps that could have been avoided if the Dealer Class was made a subclass of the player. A Hand Class could have also been implemented to simplify some of the code, and there could have been better organization between the interactions between the Dealer and Player classes. State classes could have been used to deal with logic regarding hitting, standing, and splitting. In addition, state classes could make it easier to add on more logic later on in the project, such as doubling down or surrendering. 
