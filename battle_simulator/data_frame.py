import csv
import pandas as pd

def data_frame(): #Data frame function
    with open('battle_simulator/characters.csv', 'r') as csvfile:
        file = csv.reader(csvfile)
        next(file) #Skips the first line
        
        names = [] #Creates lists for all the things about the character
        health = []
        strength = []
        defense = []
        speed = []

        for row in file: #In each row it takes all its stats and removes the beginning of each thing like Name - , etc.
            names.append(row[0].replace('Name - ', '').strip())
            health.append(int(row[1].replace('Health: ', '').strip()))
            strength.append(int(row[2].replace('Strength: ', '').strip()))
            defense.append(int(row[3].replace('Defense: ', '').strip()))
            speed.append(int(row[4].replace('Speed: ', '').strip()))

        #Storing all the data in a dictionary
        data = {
            'Name': names,
            'Health': health,
            'Strength': strength,
            'Defense': defense,
            'Speed': speed
        }

        dataframe = pd.DataFrame(data, index=range(1, len(names)+1)) #this is the actual data frame with pandas, also displaying each number as 1 and up.
        print(dataframe)