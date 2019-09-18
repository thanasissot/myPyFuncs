def isArmstrongNumber(number):
    """checks if a number is an Armstrong number
    https://en.wikipedia.org/wiki/Narcissistic_number
    """
    myArr = []
    temp = number
    while int(temp) > 0:
        temp2 = temp % 10
        myArr.append(int(temp2) ** 3)
        temp /= 10
    if sum(myArr) == number:
        print("Yes")
    else:
        print("No")