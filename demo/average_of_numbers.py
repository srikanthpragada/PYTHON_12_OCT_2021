# Take 5 numbers from user and print average

total = 0
for i in range(5):
    n = int(input("Enter a number :"))
    total += n

print(f"Average = {total / 5}")
