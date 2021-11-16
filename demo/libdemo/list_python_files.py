import os

entries = os.walk(r"c:\classroom\oct12\demo")

count = 0
for name, dirs, files in entries:
    for f in files:
        if f.endswith(".py"):
            print(name + "\\" + f)
            count += 1

print(f"Count = {count}")
