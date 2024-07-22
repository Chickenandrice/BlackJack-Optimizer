import sqlite3
import cards
from dealer import Dealer
from dealer import compare_hands
from hand import Hand
import os
#helper method for executing sql commmands
def sql_command(sql, db, val = None):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    if val: 
        cursor.execute(sql, val)
    else:
        cursor.execute(sql)
    connection.commit()
        
# holds the stats for a particular simulation 
class Player:
    # wlp stands for win loss push 
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        self.entry = 0
        self.hands = [[]] 
        self.wlp = "N/A" 

        directory = os.path.join('..', 'data')
        os.makedirs(directory, exist_ok=True)
        self.db_path = os.path.join(directory, self.name + ".db") # name of player is the name of the database

        sql_command(f'CREATE TABLE IF NOT EXISTS {self.name} (balance INTEGER, entry INTEGER, WLP TEXT)', self.db_path)
        sql_command(f'INSERT INTO {self.name} (balance, entry, WLP) VALUES (?, ?, ?)', self.db_path, (self.balance, self.entry, self.wlp)) 
        sqlite3.connect(self.db_path).close()

    def add(self, amount):
        self.balance += amount
    
    def get_balance(self):
        return self.balance 
        
    def split(self, hand_num): 
        if self.hands[hand_num].pair(): 
            self.hands.append(self.hands[0].remove(self.hands[hand_num][1]))

    def stand(): 
        pass

        # problem referencing index that hasnt been instantiated 
    
    def hit(self, hand_num, deck, dealer):
        if hand_num > 1: 
            self.hands.append([]) 
        if hand_num >= 1 and hand_num <= len(self.hands): 
            self.hands[hand_num - 1].append(dealer.deal_player(deck))
        else:
            print("invalid index") 

    def get_hand(self):
        return self.hands
    
    def new_hand(self):
        self.hands = []
    
    def final_bet(self, amount, num_hands, dealer_hand):
        
        if len(self.hands) == 0 or len(dealer_hand) == 0: 
            print("haven't dealt")

        outcome = "" 
        for i in range(num_hands): 
        
            if self.balance < amount:
                amount = -1

            if compare_hands(dealer_hand, self.hands[i][0]) == "win": 
                self.balance += amount*1.5 
                outcome = "win"
            elif compare_hands(dealer_hand, self.hands[i][0]) == "loss": 
                self.balance -= amount
                outcome = "loss"
            else:
                outcome = "push"
        
            if amount == -1: 
                outcome = "N/A"
            sql_command(f'INSERT INTO {self.name} (balance, entry, WLP) VALUES (?, ?, ?)', self.db_path, (self.balance, amount, outcome))

Plyer = Player("jim", 10000)
print(Plyer.balance)

dlr = Dealer()
hnd = cards.new_deck(6)
dlr.deal_self(hnd)
dlr.deal_self(hnd)
print(Plyer.get_hand())
Plyer.hit(1, hnd, dlr)
print(Plyer.get_hand()) 
Plyer.hit(1, hnd, dlr) 
print(dlr.get_hand())
Plyer.final_bet(213, 1, dlr.get_hand()) 