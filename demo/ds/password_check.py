# Check whether two strings have same set of chars

pwd1 = "abc123"
pwd2 = "123abcc"

uncommon = set(pwd1) ^ set(pwd2)
if len(uncommon) == 0:
    print("Invalid")
else:
    print("Valid")