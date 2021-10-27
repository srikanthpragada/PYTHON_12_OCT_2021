def isprime(num : int) -> bool:
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return False

    return True


print(isprime(13), isprime(393939331))
