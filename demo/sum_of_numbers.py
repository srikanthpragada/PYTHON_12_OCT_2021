# Take numbers from user until user gives 0 and display total of numbers

total = 0
while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break  # Terminate loop

    total += n

print(f"Total = {total}")