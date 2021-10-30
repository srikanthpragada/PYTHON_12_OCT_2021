def firstname(name):
    pos = name.find(' ')
    if pos == -1:
        return name
    else:
        return name[:pos]


names = ["Joe Stagner", "James Gosling", "Larry Ellison", "Scott"]

for n in map(firstname, names):
    print(n)