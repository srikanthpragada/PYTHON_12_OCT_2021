def zero(v):
    print(id(v))
    v = 0
    print(id(v))


def prepend(lst, value):
    lst.insert(0, value)


a = 10
print(id(a))
zero(a)
print(a)

l = [10, 20]
prepend(l, 100)
print(l)
