marks = ["70,85,30", "80,70", "35,45,48"]

for m in marks:
    numbers = map(int, m.split(","))
    print(sum(numbers))