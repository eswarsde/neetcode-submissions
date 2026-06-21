class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health 


# TODO: Create Superhero instances
s1 = SuperHero("Batman", "Intelligence", 100)
s2 = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero
print(s1.name)
print(s1.power)
print(s1.health)

print(s2.name)
print(s2.power)
print(s2.health)
