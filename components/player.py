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


    """
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        self.hands = [[]]
        self.wlp = 0
        self.prev_hands = []
        self.curr_bet = 0 

        directory = os.path.join('data')
        os.makedirs(directory, exist_ok=True)
        self.db_path = os.path.join(directory, self.name + ".db") # name of player is the name of the database

        sql_command(f'CREATE TABLE IF NOT EXISTS {self.name} (balance INTEGER, entry INTEGER, WLP TEXT, Dealer_Total TEXT, Player_Total TEXT)', 
                    self.db_path)
        sql_command(f'INSERT INTO {self.name} (balance, entry, WLP, Dealer_Total, Player_Total) VALUES (?, ?, ?, ?, ?)', 
                    self.db_path, (self.balance, self.curr_bet, self.wlp, "None", "None"))
        sqlite3.connect(self.db_path).close()

    def add(self, amount: int) -> None:
        """ 
        This method adds to the balance of a player.

        Parameters: 

        amount (int): amount of simulation money being added to a player's balance

        """
        self.balance += amount
    
    def get_balance(self):
        """ This method returns the current balance of a player """
        return self.balance 
        
    def split(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer, card_value = None) -> bool: 
        """ 
        This method represents a split in BlackJack. 

        Parameters: 

        hand_num (int): the number of the hand in a player's game that needs to be split.
        """
        if len(self.hands[hand_num-1]) == 2:
            card_1 = self.hands[hand_num-1][0][0]
            card_2 = self.hands[hand_num-1][1][0]
            card_value = card_value or card_1
            self.hands.append([])        

            if len(self.hands[hand_num-1]) >= 2 and card_1 == card_2 == card_value: 
                self.hands[hand_num].append(self.hands[hand_num-1].remove(self.hands[hand_num-1][1]))
                print("a split was done") 
                self.hit(hand_num, deck, dealer) 
                self.hit(hand_num+1, deck, dealer) #TODO: FIX THIS METHOD !!!! 

                if len(self.hands) > hand_num: 
                    return self.split(hand_num, deck, dealer, card_value) or self.split(hand_num+1, deck, dealer, card_value)
        return False 
        
    def stand():
        pass

        # problem referencing index that hasnt been instantiated 

    def initial_deal(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer) -> None:
        i = 0
        print("player cards:")
        while i in range(2):
            card = dealer.deal_card(deck)
            self.hands[hand_num - 1].append(card)
            print(card) 
            i += 1

    def hit(self, hand_num: int, deck: list[tuple[str, str]], dealer: Dealer) -> None:
        if hand_num > 1 and len(self.hands) != hand_num:
            self.hands.append([]) 
        if hand_num >= 1:
            card = dealer.deal_card(deck)
            self.hands[hand_num - 1].append(card)
            print(card) 
        else:
            print("invalid index")

    def get_hand(self, hand_num) -> list[tuple[str, str]]:
        """ returns a list of tuples for a Player object's current hand of cards in the format list[tuple[str, str]] """
        if self.hands[hand_num] == [[]]: 
            return "None"
        return self.hands[hand_num]
    
    def get_hand_values(self, hand_num):
        vals = []
        for value in self.hands[hand_num - 1]: 
            vals.append(value[0]) 
        return str(vals)
    
    def new_hand(self) -> None:
        """ resets a Player object's current hand by setting self.hands to an empty list with an empty list """
        self.hands = [[]]
        sqlite3.connect(self.db_path).close()
    
    def previous_hands(self) -> list[str]:
        """
        This method returns a list of strings, which show if a previous had was a loss, push, or win, which is used in strategies 
        """
        return self.prev_hands
    
    def sum_player_hand(self, num_hand: int) -> int:
        """
        This is a private helper method that adds a hand's card value, which is represented by the first string in the list of tuples. 

        Parameters: 

        hand (list[tuple[str, str]]): list of tuples, which represent a card's value and suit 

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
            if dealer_total > player_total: 
                return "loss"
            elif dealer_total == player_total:
                return "push"
            else: 
                return "win"
    
    def bet(self, amount: int): 
        """
        This method sets a player's current bet. 

        Parameters: 

        amount (int): amount of the current bet. 
        """
        self.curr_bet = amount
        
    def check_bet(self, dealer_total: int) -> None:
        
        if len(self.hands) == 0 or dealer_total == 0:
            print("dealer hasn't dealt")

        outcome = ""
        for i in range(len(self.hands)):
            player_total = self.sum_player_hand(i)
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
            sql_command(f'INSERT INTO {self.name} (balance, entry, WLP, Dealer_Total, Player_Total) VALUES (?, ?, ?, ?, ?)',
                        self.db_path, (self.balance, self.curr_bet, self.prev_hands[len(self.prev_hands)-1], dealer_total, player_total))
        