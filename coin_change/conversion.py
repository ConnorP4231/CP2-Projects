import csv

def conversion():
    try:
        with open("coin_change/currencies.csv", "r") as csv_file:
            file = csv.reader(csv_file)
            next(file)  # Skip the header
            US = next(file) #The next line is a certain country
            BR = next(file)
            NK = next(file)
            UK = next(file)
            Robux = next(file)
    except FileNotFoundError: #Makes sure the file exists.
        print('File not found.')  
        return

    country = input("\nWhich country's currency would you like to use?\n\n1. United States Dollar\n2. Brazil Reais\n3. North Korean Won\n4. British Pound\n5. Roblox Robux\n\n(1-5): ") #Asks which country.

    def process_currency(currency_row):
        # Remove the first column (Country Name)
        currency_row = currency_row[1:]

        # Split into currency type and value (value is after the dash)
        money_types = []
        for item in currency_row:
            name, value = item.split(' - ') #Name and value are the things that this splits it into.
            money_types.append((name.strip(), float(value.strip()))) #Adds a tuple to money types list.

        return money_types

    def US_conversion(US): #US function
        money_amnt = process_currency(US) #Uses the process_currency helper function to do everything with US.
        
        try:
            money = float(input('How much money would you like to check?: '))
            if money == 0 or money < 0: #Makes sure money isnt negative or 0
                print("I can't do anything with this amount.")
            else:
                rounded_money = '{:.2f}'.format(money) #Rounds it to 2 decimal places.
                print(f"Converted amount: {rounded_money}")
        except ValueError: #Makes sure the user doesn't input text or anything like that.
            print('Incorrect input.')
            return
        
        all_types = [] #The list that will store the bills/coins.

        for name, value in money_amnt: #Pairs the name and bill.
            while money - value >= 0: #Checks to see if the bill can be subtracted from the amount.
                all_types.append(name) #Adds the bill name to the list.
                money -= value

        print(f"Currency Breakdown:") #Prints the list
        for item in all_types:
            print(item)
        print(f'Amount of coins/bills: {len(all_types)}') #Displays how many coins/bills needed.
    
    def BR_conversion(BR): #Brazil function
        money_amnt = process_currency(BR) #Uses the process_currency helper function to do everything with BR.
        
        try:
            money = float(input('How much money would you like to check?: '))
            if money == 0 or money < 0: #Makes sure money isnt negative or 0
                print("I can't do anything with this amount.")
            else:
                rounded_money = '{:.2f}'.format(money) #Rounds it to 2 decimal places.
                print(f"Converted amount: {rounded_money}")
        except ValueError: #Makes sure the user doesnt input text or anything like that.
            print('Incorrect input.')
            return
        
        all_types = [] #The list that will store the bills/coins.

        for name, value in money_amnt: #Pairs the name and bill.
            while money - value >= 0: #Checks to see if the bill can be subtracted from the amount.
                all_types.append(name) #Adds the bill name to the list.
                money -= value

        print(f"Currency Breakdown:") #Prints the list.
        for item in all_types:
            print(item)
        print(f'Amount of coins/bills: {len(all_types)}') #Displays how many coins/bills needed.

    def NK_conversion(NK): #North Korea function.
        money_amnt = process_currency(NK) #Uses the process_currency helper function to do everything with NK.
        
        try:
            money = float(input('How much money would you like to check?: '))
            if money == 0 or money < 0: #Makes sure money isnt negative or 0.
                print("I can't do anything with this amount.")
            else:
                rounded_money = '{:.2f}'.format(money) #Rounds it to 2 decimal places.
                print(f"Converted amount: {rounded_money}")
        except ValueError: #Makes sure the user doesnt input text or anything like that.
            print('Incorrect input.')
            return
        
        all_types = [] #The list that will store the bills/coins.

        for name, value in money_amnt: #Pairs the name and bill.
            while money - value >= 0: #Checks to see if the bill can be subtracted from the amount.
                all_types.append(name) #Adds the bill name to the list.
                money -= value

        print(f"Currency Breakdown:") #Prints the list.
        for item in all_types:
            print(item)
        print(f'Amount of coins/bills: {len(all_types)}') #Displays how many coins/bills needed.
    
    def UK_conversion(UK): #United Kingdom function.
        money_amnt = process_currency(UK) #Uses the process_currency helper function to do everything with UK.
        
        try:
            money = float(input('How much money would you like to check?: '))
            if money == 0 or money < 0: #Makes sure money isnt negative or 0.
                print("I can't do anything with this amount.")
            else:
                rounded_money = '{:.2f}'.format(money) #Rounds it to 2 decimal places.
                print(f"Converted amount: {rounded_money}")
        except ValueError: #Makes sure the user doesnt input text or anything like that.
            print('Incorrect input.')
            return
        
        all_types = [] #The list that will store the bills/coins.

        for name, value in money_amnt: #Pairs the name and bill.
            while money - value >= 0: #Checks to see if the bill can be subtracted from the amount.
                all_types.append(name) #Adds the bill name to the list.
                money -= value

        print(f"Currency Breakdown:") #Prints the list.
        for item in all_types:
            print(item)
        print(f'Amount of coins/bills: {len(all_types)}') #Displays how many coins/bills needed.

    def Robux_conversion(Robux): #Roblox robux function.
        money_amnt = process_currency(Robux) #Uses the process_currency helper function to do everything with UK.
        
        try:
            money = float(input('How much money would you like to check?: '))
            if money == 0 or money < 0: #Makes sure money isnt negative or 0.
                print("I can't do anything with this amount.")
            else:
                rounded_money = '{:.2f}'.format(money) #Rounds it to 2 decimal places.
                print(f"Converted amount: {rounded_money}")
        except ValueError: #Makes sure the user doesnt input text or anything like that.
            print('Incorrect input.')
            return
        
        all_types = [] #The list that will store the bills/coins.

        for name, value in money_amnt: #Pairs the name and bill.
            while money - value >= 0: #Checks to see if the bill can be subtracted from the amount.
                all_types.append(name) #Adds the bill name to the list.
                money -= value

        print(f"Currency Breakdown:") #Prints the list.
        for item in all_types:
            print(item)
        print(f'Amount of coins/bills: {len(all_types)}') #Displays how many coins/bills needed.

    #Depending on what country the user chose, it does that country function.
    while True:
        if country == '1':
            US_conversion(US)
            break
        elif country == '2':
            BR_conversion(BR)
            break
        elif country == '3':
            NK_conversion(NK)
            break
        elif country == '4':
            UK_conversion(UK)
            break
        elif country == '5':
            Robux_conversion(Robux)
            break
        else:
            print('Incorrect option, try again.')