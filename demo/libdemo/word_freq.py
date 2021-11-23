import re

with open(f"c:\classroom\oct12\old_man.txt") as f:
    contents = f.read()

words = re.findall(r'\w+', contents)

for w in sorted(set(words)):
    print(f"{w:15} - {words.count(w):3}")
