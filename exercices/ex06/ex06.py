from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore
from cross_product import cross_product

init(autoreset=True)

# Little difference with the subject result because they're using 32bit floats.
def subjectTests() -> None :
	u: Vector[K] = Vector([0., 0., 1.])
	v: Vector[K] = Vector([1., 0., 0.])
	print(cross_product(u, v))
	u = Vector([1., 2., 3.])
	v = Vector([4., 5., 6.])
	print(cross_product(u, v))
	u = Vector([4., 2., -3.])
	v = Vector([-2., -5., 16.])
	print(cross_product(u, v))

def additionalsTests() :
	u: Vector[K] = Vector([0., 0., 1., 1.])
	v: Vector[K] = Vector([1., 0., 0., 1.])
	print(cross_product(u, v))


def main() :
	print(Fore.GREEN + "Subject tests")
	subjectTests()
	print(Fore.GREEN + "\nAdditionals tests")
	additionalsTests()
    
    
if __name__ == "__main__" :
    main()