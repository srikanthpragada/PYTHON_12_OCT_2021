def ispass(m):
    return m >= 50


marks = [70, 45, 68, 34, 65, 78, 98, 31]

for n in filter(ispass, marks):
    print(n)

# display all uppercase letters

for c in filter(str.isupper, "How Are You"):
    print(c)
