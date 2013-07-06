from utils import timer
import random

def swap(l, p, q):
	if p == q:
		return
	tmp = l[p]
	l[p] = l[q]
	l[q] = tmp

def partition(l, begin, end):
	index = begin
	pivot = l[begin]
	right_begin = begin
	right_end = begin + 1
	while right_end <= end:
		if l[right_end] <= pivot:
			right_begin = right_begin + 1
			swap(l, right_begin, right_end)
		right_end = right_end + 1
	swap(l, right_begin, index)
	return right_begin

def quick_sort(l, begin, end):
	if begin >= end:
		return
	q = partition(l, begin, end)
	print l
	print begin, end, q
	quick_sort(l, begin, q - 1)
	quick_sort(l, q + 1, end)

def tail_recursion_quick_sort(l, begin, end):
	if begin >= end:
		return
	tbegin = begin
	tend = end
	print l
	print begin, end
	while tbegin < tend:
		q = partition(l, tbegin, tend)
		tail_recursion_quick_sort(l, tbegin, q - 1)
		tbegin = q + 1


if __name__ == '__main__':
	l = [5, 6, 3, 2, 1, 7, 9, 12, 33, 11, 10, 29]
	#l = [ 3, 2]
	tail_recursion_quick_sort(l, 0, len(l) - 1)
	print l