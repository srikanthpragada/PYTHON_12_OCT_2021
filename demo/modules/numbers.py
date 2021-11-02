# Number related functions

def iseven(n: int) -> bool:
    """
    Returns true if the given number is even otherwise false
    """
    return n % 2 == 0


def ispositive(n):
    """
       Returns true if the given number is positive (>0) otherwise false
    """
    return n > 0


def isprime(n):
    pass


# Testing - run when module is executed as script and not imported
if __name__ == '__main__':
    print("Testing Numbers")
    print(iseven(10))
    print(ispositive(-10))
