def add(v1, v2):
    if isinstance(v1, str):
        v1 = int(v1)

    if isinstance(v2, str):
        v2 = int(v2)

    return v1 + v2


print(add(10, 20))
print(add("10", "20"))
print(add("10", 20))
