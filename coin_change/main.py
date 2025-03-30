from conversion import conversion #Conversion function
from display_csv import display_csv #Display csv function.

def main(): #Main function.
    print('This is a program that can tell you the least amount of bills/coins needed for a certain amount of a certain currency, and it also tells you those bills/coins.') #Describes what the program does.
        
    while True:
        choice = input('\nWhich one would you like to do?:\n\n1. Find the lowest amount of coins/bills of a certain amount of a certain currency. \n2. Look at the currency csv file.\n3. Exit the program. \n\n(1, 2, or 3): ')

        #Does something based on the user input.
        if choice == '1':
            conversion()
        elif choice == '2':
            display_csv()
        elif choice == '3':
            print('Thanks for using this program.')
            break
        else: #Tells the user they input something wrong if they did.
            print('Incorrect option, try again.')

if __name__ == '__main__': #Runs main function.
    main()