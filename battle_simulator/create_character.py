import csv

def create_character():
    """Creates a new character and saves it to a CSV file."""
    name = input("What is the name of your character?: ")

    def get_stat(stat_name):
        """Inner function to get a valid stat between 1-100."""
        while True:
            try:
                value = int(input(f"What is your character's {stat_name}? (1-100): "))
                if 1 <= value <= 100:
                    return value
                else:
                    print("Value must be between 1 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    def save_character(name, health, strength, defense, speed):
        """Inner function to save character data to the CSV file."""
        with open("battle_simulator/characters.csv", "a", newline="") as file:
            writer = csv.writer(file)
            # Remove the extra newline \n from the string
            formatted_string = f"Name - {name}:,Health: {health},Strength: {strength},Defense: {defense},Speed: {speed}"
            writer.writerow([formatted_string])  # Writing as a single cell row

    # Call the functions to get actual values (previously, the function objects were stored instead)
    health = get_stat("health")
    strength = get_stat("strength")
    defense = get_stat("defense")
    speed = get_stat("speed")

    # Save character using the inner function
    save_character(name, health, strength, defense, speed)

    return f"Character {name} has been created successfully!"