#Question 2

class Product:
    def __init__(self, product_ID, name, price):
        self.product_ID = product_ID
        self.name = name
        self.price = price
    # ...

    def display_info(self):
        print(f"Product: {self.product_ID}, name: {self.name}, price: ${self.price}")
        
class Book(Product):
    def __init__(self, product_id, name, author, price):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        print(f"Product: {self.product_ID}, name: {self.name}, author: {self.author}, price: ${self.price}")

class Electronics(Product):
    def __init__(self, product_id, name, specs, price):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        print(f"Product: {self.product_ID}, name: {self.name}, specs: {self.specs}, price: ${self.price}")

class Clothing(Product):
    def __init__(self, product_id, name, size, price):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        print(f"Product: {self.product_ID}, name: {self.name}, size: {self.size}, price: ${self.price}")
# Example usage
my_product=Product("012", "Coding Temple", 8995)
my_product.display_info()
my_book = Book("123", "Python Essentials", "J. Doe", 29.99)
my_book.display_info()
my_electronics = Electronics("456", "Laptop", "16GB RAM", 799.99)
my_electronics.display_info()
my_clothing = Clothing("789", "Pants", "Large", 39.99)
my_clothing.display_info()