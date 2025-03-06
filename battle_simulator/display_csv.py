import csv

def display_csv():
    with open("battle_simulator\\characters.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            print(", ".join(line))