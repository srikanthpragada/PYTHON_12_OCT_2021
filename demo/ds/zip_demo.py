langs = ['Java', 'Python', 'C#', 'JavaScript']
vers = [17, 3.10, 11]

# for i, l in enumerate(langs):
#     print(l, vers[i])

for l, v in zip(langs, vers):
    print(l, v)
