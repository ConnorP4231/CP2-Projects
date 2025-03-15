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
        file_path = "battle_simulator/characters.csv"

        # Check if file exists by attempting to read it
        try:
            with open(file_path, "r") as file:
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        # Open file in append mode and write character data
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Health", "Strength", "Defense", "Speed"])  # Add headers
            writer.writerow([])
            writer.writerow([f"Name - {name}:", f"Health: {health}", f"Strength: {strength}", f"Defense: {defense}", f"Speed: {speed}"]) # Save character stats properly

    # Get character stats
    health = get_stat("health")
    strength = get_stat("strength")
    defense = get_stat("defense")
    speed = get_stat("speed")

    # Save character
    save_character(name, health, strength, defense, speed)