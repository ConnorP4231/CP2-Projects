import csv

def display_csv(): #Displays the csv file by making it a list and then in the main function using a for loop.
    with open("battle_simulator/characters.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        display_list = []
        for line in reader:
            display_list.append(f", ".join(line))

        return display_list