import csv
import matplotlib.pyplot as plt

def bar_graph(): #Bar graph function
    with open("battle_simulator/characters.csv", "r", newline="") as file:
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
                        #Gets all the data to be used later
                        user_name = row[0].replace("Name - ", "").strip()
                        health = int(row[1].replace("Health: ", "").strip())
                        strength = int(row[2].replace("Strength: ", "").strip())
                        defense = int(row[3].replace("Defense: ", "").strip())
                        speed = int(row[4].replace("Speed: ", "").strip())
                        break  # Exit the loop after user selects their character
                    else:
                        print("Please enter a valid number corresponding to a character.")
                
                except ValueError:
                    print("Invalid input. Please enter a valid number.")


    categories = ['Health', 'Strength', 'Defense', 'Speed'] #Labeling 
    values = [health, strength, defense, speed]  #The actual values being used

    plt.bar(categories, values)  #Plots the stuff

    #Labeling
    plt.xlabel('Categories')  
    plt.ylabel('Values')  
    plt.title(f'{user_name} Statistics Bar Graph:')  

    plt.show() #Shows the graph