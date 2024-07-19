import sqlite3

class Player: 
    def __init__(self) -> None:
        pass

connection = sqlite3.connect("players.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS players (name TEXT, balance INTEGER, Win/Loss TEXT)")