def contains_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


values = ["Abc", "Abc122", "Xy33", "Pq", "Def1"]

for n in filter(contains_digit, values):
    print(n)
