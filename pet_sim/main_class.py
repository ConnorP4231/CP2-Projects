import random  # For random events
import pickle  # For saving and loading pets
from datetime import datetime  # For timestamping

print("""Welcome to the Pet Simulator!
Here you can adopt virtual pets, take care of them, and watch them grow.
Your pets have stats like hunger, happiness, energy, and health.
Take good care of them, and they'll even learn new skills!
""")

# Global dictionary to store all pets
pet_collection = {}

# Food types and their effects
FOOD_TYPES = {
    "kibble": {"hunger": -20, "happiness": +2},
    "treat": {"hunger": -10, "happiness": +10},
    "vegetables": {"hunger": -15, "happiness": +5},
    "meat": {"hunger": -25, "happiness": +3}
}

# Pet class
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

        # Stats
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.level = 1
        self.skills = []
        self.last_updated = datetime.now()

    def feed(self, food_type):
        if food_type not in FOOD_TYPES:
            print("Invalid food type. Try again.")
            return

        effects = FOOD_TYPES[food_type]
        self.hunger = max(0, self.hunger + effects["hunger"])
        self.happiness = min(100, self.happiness + effects["happiness"])
        self.advance_time()
        print(f"{self.name} was fed {food_type}. Hunger and happiness adjusted.")

    def play(self):
        if self.energy < 20:
            print(f"{self.name} is too tired to play. Try letting them sleep.")
            return

        self.happiness = min(100, self.happiness + 15)
        self.energy = max(0, self.energy - 20)
        self.hunger = min(100, self.hunger + 10)
        self.advance_time()
        print(f"You played with {self.name}. Happiness increased, but they're a bit hungrier and tired now.")

    def sleep(self):
        self.energy = min(100, self.energy + 40)
        self.hunger = min(100, self.hunger + 15)
        self.advance_time()
        print(f"{self.name} took a nap. Energy increased, but now they're a bit hungrier.")

    def get_status(self):
        print(f"""
Status for {self.name} the {self.species}:
Age: {self.age} | Level: {self.level}
Hunger: {self.hunger}/100
Happiness: {self.happiness}/100
Energy: {self.energy}/100
Health: {self.health}/100
Skills: {', '.join(self.skills) if self.skills else "None yet"}
        """)

    def advance_time(self):
        # Simulate time effects
        self.health = max(0, self.health - int(self.hunger / 50) - int((100 - self.energy) / 50))
        self.level_up()
        self.random_event()

    def level_up(self):
        # 30% chance to level up if stats are good
        if self.happiness > 80 and self.energy > 50:
            if random.random() < 0.3:
                self.level += 1
                new_skill = f"Skill_{self.level}"
                self.skills.append(new_skill)
                print(f"{self.name} leveled up to Level {self.level} and learned {new_skill}!")

    def random_event(self):
        chance = random.randint(1, 100)
        if chance <= 10:
            self.health = max(0, self.health - 10)
            print(f"Oh no! {self.name} got sick and lost some health.")
        elif chance >= 90:
            self.happiness = min(100, self.happiness + 10)
            print(f"{self.name} found a toy and got happier!")

# Create a new pet
def create_pet():
    name = input("Enter pet name: ").strip()
    species = input("Enter species: ").strip()
    while True:
        try:
            age = int(input("Enter pet's age: ").strip())
            break
        except ValueError:
            print("Please enter a valid number for age.")

    new_pet = Pet(name, species, age)
    pet_collection[name.lower()] = new_pet
    print(f"{name} the {species} has been added to your collection!")

# Select a pet
def select_pet():
    if not pet_collection:
        print("No pets available. Add one first.")
        return None

    print("Your pets:")
    for pet_name in pet_collection:
        print(f"- {pet_name.title()}")

    choice = input("Enter the name of the pet you want to select: ").strip().lower()
    return pet_collection.get(choice, None)

# Save pets to file
def save_pets():
    try:
        with open("pets_data.pkl", "wb") as f:
            pickle.dump(pet_collection, f)
        print("Pets saved successfully!")
    except Exception as e:
        print(f"Something went wrong while saving: {e}")

# Load pets from file
def load_pets():
    global pet_collection
    try:
        with open("pets_data.pkl", "rb") as f:
            pet_collection = pickle.load(f)
        print("Pets loaded successfully!")
    except FileNotFoundError:
        print("No saved pets found.")
    except Exception as e:
        print(f"Something went wrong while loading: {e}")

# Reset pets (delete save file data)
def reset_pets():
    confirm = input("Are you sure you want to delete all saved pets? (yes/no): ").strip().lower()
    if confirm == "yes":
        with open("pets_data.pkl", "wb") as f:
            pickle.dump({}, f)
        print("All saved pets have been reset.")
        pet_collection.clear()
    else:
        print("Reset cancelled.")

# Submenu for interacting with a selected pet
def pet_menu(pet):
    while True:
        option = input(f"""
Pet Menu - {pet.name.title()} the {pet.species}
1. Feed
2. Play
3. Sleep
4. Check Status
5. Return to Main Menu

Choose an option: """).strip()

        if option == '1':
            print(f"Available foods: {', '.join(FOOD_TYPES.keys())}")
            food = input("Enter a food type to feed your pet: ").strip().lower()
            pet.feed(food)
        elif option == '2':
            pet.play()
        elif option == '3':
            pet.sleep()
        elif option == '4':
            pet.get_status()
        elif option == '5':
            print("Returning to main menu...")
            break
        else:
            print("Invalid input. Try again.")

# Main program loop
def main():
    load_pets()

    while True:
        option = input("""
Main Menu:
1. Create a new pet
2. Select a pet
3. Save pets
4. Load pets
5. Exit
6. Reset all saved pets

Choose an option: """).strip()

        if option == '1':
            create_pet()
        elif option == '2':
            selected_pet = select_pet()
            if selected_pet:
                pet_menu(selected_pet)
        elif option == '3':
            save_pets()
        elif option == '4':
            load_pets()
        elif option == '5':
            save_pets()  # Autosave on exit
            print("Thanks for playing! Your pets will miss you.")
            break
        elif option == '6':
            reset_pets()
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

# Start the game
if __name__ == "__main__":
    main()
