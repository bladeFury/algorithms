import random

def binary_search(search_list, search_object, compare_func):
	search_begin = 0
	search_end = len(search_list) - 1
	while search_begin <= search_end:
		middle = (search_begin + search_end) / 2
		compare_result = compare_func(search_list[middle] , search_object)
		if compare_result == 0:
			return middle
		elif compare_result > 0:
			search_end = middle - 1
		else:
			search_begin = middle + 1
	return -1

def generate_list():
	l = []
	for i in range(100):
		l.append(random.randint(0, 100))
	l.sort()
	return l

if __name__ == "__main__":
	l = generate_list()
	def compare_func(a, b):
		if (a > b):
			return 1
		elif (a < b):
			return -1
		return 0
	print binary_search(l, 4, compare_func)
	print binary_search(l, 47, compare_func)
	print binary_search(l, 44, compare_func)
	print binary_search(l, 411, compare_func)
	print binary_search(l, 42, compare_func)
	print binary_search(l, 43, compare_func)
	print binary_search(l, 44, compare_func)
