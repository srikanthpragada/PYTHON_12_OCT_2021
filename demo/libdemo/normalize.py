import re

with open(f"story.txt", "rt") as f:
    contents = f.read()

step1 = re.sub(r'[ ,;]+', ' ', contents)
step2 = re.sub(r'\n+', r'\n', step1)

with open(f"story.txt", "wt") as f:
    f.write(step2)

