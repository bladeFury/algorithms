import random

def swap(l, i, j):
	if i == j:
		return
	tmp = l[i]
	l[i] = l[j]
	l[j] = tmp

def rand_partition(l):
	llen = len(l)
	rand_index = random.randint(0, llen - 1)
	swap(l,rand_index, -1)
	pivot = l[-1]
	i = -1
	for j in range(llen - 1):
		if l[j] <= pivot:
			i = i + 1
			swap(l, i, j)
	swap(l, i + 1, -1)
	return i + 1	

def rand_select(l, i):
	"""
	select the ith biggest in l
	"""
	j = rand_partition(l)
	if j == i:
		return l[j]
	elif j > i:
		return rand_select(l[:j], i)
	else:
		return rand_select(l[j+1:], i - j - 1)

def rand_select_non_recursive(l, i):
	loop_l = l
	while(True):
		j = rand_partition(loop_l)
		if j == i:
			return loop_l[j]
		elif j > i:
			loop_l = loop_l[:j]
		else:
			loop_l = loop_l[j+1:]
			i = i - j - 1


if __name__ == '__main__':
	l = [3, 1, 2, 4, 6, 5, 7]
	print rand_select_non_recursive(l, 2)