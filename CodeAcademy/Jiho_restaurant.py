class Table:
    def __init__(self, table_number, name="", vip_status=False, order=None) -> None:
       self.table_number = table_number
       self.name = name
       self.vip_status = vip_status
       if order is None:
        self.order = {}

    def __repr__(self) -> str:
        return f"""
        Table Number: {self.table_number}
        Name: {self.name}
        VIP Status: {self.vip_status}
        Order: {self.order}"""

    def place_order(self, **order_items):
        if order_items.get('food'):
            food = order_items.get('food')
            self.order["Food"] = self.order.get("Food", []) + food
            print(food)
        if order_items.get('drinks'):
            drinks = order_items.get('drinks')
            self.order["Drinks"] = self.order.get("Drinks", []) + drinks
            print(drinks)
        if order_items.get('total'):
            total = order_items.get('total')
            self.order["Total"] = self.order.get("Total", []) + total
            print(total)

    def change_order(self, **order_items):
        if order_items.get('food') and "Food" in self.order:
            for food in order_items.get('food'):
                self.order["Food"].remove(food)
        if order_items.get('drinks') and "Drinks" in self.order:
            for drink in order_items.get('drinks'):
                self.order["Drinks"].remove(drink)

    def calculate_price_per_person(self, ):
        pass
        #total, tip, split = tables[table_number]['order']['total']
        #total_tip = total * (tip/100)
        #split_price = (total + total_tip) / split
        #print(split_price)

#    def clean_table(self):
#        self.name = ""
#        self.vip_status = ""
#        self.order = {}

def main():
    total_tables = 8
    tables = [Table(x) for x in range(1, total_tables+1)]
    print(tables)
    tables[1].name = "Justin"
    tables[1].place_order(food = ["Eggs", "Bacon"], drinks = ["Coffee"])
    tables[1].place_order(food = ["Toast"])
    tables[1].place_order(drinks = ["Orange Juice"])
    print(tables[1])
    tables[1].change_order(food = ["Eggs"])
    print(tables[1])
    #table1.clean_table()

if __name__ == '__main__':
    main()