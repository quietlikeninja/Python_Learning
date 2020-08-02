class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level * 100
        self.health = self.max_health
        self.is_knocked_out = False
    
    def lose_health(self, points):
        if self.health - points <= 0:
            self.knock_out()
        else:
            self.health = self.health - points
            print(f"{self.name} has lost {points} points of health and now has {self.health} remaining.")

    def gain_health(self, points):
        if self.is_knocked_out:
            return print(f"{self.name} is currently knocked out and needs to be revived")
        if self.health + points > self.max_health:
            self.health = self.max_health
        else:
            self.health += points
        print(f"{self.name} has gained {points} points of health and now has {self.health} remaining.")
    
    def knock_out(self):
        if not self.is_knocked_out:
            self.is_knocked_out = True
            self.health = 0
            print(f"{self.name} has been knocked out")
        else:
            print(f"{self.name} was already knocked out")

    def revive(self):
        if self.is_knocked_out:
            self.is_knocked_out = False
            self.health = self.max_health
            print(f"{self.name} has been revived")
        else:
            print(f"{self.name} doesn't need to be revived")

    def attack(self, other_pokemon):
        attack_multiplier = 1
        print(f"{self.name} attacks {other_pokemon.name}")
        if self.is_knocked_out:
            print(f"{self.name} can't attack while knocked out")
            return
        if other_pokemon.is_knocked_out:
            print(f"{other_pokemon.name} is already knocked out")
            return
        if attack_types.get(self.type):
            if other_pokemon.type in attack_types.get(self.type).get("advantage"):
                attack_multiplier = 2
                print(f"{self.name} has an advantage of a {attack_multiplier} times attack multiplier")
            else:
                attack_multiplier = 0.5
                print(f"{self.name} has a disadvantage of a {attack_multiplier} times attack multiplier")
        else:
            print("No type in DB")
        other_pokemon.lose_health(10 * attack_multiplier)
        
attack_types = {
    "fire": {"advantage": ["grass"], "disadvantage": ["fire", "water"]},
    "water": {"advantage": ["fire"], "disadvantage": ["grass", "water"]},
    "grass": {"advantage": ["water"], "disadvantage": ["fire", "grass"]}
}
charmander = Pokemon("Charmander", 1, "fire")
squirtle = Pokemon("Squirtle", 1, "water")
gloom = Pokemon("Gloom", 1, "grass")

charmander.attack(squirtle)
charmander.attack(gloom)

#charmander.attack(squirtle)
#Charmander attackes Squirtle
#charmander.lose_health(100)
#Charmander has been knocked out
#charmander.attack(squirtle)
#Charmander can't attack while knocked out
#charmander.revive()
#Charmander has been revived
#squirtle.lose_health(100)
#Squirtle has been knocked out
#charmander.attack(squirtle)
#Squirtle is already knocked out