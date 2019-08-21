def time(seconds):
	""" takes input as integer seconds and returns a tuple
	of integers, days, hours, minures and the remainder seconds"""
	day = seconds // (3600 * 24)
	seconds -= (day * (3600 * 24))
	hour =  seconds // 3600
	seconds -= (hour * 3600)
	minute = (seconds // 60)
	seconds -= (minute * 60)
	return day, hour, minute, seconds