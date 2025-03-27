import csv

def conversion():
    with open("coin_change/currencies.csv", "r") as csv_file:
        file = csv.reader(csv_file)
        
        US = next(file)
        
        BR = next(file)

        NK = next(file)

        UK = next(file)

        Robux = next(file)

        country = input("Which country's currency would you like to use?:\n\n1. United States Dollar\n2. Brazil Reais\n3. North Korean Won\n4. British Pound\n5. Roblox Robux\n\n(1-5): ")
        


conversion()