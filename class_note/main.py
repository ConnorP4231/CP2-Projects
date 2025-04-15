class subject:
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f'name: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}\nRoom: {self.room}'


first = subject("CS Principles", 1, "Ms. LaRose", 200)
second = subject("CP2", 2, "Ms. LaRose", 200)


class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp 
        self.dmg = dmg

    def __str__(self):
        return f'{self.name} is a {self.species} and they have {self.hp} HP and do {self.dmg} amount of damage in battle.'

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f'{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}.')

            if opponent.hp <= 0:
                print(f'{opponent.name} is knocked out. {self.name} wins!')
            else:
                self.hp -= opponent.dmg
                print(f'{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp}.')

                if self.hp <= 0:
                    print(f'{self.name} is knocked out. {opponent.name} wins!')

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spiky = pokemon("Spiky", "Jolteon", 150, 100)

fluffy.battle(spiky)
slimy.battle(spiky)

# What is a class in python?
    # It is a blueprint for an object.

# What is an object in python?
    # It is an instance of a class.

# How do python classes relate to python objects?
    # Python classes can create python objects.

# How do you create a python class?
    # class className:
        # def functionInTheClass:
            # function contents

# What are methods?
    #They are functions created in a specific class.

# How do you create a python object?
    #Using a python class and inputs.

# How do you call a method for an object?
    # method(paramater1, parameter 2...)

# Why do we use python classes?
    # They help us sort functions and create objects needed for a program.