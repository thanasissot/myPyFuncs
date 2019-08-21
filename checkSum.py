def checkSum(list):
	res = 0
	for x in list:
		res += x
		res *= 113
		res %= 10000007
	return res