class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return f"{self.name}  {self.age}"

people = [
    Person('Паша',20),
    Person('Славік', 21),
    Person('Богдан', 25),
    Person('Діана', 18)
]

sorted_people = sorted(people)
print('Відсортований список за віком')
for person in sorted_people:
    print(person)