# 5th mathematical problem for geeksforgeeks practice
# closest number
def closestNumber(a, b):
    """Return the number closes to a that is divisible by M, if there
    are more than one it returns the maximum absolute value
    """
    if a % b == 0:
        return a
    if b < 0:
        b *= -1
    for x in range(1, b + 1):
        if a < 0:
            x *= - 1
        if (a + x) % b == 0:
            return a + x
        elif (a - x) % b == 0:
            return a - x