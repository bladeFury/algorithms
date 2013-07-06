
def merge(left, right):
	lleft = len(left)
	lright = len(right)
	result = []
	i = j = 0
	while i < lleft and j < lright:
		if left[i] < right[j]:
			result.append(left[i])
			i = i + 1
		else:
			result.append(right[j])
			j = j + 1
	if i == lleft:
		result = result + right[j:]
	elif j == lright:
		result = result + left[i:]
	return result

def merge_sort(l):
	length = len(l)
	if length == 1:
		return l
	print length
	left = merge_sort(l[:length/2])
	right = merge_sort(l[length/2:])
	return merge(left, right)

if __name__ == '__main__':
	ll = [12, 3, 43, 53, 12, 32, 42, 21, 23, 76, 425, 17, 44]
	print ll
	print merge_sort(ll)