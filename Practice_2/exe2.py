class Matrix:
	def __init__(self, *args):
		self.matrix = []
		for var in args:
			self.matrix.append(var)
	def print_matrix(self):
		for var in self.matrix:
			for item in var:
				print(item, end= " ")
			print()
	def det2(self):
		return (self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0])
	
	def minor(self, i, j):
		tmp = [row for k, row in enumerate(self.matrix) if k != i]
		tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
		print(tmp)
		return tmp
 
	def determinant(self):
		size = len(self.matrix)
		print()
		self.print_matrix()
		ret = 0
		if size == 2:
			return self.det2
		for j in range(size):
			matrix = Matrix(self.minor(0, j))
			ret += (-1) ** j * self.matrix[0][j] * matrix.determinant()
		return ret

ob = Matrix([1, 2, 3], [2, 3, 1], [2, 1, 4])
ob.print_matrix()
print(ob.determinant())