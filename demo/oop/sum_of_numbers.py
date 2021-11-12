
total = 0
while True:
    try:
        num = int(input("Enter a number [0 to stop] :"))
        if num == 0:
            break

        total += num
    except ValueError:
        print('Invalid number!')

print(total)