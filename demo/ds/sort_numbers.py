# Take numbers until 0 and sort them

l = []
while True:
    m = int(input("Enter the number [-1 to stop] :"))
    if m == -1:
        break

    l.append(m)

l.sort()
print(l)
