import re

class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def email(self):
        return self.email

user = User("Павло", "Саракій", "PavloSarakiy@gmail.com")
print("Ім'я:", user.first_name)
print("Призвище:", user.last_name)
print("Email:", user.email)










