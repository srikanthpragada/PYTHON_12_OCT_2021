class Person:
    def __init__(self, name, age):
        # Private attributes
        self.__name = name
        self.__age = age

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age


p = Person("Abc", 20)
print(p.__dict__)
# print(p._Person__age)
print(p.getage())
