class MyCollection:

    def __init__(self, items):
        self.items = items

    def my_len(self):
        count = 0
        for i in self.items:
            count += 1
        return count

    def my_sum(self):
        total = 0
        for items in self.items:
            total += items
        return total

    def my_min(self):
        if not self.items:
            return ValueError('Порожня колекція')

        minimum = self.items[0]
        for item in self.items:
            if item < minimum:
                minimum = item
        return minimum

collection = MyCollection([3, 1, 4, 1, 5, 9])
print("Довжина колекції:", collection.my_len())
print("Сума елементів:", collection.my_sum())
print("Мінімальний елемент:", collection.my_min())




