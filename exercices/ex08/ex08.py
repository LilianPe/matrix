from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore

init(autoreset=True)

# Little difference with the subject result because they're using 32bit floats.
def subjectTests() -> None :
	u: Matrix[K] = Matrix([[1., 0.], [0., 1.]])
	print(u.trace())
	u = Matrix([[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.]])
	print(u.trace())
	u = Matrix([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.]])
	print(u.trace())

def additionalsTests() :
	u = Matrix([[-2., -8.],[1., -23.],[0., 4.]])
	print(u.trace())

def main() :
	print(Fore.GREEN + "Subject tests")
	subjectTests()
	print(Fore.GREEN + "\nAdditionals tests")
	additionalsTests()
    
    
if __name__ == "__main__" :
    main()