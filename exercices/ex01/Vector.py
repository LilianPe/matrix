from typing import TypeVar, Generic, List
from colorama import init, Fore

init(autoreset=True)

K = TypeVar('K')

class Vector(Generic[K]):
	"""Vector class"""
	data: List[K]
	size: int

	def __init__(self, data:List[K]) -> None :
		"""Init the Vector"""
		self.data = data
		self.size = len(data)


	def __repr__(self) -> str:
		"""return the representation of the Vector"""
		return str(self.data)
	
	def __getitem__(self, index: int) -> K :
		"""Overload for Vector[i]"""
		return self.data[index]
	
	def __setitem__(self, index: int, value: K) -> None :
		"""Overload for Vector[i] = """
		self.data[index] = value

	def copy(self) -> 'Vector' :
		return Vector(self.data.copy())

	def display(self) -> None :
		"""display the vector and his size"""
		print(f"Vector: {self}")
		print(f"Size: {self.size}")

	def getSize(self) -> int:
		"""return the size of the vector"""
		return self.size
	
	def add(self, second:'Vector') -> bool :
		"""add another vector of same size to this one"""
		if (not isinstance(second, Vector)) :
			print(Fore.RED + "Invalid operand, not a Vector.")
			return False
		if (self.getSize() != second.getSize()):
			print(Fore.RED + f"Can't add {second}, sizes are different.")
			return False
		for i in range(0, self.getSize()):
			try:
				self[i] += second[i]
			except:
				print(Fore.RED + f"Incompatible types: {type(self[i])} and {type(second[i])}")
				return False
		return True

	def sub(self, second:'Vector') -> bool :
		"""substract another vector of same size from this one"""
		if (not isinstance(second, Vector)) :
			print(Fore.RED + "Invalid operand, not a Vector.")
			return False
		if (self.getSize() != second.getSize()):
			print(Fore.RED + f"Can't add {second}, sizes are different.")
			return False
		for i in range(0, self.getSize()):
			try:
				self[i] -= second[i]
			except:
				print(Fore.RED + f"Incompatible types: {type(self[i])} and {type(second[i])}")
				return False
		return True

	def scl(self, scalar: K) -> bool :
		"""multiply the vector by a scalar"""
		if (self.getSize() == 0) :
			return True
		for i in range(0, self.getSize()):
			try:
				self[i] *= scalar
			except:
				print(Fore.RED + f"Incompatible types: {type(self[i])} and {type(scalar)}")
				return False
		return True