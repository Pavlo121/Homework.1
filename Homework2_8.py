from functools import total_ordering

class Price:
    def __init__(self, amount):
        self.amount = round(amount, 2)

    def __add__(self, other):
        return Price(self.amount + other.amount)

    def __sub__(self, other):
        return Price(self.amount - other.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __repr__(self):
        return f'${self.amount:.2f}'

price1 = Price(19.99)
price2 = Price(5.50)

total_price = price1 + price2
print("Сумарна ціна", total_price)

discounted_price = price1 - price2
print("Ціна зі знижкою", discounted_price)




