names = ["Abc", "Bdkdfd", "Ieieier", "dd", "xy", "Eeieee"]

for n in filter(lambda v: len(v) > 3, names):
    print(n)

for n in filter(lambda v: v[0].isupper(), names):
    print(n)