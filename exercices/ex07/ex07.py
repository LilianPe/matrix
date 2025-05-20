from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore

init(autoreset=True)

# Little difference with the subject result because they're using 32bit floats.
def subjectTests() -> None :
	print(Fore.GREEN + "mul_vec:")
	u: Matrix[float] = Matrix([[1., 0.,], [0., 1.]])
	v: Vector[float] = Vector([4., 2.])
	print(u.mul_vec(v))
	u = Matrix([[2., 0.,], [0., 2.]])
	v = Vector([4., 2.])
	print(u.mul_vec(v))
	u = Matrix([[2., -2.,], [-2., 2.]])
	v = Vector([4., 2.])
	print(u.mul_vec(v))
	print(Fore.GREEN + "\nmul_mat:")
	print("\n____________________________\n\n")
	u = Matrix([[1., 0.,], [0., 1.]])
	v: Matrix[float] = Matrix([[1., 0.], [0., 1.]])
	print(u.mul_mat(v))
	print("____________________________")
	print("\n____________________________\n\n")
	u = Matrix([[1., 0.,], [0., 1.]])
	v: Matrix[float] = Matrix([[2., 1.], [4., 2.]])
	print(u.mul_mat(v))
	print("____________________________")
	print("\n____________________________\n\n")
	u = Matrix([[3., -5.,], [6., 8.]])
	v: Matrix[float] = Matrix([[2., 1.], [4., 2.]])
	print(u.mul_mat(v))
	print("____________________________")

def additionalsTests() :
	print(Fore.GREEN + "mul_vec:")
	u: Matrix[float] = Matrix([[1., 0.,], [0., 1.]])
	v: Vector[float] = Vector([4., 2., 6.])
	print(u.mul_vec(v))
	u = Matrix([[2., 0.,], [0., 2.]])
	v = Vector([4., 2.])
	print(u.mul_vec("v"))
	u = Matrix([[1., 0.,], [0., 1.]])
	v: Matrix[float] = Matrix([[1., 0., 1.], [0., 1., 0.]])
	print(u.mul_mat(v))
	u = Matrix([[1., 0.,], [0., 1.]])
	v: Matrix[float] = Matrix([[1., 0.], [0., 1.], [1., 0.]])
	print(u.mul_mat(v))
	u = Matrix([[1., 0.,], [0., 1.]])
	v = Vector([4., 2.])
	print(u.mul_mat(v))

def main() :
	print(Fore.GREEN + "Subject tests")
	subjectTests()
	print(Fore.GREEN + "\nAdditionals tests")
	additionalsTests()
    
    
if __name__ == "__main__" :
    main()