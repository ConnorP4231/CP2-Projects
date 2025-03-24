import csv
import pandas as pd

def data_frame():
    with open('battle_simulator/characters.csv', 'r') as csvfile:
        file = csv.reader(csvfile)
        next(file)
        
        names = []
        health = []
        strength = []
        defense = []
        speed = []

        for row in file:
            names.append(row[0].replace('Name - ', '').strip())
            health.append(int(row[1].replace('Health: ', '').strip()))
            strength.append(int(row[2].replace('Strength: ', '').strip()))
            defense.append(int(row[3].replace('Defense: ', '').strip()))
            speed.append(int(row[4].replace('Speed: ', '').strip()))

        data = {
            'Name': names,
            'Health': health,
            'Strength': strength,
            'Defense': defense,
            'Speed': speed
        }

        dataframe = pd.DataFrame(data, index=range(1, len(names)+1))
        print(dataframe)