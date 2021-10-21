num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

smallest = num1 if num1 < num2 else num2

i = smallest // 2

while True:
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break

    i -= 1

