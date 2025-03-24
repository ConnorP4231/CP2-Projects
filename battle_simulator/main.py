# Connor Pavicic, battle_simulator
from create_character import create_character #Importing all the functions
from display_csv import display_csv
from choose_character import choose_character
from battle import battle
from bar_graph import bar_graph
from battle import line_graph

def main(): # Main function
    with open("battle_simulator/points.txt", "w") as file: # Resets the points
        file.write('0')
    print('This is a battle simulator.')
    
    battles = 0
    battles_values = []
    xp_values = []
    
    while True:
        choice = input('Which one would you like to do?: \n\n1. Battle the computer\n2. Create a character\n3. Display the characters\n4. Look at a character\'s bar graph\n5. Look at your XP line graph\n6. Exit the program\n\n(1-6): ')
        if choice == '1':
            choose_character()  # Choose a character for the battle
            # Pass the variables and get the updated ones from the battle
            battles, xp_values, battles_values = battle(battles, xp_values, battles_values)
            battles += 1  # Increment the battle count
        elif choice == '2':
            create_character()
        elif choice == '3':
            for row in display_csv():
                print(row)
        elif choice == '4':
            bar_graph()
        elif choice == '5':
            line_graph(battles_values, xp_values)
        elif choice == '6':
            print('Thanks for using the program.')
            break
        else:
            print('\nIncorrect option, try again.')

if __name__ == "__main__":  # Makes sure this is the correct file.
    main()
