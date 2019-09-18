def kthDigit(a, b, k):
	"""return the Kth Digit from right of a**b"""
	return ((a ** b) % (10 ** k)) // (10 ** (k - 1))