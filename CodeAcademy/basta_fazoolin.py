#https://www.codecademy.com/courses/learn-python-3/projects/basta-fazoolin
from datetime import time

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return f"The resturants address is {self.address}"
    
    def available_menus(self, time):
        menus = []
        for menu in self.menus:
            if (time >= menu.start_time) and (time <= menu.end_time):
                menus.append(menu)
        return menus

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu is available from {self.start_time.strftime('%I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill


def main():
    brunch_menu_items = {
        'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
        'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
        'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
        }
    brunch_menu = Menu("Brunch", brunch_menu_items, time(11, 00), time(16, 00))

    early_bird_menu_items = {
        'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
        'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 
        'coffee': 1.50, 'espresso': 3.00
        }
    early_bird_menu = Menu("Early Bird Dinner", early_bird_menu_items, time(15, 00), time(18, 00))

    dinner_menu_items = {
        'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
        'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
        'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
        }
    dinner_menu = Menu("Dinner", dinner_menu_items, time(17, 00), time(23, 00))

    kids_menu_items = {
        'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
        'apple juice': 3.00
        }
    kids_menu = Menu("Kids", kids_menu_items, time(11, 00), time(21, 00))

    arepas_menu_items = {
        'arepa pabellon': 7.00, 'pernil arepa': 8.50, 
        'guayanes arepa': 8.00, 'jamon srepa': 7.50
        }
    arepas_menu = Menu("Arepas", arepas_menu_items, time(10, 00), time(20, 00))

    flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
    new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
    arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

    basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
    arepa = Business("Take a' Arepa", [arepas_place])

    #print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
    #print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
    #print(flagship_store.available_menus(time(17, 00)))
    print(basta.franchises[0].menus)

if __name__ == '__main__':
    main()