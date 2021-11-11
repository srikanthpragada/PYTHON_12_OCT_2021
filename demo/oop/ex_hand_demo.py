try:
    n = int(input("Enter number :"))
    print(100 // n)
except ValueError:
    print("Sorry! Invalid input!")
except ZeroDivisionError:
    print("Sorry! Number cannot be zero!")
finally:
    print("Do something")


print("The END")
