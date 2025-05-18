from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore

init(autoreset=True)

def subjectTests() -> None :
	u: Vector[float] = Vector([1., 1.])
	v: Vector[float] = Vector([0., 0.])
	print(u.dot(v))
	u = Vector([1., 1.])
	v = Vector([1., 1.])
	print(u.dot(v))
	u = Vector([-1., 6.])
	v = Vector([3., 2.])
	print(u.dot(v))

def additionalTests() -> None :
	u: Vector[float] = Vector([1., 1.])
	v: Vector[float] = Vector([0., 0., 0.])
	print(u.dot(v))
	u = Vector([1., 1.])
	v = Vector([1., 1.])
	print(u.dot("v"))
	u = Vector([-1., 6.])
	v = Vector([3., "2."])
	print(u.dot(v))

def main() :
	print(Fore.GREEN + "Subject tests")
	subjectTests()
	print(Fore.GREEN + "\nAdditionals tests")
	additionalTests()
    
    
if __name__ == "__main__" :
    main()