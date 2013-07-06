from utils import timer

@timer
def fibonacci(n):
	return raw_fibonacci(n)

def raw_fibonacci(n):
	if n == 1 or n == 0:
		return 1
	return raw_fibonacci(n - 1) + raw_fibonacci(n - 2)

@timer
def bottomup_fibonacci(n):
	i = 0
	j = 1
	fi = 1
	fj = 1
	while j < n:
		i = j
		j = j + 1
		tmp = fj
		fj = fj + fi
		fi = tmp
	return fj

class matrix22:
	def __init__(self, a00, a01, a10, a11):
		self.a00 = a00
		self.a01 = a01
		self.a10 = a10
		self.a11 = a11
	def multiply(self, another_matrix):
		
		a00 = self.a00 * another_matrix.a00 + self.a01 * another_matrix.a10
		a01 = self.a00 * another_matrix.a01 + self.a01 * another_matrix.a11
		a10 = self.a10 * another_matrix.a00 + self.a11 * another_matrix.a10
		a11 = self.a10 * another_matrix.a01 + self.a11 * another_matrix.a11

		self.a00 = a00
		self.a01 = a01
		self.a10 = a10
		self.a11 = a11
		return self

@timer
def recursive_squaring_fibonacci(n):
	m = matrixn(n)
	return m.a00

def matrixn(n):
	if n == 1:
		return matrix22(1, 1, 1, 0)
	if n % 2 == 0:
		m = matrixn(n/2)
		return m.multiply(m)
	else:
		m = matrixn(n/2)
		return m.multiply(m).multiply(matrix22(1, 1, 1, 0))

if __name__ == '__main__':
	n = 600
	#print fibonacci(n)
	print bottomup_fibonacci(n)
	print recursive_squaring_fibonacci(n)