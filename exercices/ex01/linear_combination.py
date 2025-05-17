from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore

init(autoreset=True)

# Linear combinaison: scale each vector with his corresponding scale, then add them together

def linear_combination(u: List[Vector], coefs: List[K]) -> Vector[K] :
	"""Make a linear combinaison of all the vectors scaled by coefs"""
	if (len(u) != len(coefs)) :
		print(Fore.RED + "Size of the arrays are different.")
		return None
	if (len(u) == 0) :
		return Vector([])
	size: int = u[0].getSize()
	for v in u :
		if (v.getSize() != size) :
			print(Fore.RED + "Vectors have different sizes.")
			return None
	scaledVectors: List[Vector[K]] = [vector.copy() for vector in u]
	for i, coef in enumerate(coefs) :
		scaledVectors[i].scl(coef)
	finalVector: Vector[K] = scaledVectors[0]
	for i in range(1, len(scaledVectors)) :
		finalVector.add(scaledVectors[i])
	return finalVector
