import csv

with open("coin_change/currencies.csv", "r") as csv_file:
    file = csv.reader(csv_file)
    next(file)
    for index, line in enumerate(file):
        print(f'{index+1}: {line}')