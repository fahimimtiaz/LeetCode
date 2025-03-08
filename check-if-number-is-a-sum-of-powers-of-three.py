def checkPowersOfThree(n):
    while n > 0:
        print("value of n: ", n)
        if n % 3 == 2:
            return False
        n //= 3
    return True

# Test cases
print(checkPowersOfThree(12))  # True
print(checkPowersOfThree(91))  # True
print(checkPowersOfThree(21))  # False
