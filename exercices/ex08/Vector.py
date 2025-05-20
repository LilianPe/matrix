from typing import TypeVar, Generic, List
from colorama import init, Fore
from math import sqrt

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

	# Dot product = Produit scalaire -> u·v = u[0] * v[0] + u[1] * v[1] ect...
	def dot(self, v: 'Vector[K]') -> K :
		"""Return the dot product of this vector and v"""
		if (not isinstance(v, Vector)) :
			print(Fore.RED + "Invalid operand, not a Vector.")
			return None
		if (self.getSize() != v.getSize()):
			print(Fore.RED + f"Can't make the dot product with v: {v}, sizes are different.")
			return None
		result: K = 0
		for i in range(0, self.getSize()) :
			try :
				result += self[i] * v[i]
			except:
				print(Fore.RED + f"Error: invalids types. Can't calculate with {type(self[i])} and {type(v[i])}.")
				return None
		return result

	def norm_1(self) -> float :
		result: int = 0
		for n in self.data :
			result += abs(n)
		return float(result)
	
	# Triangle inequality : ∥u+v∥≤∥u∥+∥v∥
	# Norm of vector(u + v) is shorter than norm(u) + norm(v)
	def norm(self) -> float :
		result: int = 0
		for n in self.data :
			result += n ** 2
		# return float(sqrt(result)) ?? Using pow because sqrt is forbidden, pow(n, 0.5) == sqrt(n)
		return float(pow(result, 0.5))

	def norm_inf(self) -> float :
		absData : List[K] = [abs(n) for n in self.data]
		return(float(max(absData)))

	def isNull(self) -> bool :
		for n in self :
			if n != 0 :
				return False
		return True