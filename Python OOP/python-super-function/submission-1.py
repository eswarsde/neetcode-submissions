class SuperHero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power
    
    def attack(self) -> None:
        print(f"{self.name} is attacking with {self.power}")

class Avenger(SuperHero):
    def __init__(self,name, power, team):
        super().__init__(name, power)
        self.team = team 
    
    def attack(self):
        super().attack()



# TODO: Create a Avenger class that inherits from the SuperHero class
# TODO: Override the __init__ method to add a team property to the Avenger class
# TODO: Call the attack method of the SuperHero class from the Avenger class



# Don't change the code below
avenger = Avenger("Iron Man", "repulsor beams", "Avengers")
print(avenger.name)
print(avenger.power)
print(avenger.team)
avenger.attack()
