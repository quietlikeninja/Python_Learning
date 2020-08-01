from datetime import time

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "The {name} menu is available between {start} and {end}.".format(name=self.name, start=self.start_time.strftime("%I%p"), end=self.end_time.strftime("%I%p"))

  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      if item in self.items:
        total_bill += self.items[item]
      else:
        return "{item} is not on the {name} menu".format(item=item, name=self.name)
    return total_bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#Menus
brunch_items = {
  'pancakes': 7.50,
  'waffles': 9.00,
  'burger': 11.00,
  'home fries': 4.50,
  'coffee': 1.50,
  'espresso': 3.00,
  'tea': 1.00,
  'mimosa': 10.50,
  'orange juice': 3.50
  }
brunch_menu = Menu("Brunch", brunch_items, time(hour=11), time(hour=16))

early_bird_items = {
  'salumeria plate': 8.00,
  'salad and breadsticks (serves 2, no refills)': 14.00,
  'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 1.50,
  'espresso': 3.00
  }
early_bird_menu = Menu("Early-bird", early_bird_items, time(hour=15), time(hour=18))

dinner_items = {
  'crostini with eggplant caponata': 13.00,
  'ceaser salad': 16.00,
  'pizza with quattro formaggi': 11.00,
  'duck ragu': 19.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 2.00,
  'espresso': 3.00
  }
dinner_menu = Menu("Dinner", dinner_items, time(hour=17), time(hour=23))

kids_items = {
  'chicken nuggets': 6.50,
  'fusilli with wild mushrooms': 12.00,
  'apple juice': 3.00
  }
kids_menu = Menu("Kids", kids_items, time(hour=11), time(hour=21))

arepas_items = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa': 7.50
  }
arepas_menu = Menu("Arepas", arepas_items, time(hour=10), time(hour=20))

#Franchises
flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#Businesses
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas = Business("Take a' Arepa", [arepas_place])

#print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
#print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

#print(new_installment.available_menus(time(hour=17)))

print(arepas.franchises)