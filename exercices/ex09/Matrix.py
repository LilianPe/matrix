from typing import TypeVar, Generic, List
from colorama import init, Fore
from Vector import Vector

init(autoreset=True)

K = TypeVar('K')

class Matrix(Generic[K]):
	matrix: List[List[K]]
	size: tuple
	def __init__(self, matrix: List[List[K]]) -> None:
		"""Matrix initialisation"""
		self.matrix = matrix
		self.size = (len(matrix), len(matrix[0])) if len(matrix) != 0 else (len(matrix), 0)
		for i, tab in enumerate(self.matrix):
			if len(tab) != self.size[1] :
				raise ValueError(f"Invalide row {i}, len is {len(tab)}, expected: {self.size[1]}")

	def __repr__(self) -> str:
		"""Return the representation of the matrix in string"""
		rep: str = ""
		for tab in self.matrix :
			rep += str(tab) + "\n"
		return rep

	def __getitem__(self, index: int) -> List[K] :
		"""Overload for matrix[i]"""
		return self.matrix[index]
	
	def __setitem__(self, index: int, value: List[K]) -> None :
		"""Overload for matrix[i] = """
		self.matrix[index] = value

	def getSize(self) -> tuple:
		"""return the size of the vector"""
		return self.size

	def copy(self) -> 'Matrix':
		return Matrix([row.copy() for row in self.matrix])


	def display(self) -> None :
		"""Display the matrix and her size"""
		print(self)
		print(self.size)
		print("\n")

	def add(self, second: 'Matrix') -> bool :
		"""add second to the matrix"""
		if (not isinstance(second, Matrix)) :
			print(Fore.RED + "Invalid operand, second is not a Matrix.")
			return False
		if (self.size != second.size) :
			print(Fore.RED + "matrix does not have the same dimensions.")
			return False
		for col in range(0, self.size[0]) :
			for row in range(0, self.size[1]) :
				try:
					self[col][row] += second[col][row]
				except:
					print(Fore.RED + f"Incompatible types: {type(self[col][row])} and {type(second[col][row])}")
		return True
	
	def sub(self, second: 'Matrix') -> bool :
		"""add second to the matrix"""
		if (not isinstance(second, Matrix)) :
			print(Fore.RED + "Invalid operand, second is not a Matrix.")
			return False
		if (self.size != second.size) :
			print(Fore.RED + "matrix does not have the same dimensions.")
			return False
		for col in range(0, self.size[0]) :
			for row in range(0, self.size[1]) :
				try:
					self[col][row] -= second[col][row]
				except:
					print(Fore.RED + f"Incompatible types: {type(self[col][row])} and {type(second[col][row])}")
		return True

	def scl(self, scalar: K) -> bool :
		"""scale the matrix with scalar"""
		for col in range(0, self.size[0]) :
			for row in range(0, self.size[1]) :
				try :
					self[col][row] *= scalar
				except :
					print(Fore.RED + f"Incompatible types: {type(self[row])} and {type(scalar)}")
					return False
		return True

	def mul_vec(self, vec: Vector[K]) -> Vector[K] :
		"""Return the result of the matrice dot by a vector vec"""
		if (not isinstance(vec, Vector)) :
			print(Fore.RED + "Invalid operand, vec is not a Vector.")
			return None
		if self.getSize()[1] != vec.getSize() :
			print(Fore.RED + f"Matrix and vec are not the same size: matrix col: {self.getSize()[1]}, vec: {vec.getSize()}.")
			return None
		vecContent: List = []
		for row in self :
			result: K = 0
			for i, n in enumerate(vec) :
				result += n * row[i]
			vecContent.append(result)
		return Vector(vecContent)

	def mul_mat(self, mat: 'Matrix[K]') -> 'Matrix[K]' :
		"""Return the result of the matrice dot by a matrix mat"""
		if (not isinstance(mat, Matrix)) :
			print(Fore.RED + "Invalid operand, mat is not a Matrix.")
			return None
		if self.getSize()[1] != mat.getSize()[0] :
			print(Fore.RED + f"Matrixes are not the same size: matrix1 col: {self.getSize()[1]}, matrix2 line: {mat.getSize()[0]}.")
			return None
		final_mat: List[List[K]] = []
		for row in self :
			new_row: List[K] = []
			for col in range(0, mat.getSize()[1]):
				result: K = 0
				for i in range(0, mat.getSize()[0]):
					result += mat[i][col] * row[i]
				new_row.append(result)
			final_mat.append(new_row)
		return Matrix(final_mat)
	
	def trace(self) -> K:
		"""Return the trace of the matrix"""
		size: tuple = self.getSize()
		if size[0] != size[1] :
			print(Fore.RED + f"Matrix is not squared: matrix line: {size[0]}, matrix col: {size[1]}.")
			return None
		trace: K = 0
		for i in range(0, size[0]) :
			trace += self[i][i]
		return trace

	def transpose(self) -> 'Matrix[K]':
		newMatrice: List[List[K]] = []
		for j in range(0, self.getSize()[1]):
			row: List[K] = []
			for i in range(0, self.getSize()[0]):
				row.append(self[i][j])
			newMatrice.append(row)
		return Matrix(newMatrice)
