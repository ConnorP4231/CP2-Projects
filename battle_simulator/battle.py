import csv

def parse_stat(stat_str):
    """Extracts the numeric part from a stat string like 'Health: 90'."""
    return int(stat_str.split(":")[1].strip())  # Extract the part after 'Health: ', 'Strength: ', etc.

def battle():
    """Simulate a battle between the user's character and the computer's character based on their stats."""
    
    # Load the battle data from battle_data.csv
    with open("battle_simulator/battle_data.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        
        # Read the user and computer characters' data
        user_data = next(reader)  # First row is user character
        computer_data = next(reader)  # Second row is computer character
        
        # Printing both sides.
        print(f"\nUser data: {user_data}")
        print(f"Computer data: {computer_data}")
        
        if len(user_data) < 5 or len(computer_data) < 5: #makes sure that all values are correct.
            print("Error: One of the character rows is missing data. Make sure there are 5 elements per row.")
            return
        
        # Extract user stats
        user_name = user_data[0]
        user_health = parse_stat(user_data[1])
        user_strength = parse_stat(user_data[2])
        user_defense = parse_stat(user_data[3])
        user_speed = parse_stat(user_data[4])
        
        # Extract computer stats
        computer_name = computer_data[0]
        computer_health = parse_stat(computer_data[1])
        computer_strength = parse_stat(computer_data[2])
        computer_defense = parse_stat(computer_data[3])
        computer_speed = parse_stat(computer_data[4])
    
    # Print the stats of the characters
    print(f"\nBattle begins between {user_name} and {computer_name}!")
    print(f"{user_name} Stats - Health: {user_health}, Strength: {user_strength}, Defense: {user_defense}, Speed: {user_speed}")
    print(f"{computer_name} Stats - Health: {computer_health}, Strength: {computer_strength}, Defense: {computer_defense}, Speed: {computer_speed}")

    user_points = user_health + user_strength + user_defense + user_speed #User stats added together
    computer_points = computer_health + computer_strength + computer_defense + computer_speed #Computer stats added together.

    if user_points > computer_points: #Sees which one has higher points.
        with open("battle_simulator/points.txt", "r+") as file:
            # Read the current XP value from the file (assuming it's a single integer)
            XP = int(file.read().strip())  # Convert the string to an integer
            total_XP = XP + 5 #Adds 5 XP when the user wins.
            
            # Go back to the start of the file to overwrite the value
            file.seek(0)
            file.write(str(total_XP))  # Write the new total XP back to the file
        
        # Return the total XP gained
        print(f'You won and gained 5 XP! You now have a total of {total_XP} XP.')

    elif computer_points > user_points:
        print('Computer won!')
