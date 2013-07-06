import utils

def counting_sort(l, k):
	llen = len(l)
	result = [0] * llen
	counting_array = [0] * k
	for i in range(llen):
		counting_array[l[i]] = counting_array[l[i]] + 1
	for j in range(1, k):
		counting_array[j] = counting_array[j - 1] + counting_array[j]
	for m in reversed(range(llen)):
		result[counting_array[l[m]] - 1] = l[m]
		counting_array[l[m]] = counting_array[l[m]] - 1
	return result

def radix_sort(l):
	pass

if __name__ == '__main__':
	ll = [12, 3, 43, 53, 12, 32, 42, 21, 23, 76, 42, 17, 44]
	print ll
	print counting_sort(ll, 77)

