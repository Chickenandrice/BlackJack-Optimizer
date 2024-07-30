import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import os

def plot_trial_balance(trial_name):
    db = trial_name + ".db"
    directory = os.path.join('data')
    db_path = os.path.join(directory, db)
    if os.path.exists(db_path):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute(f'SELECT Balance FROM {trial_name}')

        balance = [row[0] for row in cursor.fetchall()]
        games = list(range(len(balance)))
        connection.close()

        fig, ax = plt.subplots()
        ax.plot(games, balance)
        ax.set(xlabel='Games', ylabel='Player Balance',
            title=f'Player Balance Over {len(games)-1} Games')
    
        ax.grid(True)
        output_directory = 'data/plots'
        os.makedirs(output_directory, exist_ok=True)
        plot_path = os.path.join(output_directory, trial_name + ".png")
        fig.savefig(plot_path)
        plt.show()

    

    