from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore

init(autoreset=True)

# Little difference with the subject result because they're using 32bit floats.
def subjectTests() -> None :
	pass
def additionalsTests() :
	mat: Matrix[int] = Matrix([[1,2,3], [4,5,6], [7,8,9]])
	print(mat.transpose())

def main() :
	# print(Fore.GREEN + "Subject tests")
	# subjectTests()
	print(Fore.GREEN + "\nAdditionals tests")
	additionalsTests()
    
    
if __name__ == "__main__" :
    main()