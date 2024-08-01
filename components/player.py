import sqlite3
from components.dealer import Dealer
import os
def sql_command(sql, db, val = None) -> None:
    """
    Executes sql commands

    Parameters: 
    
    sql (str): an sql command that is represented by a string 

    db (str): the name of a database's path 

    val (tuple): a tuple that holds all values that are used in specific sql commands, such as INSERT

    """

    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    if val: 
        cursor.execute(sql, val)
    else:
        cursor.execute(sql)
    connection.commit()
        
# holds the stats for a particular simulation 
class Player:
    """
    This is a class that represents a BlackJack player. 

    Attributes: 
        name (str): the name of the simulation/player
        balance (int): the starting balance of the simulation/player
        hands (list[list[tuple[str,str]]]): the hand(s) of the player per run of the simulation (multiple hands in case of split)
        prev_hands (list[str]): a list of strings that represent the outcomes of each game as 'win', 'loss', or 'push'
        curr_bet (int): the value of the player's current bet 
        can_move (list[bool]): checks if a player can make a move in a game, which could be false where a player chooses to stand 
        splits (int): holds the number of splits that occurs in a simulation. 
    
    Methods: 
        add(self, amount: int): 
            adds a inputted amount to the balance of the player/simulation
        get_balance(self): 
            returns the current balance of the player 
        split(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer, card_value: list = None):
            splits the hand of the player if applicable, splits into two list[tuple[str,str]] objects
        stand(self, hand_num: int):
            sets can_move[hand_num] to false, so more moves can't be made because the player hit 
        initial_deal(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer): 
            deals two cards to the player
        hit(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer):
            deals a card to the player 
        get_hand(self, hand_num): 
            returns a player hand specified by the hand_num param 
        get_hand_values(self, hand_num):
            returns a list of the player's hand values specified by the hand_num param
        new_hand(self):
            resets a player's hand by setting it to an empty list, sets can_move to [True], and closes the simulation database
        previous_hands(self):
            returns all previous hand results, which is used in plotting data 
        sum_player_hand(self, num_hand: int): 
            returns the sum of a player's hand values, the hand is specified by the hand_num param
        compare_hands(self, dealer_total: int, player_total: int):
            helper method that compares the dealer hand's total and the player's hand total and returns a str that represents an outcome ('win', 'loss', 'push')
        bet(self, amount: int):
            sets the curr_bet to the amount specified in the parameter
        check_bet(self, dealer: Dealer):
            checks each bet that was made by the player and sends this information to a database that was created in the init() method of this class 
    """
    def __init__(self, name: str, balance: int) -> None:
        """
            This is the constructor method for Player class that also creates a database and sql command that creates a Table in the database, which holds information regarding a 
            player's balance, current bet, game outcome, dealer's hand during the game, dealer's total, player's hand(s) during the game, and player's total. The second sql command
            inserts the first entry in the database, which has the player's starting balance. 

            Parameters: 

            name (str): name of the player/simulation 
            balance (int): the starting balance of the player/simulation
        """
        self.name = name 
        self.balance = balance 
        self.hands = [[]]
        self.prev_hands = []
        self.curr_bet = 0 
        self.can_move = [True]
        self.splits = 0

        directory = os.path.join('data')
        os.makedirs(directory, exist_ok=True)
        self.db_path = os.path.join(directory, self.name + ".db") # name of player is the name of the database

        sql_command(f'CREATE TABLE IF NOT EXISTS {self.name} (balance INTEGER, entry INTEGER, WLP TEXT, Dealer_Hand TEXT, Dealer_Total TEXT, Player_Hand TEXT, Player_Total TEXT)', 
                    self.db_path)
        sql_command(f'INSERT INTO {self.name} (balance, entry, WLP, Dealer_Hand, Dealer_Total, Player_Hand, Player_Total) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                    self.db_path, (self.balance, self.curr_bet, "None", "None", "None", "None", "None"))
        sqlite3.connect(self.db_path).close()

    def add(self, amount: int) -> None:
        """ 
        This method adds to the balance of a player.

        Parameters: 

        amount (int): amount of simulation money being added to a player's balance

        """
        self.balance += amount
    
    def get_balance(self) -> int:
        """ 
        This method returns the current balance of a player 
        
        Returns: 

        int: which is the current balance of the player
        
        """
        return self.balance 
        
    def split(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer, card_value: list = None) -> None: 
        """ 
        This method represents a split in BlackJack. 

        Parameters: 

        hand_num (int): the number of the hand in a player's game that needs to be split.
        deck (list[tuple[str, str]]): values in the list are used to deal an additional card to each hand that was split, so the hands both have 2 cards
        dealer (Dealer): Dealer object that is used to deal a player a card if the hand was split 
        card_value (list): optional list of card values that should be taken in consideration if a hand should be split. For example, if card_value = [3, 2], all 3 and 2 pairs should be split
        """
        if len(self.hands[hand_num-1]) == 2:
            card_1 = self.hands[hand_num-1][0]
            card_2 = self.hands[hand_num-1][1]
            card_value = card_value or [card_1]
            

            if len(self.hands[hand_num-1]) == 2 and (card_1 == card_2) and card_2 in card_value: 
                self.splits += 1
                self.hands.append([])
                self.can_move.append(True)
                self.hands[hand_num-1].remove(card_2)
                self.hands[len(self.hands)-1].append(card_2)

                print("a split was done")

                self.hit(hand_num, deck, dealer) 
                
                self.hit(len(self.hands), deck, dealer)

                if len(self.hands) > hand_num: 
                    self.split(hand_num, deck, dealer, card_value) or self.split(hand_num+1, deck, dealer, card_value)

        
    def stand(self, hand_num: int) -> None:
        """
        This method represents a stand.
        
        Parameters: 
        
        hand_num (int): the number of the hand in a player's game, that the player wants to stand on. 
        """
        self.can_move[hand_num - 1] = False


    def initial_deal(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer) -> None:
        """
        This method deals the player's initial cards using a dealer method.

        Parameters: 

        hand_num (int): the number of the hand in a player's game
        deck (list[tuple[str,str]]): deck used to deal cards 
        dealer (Dealer): Dealer object that deals cards (tuple[str,str]) from the deck (list[tuple[str,str]])

        """
        i = 0

        while i in range(2):
            card = dealer.deal_card(deck)
            self.hands[hand_num - 1].append(card)
            i += 1

    def hit(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer) -> None:
        """
        This method deals cards to a player's hand(s)

        Parameters: 

        hand_num (int): the number of a hand in a player's game 
        deck (list[tuple[str,str]]): deck used to deal cards 
        dealer (Dealer): Dealer object that deals cards (tuple[str,str]) from the deck (list[tuple[str,str]])
        """
        if self.can_move[hand_num - 1] == True:
            if self.sum_player_hand(hand_num) <= 21: 
                if hand_num >= 1:
                    card = dealer.deal_card(deck)
                    self.hands[hand_num - 1].append(card) 
                else:
                    print("invalid index")
        else: 
            print("Player has chosen to stand, so player can't hit.")

    def get_hand(self, hand_num: int) -> list[tuple[str, str]]:
        """ 
        Gets a player's hand at a specifc index 

        Parameter: 

        hand_num (int): the index in question 
        
        Return:

        list[tuple[str, str]]: a list of tuples for a Player object's current hand of cards in the format 
        """
        if self.hands[hand_num-1] == [[]]: 
            return "None"
        return self.hands[hand_num-1]
    
    def get_hand_values(self, hand_num: int) -> list[str]:
        """
        Gets the hand values of a player's hand in a list 

        Parameters: 

        hand_num (int): the hand number of a player's hand(s)

        Return: 

        list[str]: a list of strings that represent card values ('6', '10', 'Jack', etc)
        """
        vals = []
        for value in self.hands[hand_num - 1]: 
            vals.append(value[0]) 
        return vals
    
    def new_hand(self) -> None:
        """ resets a Player object's current hand by setting self.hands to an empty list with an empty list """
        self.hands = [[]]
        self.can_move = [True]
        sqlite3.connect(self.db_path).close()
    
    def previous_hands(self) -> list[str]:
        """
        This method returns a list of strings, which show if a previous had was a loss, push, or win, which is used in strategies 

        Returns: 

        list[str]: a list of outcomes ('win', 'loss', 'push') from previous games
        """
        return self.prev_hands
    
    def sum_player_hand(self, num_hand: int) -> int:
        """
        This is a private helper method that adds a hand's card value, which is represented by the first string in the list of tuples. 

        Parameters: 

        num_hand (int): hand number

        Returns: 

        int: the total value of a player's hand 
        """
        total = 0
        aces = 0
        for card in self.hands[num_hand - 1]:
            if card[0] in ["Jack", "Queen", "King"]: 
                total += 10

            elif card[0] == "Ace":
                total += 11
                aces += 1
            else:
                total += int(card[0])

        while aces > 0 and total > 21: 
            total -= 10 
            aces -= 1 

        return total

    def compare_hands(self, dealer_total: int, player_total: int) -> None:
        """
        This is a private helper method that compares a player's hand and the total value of a dealer's hand to determine outcome of a BlackJack game. 

        Parameters: 

        dealer_total (int): the total value of a dealer's hand

        player_hand (list[tuple[str, str]]): list of tuples, which represent a card's value and suit

        Returns: 

        str: this method returns loss, win, or push based on if player_hand total is smaller, the same, or larger than the dealer_total
        """ 
        if player_total > 21: 
            return "loss"
        
        elif player_total == 21: 
            if dealer_total == player_total: 
                return "push"
            if dealer_total > 21: 
                return "win"
        else: 
            if dealer_total > 21 and player_total <= 21: 
                return "win"
            
            if dealer_total > player_total:
                return "loss"
            elif dealer_total == player_total:
                return "push"
            else: 
                return "win"
    
    def bet(self, amount: int) -> None: 
        """
        This method sets a player's current bet. 

        Parameters: 

        amount (int): amount of the current bet. 
        """
        self.curr_bet = amount
        
    def check_bet(self, dealer: Dealer) -> None:
        """
        This method checks each bet that was made by the player and inserts an entry to the simulation database that reveals the player's balance after the game, 
        current bet, outcome, dealer hand, dealer total, player hand, player total. 

        Parameter: 

        dealer (Dealer): Dealer object that is used to compare the dealer total and player total to get an outcome. The dealer hand and total is also inserted into the database.
        """
        dealer_total = dealer.total

        if len(self.hands) == 0 or dealer_total == 0:
            print("dealer hasn't dealt")

        print("player cards:")
        for hand in self.hands: 
            print(hand)

        outcome = ""
        bet = self.curr_bet

        for i in range(len(self.hands)):
            player_total = self.sum_player_hand(i+1)
            
            if self.balance < self.curr_bet:
                print("insufficient funds")
                quit()
            if self.compare_hands(dealer_total, player_total) == "win": 
                self.balance += self.curr_bet*1.5 
                outcome = "win"
                self.curr_bet = 0
            elif self.compare_hands(dealer_total, player_total) == "loss":
                self.balance -= self.curr_bet
                outcome = "loss"
                self.curr_bet = 0
            else:
                outcome = "push"
                self.curr_bet = 0
            self.prev_hands.append(outcome)
            sql_command(f'INSERT INTO {self.name} (balance, entry, WLP, Dealer_Hand, Dealer_Total, Player_Hand, Player_Total) VALUES (?, ?, ?, ?, ?, ?, ?)',
                        self.db_path, (self.balance, bet, self.prev_hands[len(self.prev_hands)-1], str(dealer.dealer_hand_values()), dealer_total,
                                        str(self.get_hand_values(i+1)), player_total))