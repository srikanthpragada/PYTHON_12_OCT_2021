
num = 175

for i in range(2, num//2 + 1):
    if num % i == 0:
        print("Not a prime")
        break
else:
    print("Prime number!")
