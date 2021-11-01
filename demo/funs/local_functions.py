v = 100  # global variable


def f1():
    a = 10  # Enclosing variable
    global v
    v = 10

    def f2():  # local function
        nonlocal a
        b = 20  # Local variable
        a = 1
        print(v, a, b)

    f2()
    print(a)


f1()
