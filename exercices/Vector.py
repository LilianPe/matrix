from typing import TypeVar, Generic, List

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
		return f"Vector: {self.data}"
	
	def __getitem__(self, index: int) -> K :
		"""Overload for Vector[i]"""
		return self.data[index]
	
	def __setitem__(self, index: int, value: K) -> None :
		"""Overload for Vector[i] = """
		self.data[index] = value
 
	def display(self) -> None :
		"""display the vector"""
		print(self)

	def getSize(self) -> int:
		"""return the size of the vector"""
		return self.size
	
	def add(self, second:'Vector[K]') -> None :
		"""add the vector in parameter to self"""
		if (not isinstance(second, Vector)) :
			print("Invalid operand, not a Vector.")
			return
		if (self.getSize() != second.getSize()):
			print(f"Can't add {second}, sizes are different.")
			return
		for i in range(0, self.getSize()):
			try:
				self[i] += second[i]
			except:
				print(f"Incompatible types: {self[i]} and {second[i]}")

	def substract(self, second:'Vector[K]') -> None :
		"""substract the vector in parameter to self"""
		if (not isinstance(second, Vector)) :
			print("Invalid operand, not a Vector.")
			return
		if (self.getSize() != second.getSize()):
			print(f"Can't add {second}, sizes are different.")
			return
		for i in range(0, self.getSize()):
			try:
				self[i] -= second[i]
			except:
				print(f"Incompatible types: {self[i]} and {second[i]}")

	def multiply(self, scalar: K) -> None :
		"""multiply the vector by the scalar in parameter, the scalar type need to be the same than data"""
		if (self.getSize == 0) :
			return
		if (not isinstance(scalar, type(self[0]))) :
			print("invalid operand, not a scalar or invalid type.")
			return
		for i in range(0, self.getSize()):
			try:
				self[i] *= scalar
			except:
				print(f"Incompatible types: {self[i]} and {scalar}")
