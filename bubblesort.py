def bubbleSort(list):
	"""Uses BubbleSort to sort the list and also keeps track of the 
	number of passes through the list and the number of swaps of elements"""
	passes = swaps = 0
	for x in range(len(list)-1):
		rounds = False
		for y in range(len(list)-1-x):
			if list[y] > list[y + 1]:
				temp = list[y]
				list[y] = list[y + 1]
				list[y + 1] = temp
				swaps += 1
				rounds = True
		if rounds:
			passes += 1
	return passes + 1, swaps