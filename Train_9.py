class Product():
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Name: {self.name} | Price: {self.price}")

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def final_price(self):
        discount_amount = self.price * (self.discount_percent / 100)
        return self.price - discount_amount

    def show_info(self):
        super().show_info()
        print(f"Discount: {self.discount_percent}%")
        print(f"Final Price: {self.final_price()}")

p1 = DiscountedProduct("laptop", 2000000,15)
p1.show_info()