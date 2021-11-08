class Person:
    def __init__(self, name, age):
        # Private attributes
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age


p1 = Person("Abc", 20)
print(p1)  # str(p1)  --> p1.__str__()
p2 = Person("Abc", 20)
print(p1 == p2)  # p1.__eq__(p2)
p3 = Person("Xyz", 30)
# print(p3 > p1)  # p3.__gt__(p1)

people = [Person("A", 20), Person("C", 15), Person("B", 30)]

for p in sorted(people):
    print(p)

for p in sorted(people, key=lambda p: p.name):
    print(p)
