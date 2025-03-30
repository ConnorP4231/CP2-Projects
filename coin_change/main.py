from conversion import conversion
from display_csv import display_csv

def main():
    print('This is a program that can tell you the least amount of bills/coins needed for a certain amount of a certain currency, and it also tells you those bills/coins.')
        
    while True:
        choice = input('\nWhich one would you like to do?:\n\n 1. Find the lowest amount of coins/bills of a certain amount of a certain currency. \n2. Look at the currency csv file.\n3. Exit the program. \n\n(1, 2, or 3): ')

        if choice == '1':
            conversion()
        elif choice == '2':
            display_csv()
        elif choice == '3':
            print('Thanks for using this program.')
            break
        else:
            print('Incorrect option, try again.')