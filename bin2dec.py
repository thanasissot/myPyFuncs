def bin2dec(number):
	"""
	transform binary sequence to decimal
	"""
	mysum = 0
	number = str(number)[::-1]
	for i,x in enumerate(number):
		if int(x) > 0:
			mysum += (2**i)
	return mysum