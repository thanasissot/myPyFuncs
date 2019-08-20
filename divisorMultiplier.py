	def greatestCommonDivisor(a, b):
		"""Returns Greatest common divisor of a and b"""
	while a != b:
		if a < b:
			b -= a
		elif a > b:
			a -= b
	return b

def leastCommonMultiple(a, b):
	""" Uses the Greatest common divisor function to
	return the least common multiple in integer"""
	return int(a * b / greatestCommonDivisor(a, b))