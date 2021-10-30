marks = ["80", "98", "76", "65"]

# print(sum(marks))

total = 0
for v in marks:
    total += int(v)

print(total)

print(sum(map(int, marks)))
