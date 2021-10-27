
st = "how do you do"

chars = {}

for c in st:
    if c not in chars:
        chars[c] = st.find(c)


print(chars)

