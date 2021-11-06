class Account:
    # static attribute or class attribute
    minbal = 5000

    @staticmethod
    def getminbal():
        return Account.minbal

    # Constructor
    def __init__(self, no, name, amount=0):
        # object attributes
        self.acno = no
        self.ahname = name
        self.balance = amount


    def show(self):
        print(self.acno)
        print(self.ahname)
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds!")

    def getbalance(self):
        return self.balance


print('Min bal ', Account.minbal)
# create object
a1 = Account(1, "Steve")
a1.deposit(10000)
a1.deposit(40000)
print(a1.getbalance())

# Call method
a1.show()

a2 = Account(2, "Mark", 10000)
a2.withdraw(20000)
a2.show()
