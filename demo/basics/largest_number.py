# Take numbers from user until user gives 0 and display largest number

largest = 0
while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break  # Terminate loop

    if n > largest:
        largest = n

print(f"Largest = {largest}")