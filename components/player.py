import sqlite3
from components.dealer import Dealer
import components.hand as hand
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
    def __init__(self, name, balance, entry, wlp):
        self.name = name 
        self.balance = balance 
        self.entry = entry
        self.hands = [hand.Hand()]
        self.wlp = wlp

        db = self.name + ".db"
        sql_command(f'CREATE TABLE IF NOT EXISTS {self.name} (balance INTEGER, entry INTEGER, WLP TEXT)', db)
        sql_command(f'INSERT INTO {self.name} (balance, entry, WLP) VALUES (?, ?, ?)', db, (self.balance, "0", 'N/A')) 
        sqlite3.connect(db).close()

    def add(self, amount):
        self.balance += amount
        
    def split(self, hand_num): 
        if self.hands[hand_num].pair(): 
            self.hands.append(self.hands[0].remove(self.hands[hand_num][1]))

    def stand(): 
        pass

    def hit(self, hand_num): 
        if hand_num >= 0 and hand_num < len(self.hands):
            self.hands[hand_num].draw_card()
        else:
            print("invalid index")
    
    def new_hand(self):
        self.hands = []
    
    def final_bet(self, amount, num_hands):
        db = self.name + ".db"
        outcome = ""
        for i in range(num_hands): 
        
            if self.balance < amount:
                amount = -1

            if Dealer.compare_hands(self.hands[i]) == "win": 
                self.balance += amount*1.5 
                outcome = "win"
            elif Dealer.compare_hands(self.hands[i]) == "loss": 
                self.balance -= amount
                outcome = "loss"
            else: 
                outcome = "push"
        
            if amount == -1: 
                outcome = "N/A"
            sql_command(f'INSERT INTO {self.name} (balance, entry, WLP) VALUES (?, ?, ?)', db, (self.balance, amount, outcome))

Plyer = Player("jim", 10000, 0)
print(Plyer.balance)