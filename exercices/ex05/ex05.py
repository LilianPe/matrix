from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore
from angle_cos import angle_cos

init(autoreset=True)

# Little difference with the subject result because they're using 32bit floats.
def subjectTests() -> None :
	u: Vector[float] = Vector([1., 0.])
	v: Vector[float] = Vector([1., 0.])
	print(angle_cos(u, v))
	u = Vector([1., 0.])
	v = Vector([0., 1.])
	print(angle_cos(u, v))
	u = Vector([-1., 1.])
	v = Vector([1., -1.])
	print(angle_cos(u, v))
	u = Vector([2., 1.])
	v = Vector([4., 2.])
	print(angle_cos(u, v))
	u = Vector([1., 2., 3.])
	v = Vector([4., 5., 6.])
	print(angle_cos(u, v))

def additionalsTests() :
	u = Vector([0., 0.])
	v = Vector([4., 2.])
	print(angle_cos(u, v))
	u = Vector([1., 2., 3])
	v = Vector([4., 5.])
	print(angle_cos(u, v))
	u = Vector([])
	v = Vector([])
	print(angle_cos(u, v))

    

def main() :
	print(Fore.GREEN + "Subject tests")
	subjectTests()
	print(Fore.GREEN + "\nAdditionals tests")
	additionalsTests()
    
    
if __name__ == "__main__" :
    main()