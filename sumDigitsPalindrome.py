def isSumOfDigitsPalindrome(number):
	"""Checks if the sum of the numbers digits are a palindrome
	"""
	mySum = 0
	while int(number) > 0:
		mySum += number % 10
		number = int(number/10)
	mySum = str(mySum)
	if mySum[:len(mySum)-1] == mySum[len(mySum)-1:] or len(mySum) == 1:
		print("YES")
	else:
		print("NO")
