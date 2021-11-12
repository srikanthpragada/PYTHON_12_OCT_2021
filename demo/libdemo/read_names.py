# Read names from names.txt

f = open("names.txt", "rt")  # Write Text

for line in f.readlines():
    # print(line, end='')
    print(line.strip())

f.close()
