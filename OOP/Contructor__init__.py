class Item:
    pay_rate = 0.8  #Class Variable or attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the received arguments:
        assert price >= 0, f"Price {price:.2f} is not greater than or equal to zero!" #f"" = f ormatted string
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        #Assign to self object:
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute:
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    def __repr__(self): #representing method to show all objects
        return f"Item('{self.name}',{self.price}, {self.quantity})"
'''
Item1 = Item("Phone", 100,1)
Item2 = Item("Laptop", 1000,3)

print(Item1.calculate_total_price())
print(Item2.calculate_total_price())

print(Item.__dict__)    #All the attributes for Class level
print(Item1.__dict__)   #All the attributes for Instance level

Item1.apply_discount()
print(Item1.price)

Item2.pay_rate = 0.7
Item2.apply_discount()
print(Item2.price)
'''    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

'''
for instance in Item.all:
    print(instance.name)
'''