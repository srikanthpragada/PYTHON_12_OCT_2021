def ispass(m):
    return m >= 50


marks = [70, 45, 68, 34, 65, 78, 98, 31]

for n in filter(ispass, marks):
    print(n)

for n in filter(lambda v: v > 50, marks):
    print(n)
