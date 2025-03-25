import csv
import random

def save_battle_data(user_character, computer_choice):
    #Saves the selected characters and their stats to a battle_data.csv file.
    with open("battle_simulator/battle_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Character", "Name", "Health", "Strength", "Defense", "Speed"])

        # Write user character data
        writer.writerow([user_character[0], user_character[1], user_character[2], user_character[3], user_character[4]])

        # Write computer character data
        writer.writerow([computer_choice[0], computer_choice[1], computer_choice[2], computer_choice[3], computer_choice[4]])

    print("\nCharacter data saved to battle_data.csv")

def choose_character():
    #Allows the user to choose a character based on its number from a numbered list, and allows the computer to pick one randomly.
    file_path = "battle_simulator/characters.csv"

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        characters = [row for row in reader if row]  # Skip empty lines

        # Extract character names (skip header), removing "Name - " prefix from the name
        character_names = [row[0].replace("Name - ", "").strip() for row in characters[1:]]

        # Display available characters in a numbered list
        print("\nAvailable Characters:")
        for idx, name in enumerate(character_names, start=1):
            print(f"{idx}. {name}")

        # Ask user to choose a character by number
        while True:
            try:
                chosen_number = int(input("\nEnter the number of the character you want to choose: ").strip())
                
                if 1 <= chosen_number <= len(character_names):
                    # Fetch the chosen character's data
                    row = characters[chosen_number]
                    print(f"\nYou selected {row[0]}!")
                    print(f"Stats - Health: {row[1]}, Strength: {row[2]}, Defense: {row[3]}, Speed: {row[4]}")
                    user_character = row
                    break  # Exit the loop after user selects their character
                else:
                    print("Please enter a valid number corresponding to a character.")
            
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Computer randomly selects a character after user selection
        computer_choice = random.choice(characters[1:])  # Exclude the header row
        print("\nThe computer selected:")
        print(f"{computer_choice[0]}")
        print(f"Stats - Health: {computer_choice[1]}, Strength: {computer_choice[2]}, Defense: {computer_choice[3]}, Speed: {computer_choice[4]}")

        # Save user and computer selections to a CSV file
        save_battle_data(user_character, computer_choice)

        return user_character, computer_choice