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

	def __add__(self, other: 'Vector') -> None:
		"""Overload of operator + between two vector"""
		self.add(other)

	def __sub__(self, other: 'Vector') -> None:
		"""Overload of operator - between two vector"""
		self.sub(other)

	def __mul__(self, other: K) -> None:
		"""Overload of operator * between two vector"""
		self.scl(other)

	def display(self) -> None :
		"""display the vector and his size"""
		print(f"Vector: {self}")
		print(f"Size: {self.size}")

	def getSize(self) -> int:
		"""return the size of the vector"""
		return self.size
	
	def add(self, second:'Vector') -> bool :
		"""add second to self"""
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
				print(f"Incompatible types: {self[i]} and {second[i]}")
		return True

	def sub(self, second:'Vector') -> bool :
		"""substract second from self"""
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
				print(f"Incompatible types: {self[i]} and {second[i]}")
		return True

	def scl(self, scalar: K) -> bool :
		"""multiply the vector by scalar, the scalar type need to be the same than data"""
		if (self.getSize == 0) :
			return True
		if (not isinstance(scalar, type(self[0]))) :
			print(Fore.RED + "invalid operand, not a scalar or invalid type.")
			return False
		for i in range(0, self.getSize()):
			try:
				self[i] *= scalar
			except:
				print(f"Incompatible types: {self[i]} and {scalar}")
		return True