def CollatzSequence(num):
	"""Returns number of times you apply division and mupltiplication 
	to reach the Collatz Sequence for a certain number : num"""
	counter = 0
	while num != 1:
		if num % 2 == 0:
			num /= 2
		else:
			num *= 3
			num += 1
		counter += 1
	return counter