import csv

def create_character():
    with open(r"battle_simulator\characters.csv", "a") as file:
        name = input('What is the name of your character?: ')
        
        while True:
            try:
                health = int(input('What is your character\'s health? (1-100): '))
                if 1 <= health <= 100:
                    break
                else:
                    print("Health must be between 1 and 100.")
            except ValueError:
                print("Please enter a valid number for health.")
        
        while True:
            try:
                strength = int(input('What is the strength of your character? (1-100): '))
                if 1 <= strength <= 100:
                    break
                else:
                    print("Strength must be between 1 and 100.")
            except ValueError:
                print("Please enter a valid number for strength.")
        
        while True:
            try:
                defense = int(input('What is the defense of your character? (1-100): '))
                if 1 <= defense <= 100:
                    break
                else:
                    print("Defense must be between 1 and 100.")
            except ValueError:
                print("Please enter a valid number for defense.")
        
        while True:
            try:
                speed = int(input('What is the speed of your character? (1-100): '))
                if 1 <= speed <= 100:
                    break
                else:
                    print("Speed must be between 1 and 100.")
            except ValueError:
                print("Please enter a valid number for speed.")
        
        # Write character data to file
        file.write(f'\n{name},{health},{strength},{defense},{speed}')