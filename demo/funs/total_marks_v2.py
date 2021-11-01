marks = ["70,85,30", "80,70", "35,45,abc,48"]

for m in marks:
    parts = m.split(",")
    valid_parts = filter(str.isdigit, parts)
    numbers = map(int, valid_parts)
    print(sum(numbers))
