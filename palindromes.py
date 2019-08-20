def Palindromes(sentence):
	""" returns a boolean that checks if the string entered
	is a palindrome, ignores numbers spaces punctuation 
	and case in string"""
	temp = ''
	sentence = sentence.lower()
	for letter in sentence:
		if letter.isalpha():
			temp = ''.join([temp, letter])

	return temp[:len(temp)//2+1] == temp[:len(temp)//2 - 1:-1]