import csv

try:
    with open("coin_change/currencies.csv", "r") as csv_file:
        file = csv.reader(csv_file)
        next(file) #Skip the header
        for index, line in enumerate(file):
            print(f'{index+1}: {line}')
except FileNotFoundError:
    print('File not found.')