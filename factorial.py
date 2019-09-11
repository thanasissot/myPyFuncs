def factorial(num):
	"""Returns the factorial of num
	"""
    if num == 1:
        return 1
    return num * factorial(num-1)