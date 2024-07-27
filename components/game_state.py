from abc import ABC, abstractmethod

class GameState(ABC):
    @abstractmethod
    def bet(self, player, amount): 
        pass

    @abstractmethod
    def win(self, player):
        pass

    @abstractmethod
    def loss(self, player): 
        pass 

    @abstractmethod
    def push(self, player):
        pass 

class BetState(GameState):
   
    def bet(self, player, amount): 
        print("A bet is already placed.")
    
    def win(self, player):
        player.balance += player.curr_bet*1.5
        player.curr_bet = 0
        player.state = NoBetState()

    def loss(self, player): 
        player.balance -= player.curr_bet
        player.curr_bet = 0 
        player.state = NoBetState()

    def push(self, player):
        player.curr_bet = 0
        player.state = NoBetState()

class NoBetState(GameState):

    def bet(self, player, amount): 
        if player.balance < player.curr_bet: 
            print("Player's bet is larger than player's balance")
        else: 
            player.curr_bet = amount 
            player.state = BetState()

    def win(self, player):
        pass

 
    def loss(self, player): 
        pass 


    def push(self, player):
        pass 