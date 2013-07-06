import time

def timer(func):
	def wrapper(*args):
		start = time.clock()
		result = func(*args)
		print "%s%s costs %f " % (func.__name__, args, time.clock() - start)
		return result
	return wrapper