from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore

init(autoreset=True)

def subjectTests() -> None :
	u: Vector = Vector([0., 0., 0.])
	print(u.norm_1(), u.norm(), u.norm_inf())
	u = Vector([1., 2., 3.])
	print(u.norm_1(), u.norm(), u.norm_inf())
	u = Vector([-1., -2.])
	print(u.norm_1(), u.norm(), u.norm_inf())

def main() :
	print(Fore.GREEN + "Subject tests")
	subjectTests()
    
    
if __name__ == "__main__" :
    main()