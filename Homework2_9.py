import re

class ProductWithGetSet:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        self._price = value

class ProductWithProperty:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        self._price = value

class PriceDescriptor:
    def __get__(self, instance, owner):
        return instance._price

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        instance._price = value

class ProductWithDescriptor:
    price = PriceDescriptor()

    def __init__(self, name, price):
        self.name = name
        self.price = price


def test_products():
    product1 = ProductWithGetSet("Товар A", 100.0)
    print(f"Product 1: {product1.name}, Price: {product1.get_price()}")
    try:
        product1.set_price(-10)
    except ValueError as e:
        print(e)

    product2 = ProductWithProperty("Товар B", 200.0)
    print(f"Product 2: {product2.name}, Price: {product2.price}")
    try:
        product2.price = -20
    except ValueError as e:
        print(e)

    product3 = ProductWithDescriptor("Товар C", 300.0)
    print(f"Product 3: {product3.name}, Price: {product3.price}")
    try:
        product3.price = -30
    except ValueError as e:
        print(e)

test_products()
