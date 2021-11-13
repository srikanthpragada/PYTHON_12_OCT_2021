# Read marks from marks.txt and display average

f = open("marks.txt", "rt")  # Write Text

total = 0
count = 0
for line in f.readlines():
     try:
          total += int(line)
          count += 1
     except:
          pass

f.close()
print(f"Average = {total / count}")