import os

entries = os.walk(r"c:\classroom\oct12\demo")

for name, dirs, files in entries:
    print(f"{name:50}  {len(files):3}")
   