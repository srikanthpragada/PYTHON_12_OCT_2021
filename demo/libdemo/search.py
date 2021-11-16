# Usage: python search.py pattern [startdir]
# Displays all .py files where pattern is present
# If startdir is not given then take current directory

import os
import sys


def contains_pattern(filename, pattern):
    try:
        with open(filename, "rt") as f:
            return pattern in f.read()
    except:
        return False


if len(sys.argv) < 2:
    print("Usage : python search.py pattern [startdir]")
    exit(1)


if len(sys.argv) == 3:
    startdir = sys.argv[2]
else:
    startdir = os.getcwd()

pattern = sys.argv[1]

entries = os.walk(startdir)

for name, dirs, files in entries:
    for f in files:
        if f.endswith(".py"):
            filename = name + "\\" + f
            if contains_pattern(filename, pattern):
                print(filename)
