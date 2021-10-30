def hello():
    print("Hello")


def goodbye():
    print("Good Bye!")


def greet(func):
    func()


greet(hello)
greet(goodbye)
