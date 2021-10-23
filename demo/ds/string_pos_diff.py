s1 = "Abdccg"
s2 = "Abccc"


s1_len = len(s1)
s2_len = len(s2)

i = 0
while i < s1_len and i < s2_len:
    if s1[i] != s2[i]:
        print(f"Differ at {i}")
        break

    i += 1
else:
    if s1_len == s2_len:
        print("Equal")
    else:
        print(f"Differ at {i}")
