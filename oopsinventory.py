from abc import ABC, abstractmethod
# Abstraction
class Item(ABC):
    
    @abstractmethod
    def get_value(self):
        pass


# 2️ Encapsulation

class Product(Item):
    
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def add_stock(self, amount):
        self.__quantity += amount

    def sell_product(self, amount):
        if amount <= self.__quantity:
            self.__quantity -= amount
        else:
            print("Not enough stock!")

    def get_value(self):
        return self.__price * self.__quantity
 
# 3️⃣ Inheritance

class ElectronicProduct(Product):

    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def show_details(self):
        print("Electronic Product:", self.get_name())
        print("Warranty:", self.warranty, "years")


class GroceryProduct(Product):

    def __init__(self, name, price, quantity, expiry):
        super().__init__(name, price, quantity)
        self.expiry = expiry

    def show_details(self):
        print("Grocery Product:", self.get_name())
        print("Expiry Date:", self.expiry)


# 4️ Polymorphism
def display_product_info(product):
    print("Total Value:", product.get_value())

 
# Main Program

laptop = ElectronicProduct("Laptop", 60000, 5, 2)
milk = GroceryProduct("Milk", 50, 100, "10-07-2026")

laptop.show_details()
milk.show_details()

display_product_info(laptop)
display_product_info(milk)