import csv

class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Run validation to the received arguments
        assert price >= 0, f" Price {price} not greater than zero"
        assert quantity >= 0, f" Quantity {quantity} not greater than zero"

        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)

 



    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    pass

phone1 = Item("jsvPhone10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("jsvPhone20", 700, 5)
phone2.broken_phones = 1




