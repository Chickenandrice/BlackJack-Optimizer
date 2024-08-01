import matplotlib.pyplot as plt
import sqlite3
import os
from components.player import Player

def plot_trial_balance(player: Player) -> None:
    """
    Plots data from a simulation's database. 

    Parameters: 

    trial_name (str): the name of the simulation
    player (Player): player object that is used to get information, such as number of wins, losses, etc. 

    """
    db = player.name + ".db"
    directory = os.path.join('data')
    db_path = os.path.join(directory, db)
    if os.path.exists(db_path):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute(f'SELECT Balance FROM {player.name}')

        balance = [row[0] for row in cursor.fetchall()]
        games = list(range(len(balance)))
        connection.close()

        fig, ax = plt.subplots()
        ax.plot(games, balance)
        ax.set(xlabel='Games', ylabel='Player Balance',
            title=f'Player Balance Over {len(games)-1} Games')
        
        num_splits = player.splits 
        win = 0
        loss = 0
        push = 0
        for outcome in player.previous_hands():
            if outcome == "win":
                win += 1
            if outcome == "loss":
                loss += 1
            if outcome == "push":
                push += 1
        
        fig.text(0.03, 0.97, f'splits: {num_splits} ({round(num_splits/(len(balance)-1), 3)} %)', fontsize= 9, color = 'black')
        fig.text(0.03, 0.945, f'wins: {win} ({round(win/(len(balance)-1) * 100, 3)} %)', fontsize= 9, color = 'black') 
        fig.text(0.03, 0.92, f'losses: {loss} ({round(loss/(len(balance)-1) * 100, 3)} %)', fontsize= 9, color = 'black')
        fig.text(0.03, 0.895, f'pushes: {push} ({round(push/(len(balance)-1) * 100, 3)} %)', fontsize= 9, color = 'black')
    
        ax.grid(True)
        output_directory = 'data/plots'
        os.makedirs(output_directory, exist_ok=True)
        plot_path = os.path.join(output_directory, player.name + ".png")
        fig.savefig(plot_path) 
        plt.show()

    

    