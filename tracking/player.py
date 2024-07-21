import sqlite3
import dealing_cards.dealer as Dealer
#helper method for executing sql commmands
def sql_command(sql, db, val = None):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    if val: 
        cursor.execute(sql, val)
    else: 
        cursor.execute(sql)
    connection.commit()

class Hand: 
    def __init__(self):
        self.hand = []
    def draw_card(self, card): 
        self.hand.append(card) 

        
# holds the stats for a particular simulation 
class Player: 
    # wlp stands for win loss push 
    def __init__(self, name, balance, entry, wlp):
        self.name = name 
        self.balance = balance 
        self.entry = entry
        self.hand = [Hand()]
        self.wlp = wlp


    def add(self, amount):
        self.balance += amount

    def start_player_db(self):
        db = self.name + ".db"

        sql_command(f'CREATE TABLE IF NOT EXISTS {self.name} (balance INTEGER, entry INTEGER, WLP TEXT)', db)
        sql_command(f'INSERT INTO {self.name} (balance, entry, WLP) VALUES (?, ?, ?)', db, (self.balance, "0", 'N/A')) 
        sqlite3.connect(db).close()
    
    def split(): 
        pass

    def stand(): 
        pass
    def hit(self): 
        self.hand.append(Dealer.deal_card())

    def insurance(): 
        if Dealer.hand:
            pass
    
    def final_bet(self, amount, insurance=None): 
        db = self.name + ".db"
        outcome = ""
        if self.balance < amount:
            amount = -1
        if Dealer.compare_hands(self.hand) == "win": 
            self.balance += amount*1.5 
            outcome = "win"
        elif Dealer.compare_hands(self.hand) == "loss": 
            self.balance -= amount
            outcome = "loss"
        else: 
            outcome = "push"
        
        if amount == -1: 
            outcome = "N/A"
        sql_command(f'INSERT INTO {self.name} (balance, entry, WLP) VALUES (?, ?, ?)', db, (self.balance, amount, outcome))

Plyer = Player("jim", 10000, 0)
Plyer.bet(10000000)
Plyer.add(1024243)
Plyer.start_player_db()
print(Plyer.balance)