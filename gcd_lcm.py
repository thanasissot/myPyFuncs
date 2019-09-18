from fractions import Fraction

def greatestCommonDivisor(a, b) -> int:
	"""Returns Greatest common divisor of a and b
		implementation not mine, uses recursion
		tests revealed that was 6x faster that other solution
	"""
	if a==0:
		return b
	return greatestCommonDivisor(b % a, a)


def leastCommonMultiplier(a, b) -> int:
	return int((Fraction(a) * Fraction(b)) 
			/ greatestCommonDivisor(a,b))