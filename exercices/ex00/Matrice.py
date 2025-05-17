from typing import TypeVar, Generic, List
from colorama import init, Fore

init(autoreset=True)

K = TypeVar('K')

class Matrice(Generic[K]):
	matrice: List[List[K]]
	size: tuple
	def __init__(self, matrice: List[List[K]]) -> None:
		"""Matrice initialisation"""
		self.matrice = matrice
		self.size = (len(matrice), len(matrice[0])) if len(matrice) != 0 else (len(matrice), 0)
		for i, tab in enumerate(self.matrice):
			if len(tab) != self.size[1] :
				raise ValueError(f"Invalide row {i}, len is {len(tab)}, expected: {self.size[1]}")

	def __repr__(self) -> str:
		"""Return the representation of the matrice in string"""
		rep: str = ""
		for tab in self.matrice :
			rep += str(tab) + "\n"
		return rep

	def __getitem__(self, index: int) -> List[K] :
		"""Overload for Matrice[i]"""
		return self.matrice[index]
	
	def __setitem__(self, index: int, value: List[K]) -> None :
		"""Overload for Matrice[i] = """
		self.matrice[index] = value

	def display(self) -> None :
		"""Display the matrice and her size"""
		print(self)
		print(self.size)

	def add(self, second: 'Matrice') -> bool :
		"""add second to the matrice"""
		if (not isinstance(second, Matrice)) :
			print(Fore.RED + "Invalid operand, second is not a matrice.")
			return False
		if (self.size != second.size) :
			print(Fore.RED + "Matrice does not have the same dimensions.")
			return False
		for col in range(0, self.size[0]) :
			for row in range(0, self.size[1]) :
				self.matrice[col][row] += second[col][row]
		return True
	
	def sub(self, second: 'Matrice') -> bool :
		"""add second to the matrice"""
		if (not isinstance(second, Matrice)) :
			print(Fore.RED + "Invalid operand, second is not a matrice.")
			return False
		if (self.size != second.size) :
			print(Fore.RED + "Matrice does not have the same dimensions.")
			return False
		for col in range(0, self.size[0]) :
			for row in range(0, self.size[1]) :
				self.matrice[col][row] -= second[col][row]
		return True

	def sub(self, scalar: K) -> bool :
		"""scale the matrice with scalar"""
		if (type(scalar) != type(self.matrice[0][0])) :
			print(Fore.RED + "Invalid scalar, not the same type than the matrice elements.")
			return False
		for col in range(0, self.size[0]) :
			for row in range(0, self.size[1]) :
				self.matrice[col][row] *= scalar
		return True
