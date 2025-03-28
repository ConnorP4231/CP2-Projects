import csv

def conversion():
    with open("coin_change/currencies.csv", "r") as csv_file:
        file = csv.reader(csv_file)
        next(file)
        
        US = next(file)
        
        BR = next(file)

        NK = next(file)

        UK = next(file)

        Robux = next(file)

        country = input("Which country's currency would you like to use?:\n\n1. United States Dollar\n2. Brazil Reais\n3. North Korean Won\n4. British Pound\n5. Roblox Robux\n\n(1-5): ")

        def US_conversion():
            money_amnt = []
            for line in US:
                num = line.split()[-1]
                money_amnt.append(num)
                print(line)
            
            money = ('How much money would you like to check?: ')
            try:
                rounded_money = round(float(money), 2)
                print(rounded_money)
            except ValueError:
                print('Incorrect input, sigma.')

            print(money)

        US_conversion()


conversion()