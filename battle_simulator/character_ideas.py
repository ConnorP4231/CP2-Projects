# Connor Pavicic, character_ideas
from faker import Faker
import random

fake = Faker() #Uses fake instead of Faker()

def random_character():
    name = fake.name() #Generating each thing with faker
    age = random.randint(18, 65)
    job = fake.job()
    city = fake.city()
    hobby = random.choice(['hiking', 'coding', 'running', 'playing video games', 'sleeping', 'biking']) #For these I just used a list since faker didn't have anything like this
    goal = random.choice(['take over the world', 'solve world hunger', 'became a famous streamer', 'win a MrBeast challenge'])

    lore = f'{name} is a {age}-year-old {job} from {city}. {name} really loves {hobby} and one day wants to {goal}.' # Puts all the things in a sentence.
    print(lore)