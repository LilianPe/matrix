from typing import TypeVar, Generic, List
from colorama import init, Fore

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
