def numbers():
    for n in range(1, 10):
        yield n


def upper(st):
    for c in st:
        if c.isupper():
            yield c


n = numbers()
print(type(n))
print(next(n))
print(next(n))

g = upper("Hello How ARE YOU")
for c in g:
    print(c)
