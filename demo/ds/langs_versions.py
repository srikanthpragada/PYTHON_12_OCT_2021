langs = ['Java', 'Python', 'C#', 'JavaScript' , "Ruby"]
vers = [17, 3.10, 11]

for idx, lang in enumerate(langs):
    if idx < len(vers):
        print(f"{lang:20}  {vers[idx]}")
    else:
        print(f"{lang:20}")
