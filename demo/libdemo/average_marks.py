# Read marks from marks.txt and display average

f = open("marks.txt", "rt")  # Write Text

total = 0
count = 0
for line in f.readlines():
     total += int(line)
     count += 1

f.close()
print(f"Average = {total / count}")