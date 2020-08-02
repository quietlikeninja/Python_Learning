class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type.capitalize()
        self.max_health = level * 5
        self.health = self.max_health
        self.is_knocked_out = False
    
    def __repr__(self):
        return f'''
        Name:        {self.name}
        Level:       {self.level}
        Type:        {self.type}
        Max Health:  {self.max_health}
        Cur Health:  {self.health}
        Knocked out: {self.is_knocked_out}
        '''

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
        print(f"{self.name} attacks {other_pokemon.name}")
        if self.is_knocked_out:
            print(f"{self.name} can't attack while knocked out")
            return
        if other_pokemon.is_knocked_out:
            print(f"{other_pokemon.name} is already knocked out")
            return
        if attack_types.get(self.type.lower()):
            if other_pokemon.type.lower() in attack_types.get(self.type.lower()).get("advantage"):
                print(f"{self.name} has attacked {other_pokemon.name} with an attack multiplier of 2 dealing {self.level * 2} damage")
                other_pokemon.lose_health(self.level * 2)
            elif other_pokemon.type.lower() in attack_types.get(self.type.lower()).get("disadvantage"):
                print(f"{self.name} has attacked {other_pokemon.name} with an attack multiplier of 0.5 dealing {self.level * 0.5} damage")
                other_pokemon.lose_health(self.level * 0.5)
            else:
                print(f"{self.name} has attacked {other_pokemon.name} with no attack multiplier dealing {self.level} damage")
                other_pokemon.lose_health(self.level)
        else:
            #Should this be an exception?
            print("No type in DB")

class Charmander(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Charmander", level, "fire")

class Squirtle(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Squirtle", level, "water")

class Gloom(Pokemon):
    def __init__(self, level = 1):
        super().__init__("Gloom", level, "grass")

class Trainer:
    def __init__(self, name, pokemons, num_potions, active_pokemon = 0):
        self.name = name
        self.pokemons = pokemons
        self.num_potions = num_potions
        self.active_pokemon = active_pokemon

    def __repr__(self):
        print(f'''
        Trainer Name:   {self.name}
        Potions:        {self.num_potions}
        Active Pokemon: {self.pokemons[self.active_pokemon].name}
        ''')
        for pokemon in self.pokemons:
            if pokemon.name == self.pokemons[self.active_pokemon].name:
                print('''
        *****Active*****''')
            print(pokemon)
        return ""
    
    def set_active(self, pokemon):
        #add logic to cater for non existent pokemon and knoocked out pokemon
        self.active_pokemon = pokemon
        print(f'{self.name}\'s current pokemon is now {self.pokemons[self.active_pokemon].name}')

    def get_active(self):
        print(f'{self.name}\'s current pokemon is {self.pokemons[self.active_pokemon].name}')

    def heal(self):
        #add logic to heal active pokemon
    
    def attack(self, other_trainer):
        #add logic for active pokemon to attack other trainers active pokemon


attack_types = {
    "fire": {"advantage": ["grass"], "disadvantage": ["fire", "water"]},
    "water": {"advantage": ["fire"], "disadvantage": ["grass", "water"]},
    "grass": {"advantage": ["water"], "disadvantage": ["fire", "grass"]}
}

a = Charmander(5)
b = Squirtle(2)
c = Gloom(10)
d = Charmander()

t1 = Trainer("Justin", [a,c], 6, 1)
t2 = Trainer("Steph", [b,d], 6, 1)

t1.get_active()
t1.set_active(0)
t1.get_active()


"""b.attack(d)
d.attack(b)
b.attack(d)
b.attack(d)
b.attack(d)

print(d)"""
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