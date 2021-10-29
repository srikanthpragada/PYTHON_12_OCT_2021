def add(a, b):
    print(a + b)


add2 = add


def add(a, b, c):
    print(a + b + c)


add2(10, 20)
add(10, 20, 30)
