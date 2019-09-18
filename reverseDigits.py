def reverseDigits(number) -> int:
	"""
	Returns reverse number int
	"""
	myString = ''
	while int(number) > 0:
		myString = ''.join([myString, str(number % 10)])
		number = int(number / 10)
	return int(myString)