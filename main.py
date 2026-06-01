#5-masala
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

p1 = Phone("iPhone", 1200)

print(p1.price)

p1.price = 1500
print(p1.price)
