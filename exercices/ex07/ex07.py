from Vector import Vector
from Matrix import Matrix, K
from typing import List
from colorama import init, Fore

init(autoreset=True)

# Little difference with the subject result because they're using 32bit floats.
# An interpretation of multiplying vector by matrice is transforming space
# The 2x2 matrice is the vectors i, j of the span
# And multiplying a vector by this matrice give back th vector in the span represented by theses vectors i and j
# See the example below in additionals tests

# Then, multiplying two matrices is equivalent to multiplying the vectors i, j of the second matrice (for a 2x2 matrice) by the first matrice
# It is like applying first a transformation of the span with the second matrice, then a transformation with the first
# The returned matrice apply the two transformation

def subjectTests() -> None :
	print(Fore.GREEN + "mul_vec:")
	u: Matrix[float] = Matrix([[1., 0.,], 
                               [0., 1.]])
	v: Vector[float] = Vector([4., 2.])
	print(u.mul_vec(v))
	u = Matrix([[2., 0.,], [0., 2.]])
	v = Vector([4., 2.])
	print(u.mul_vec(v))
	u = Matrix([[2., -2.,], 
             	[-2., 2.]])
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
	u = Matrix([[3., -5.,], 				# multiplying [2, 4], then [1, 2] by u
             	[6., 8.]])					# 2[3, 6] + 4[-5, 8] = [6, 12] + [-20, 32] = [-14, 44]
	v: Matrix[float] = Matrix([[2., 1.], 	# 1[3, 6] + 2[-5, 8] = [3, 6] + [-10, 16] = [-7, 22]
                               [4., 2.]])
	print(u.mul_mat(v))
	print("____________________________")


def additionalsTests() :
	print(Fore.GREEN + "mul_vec:")
	u = Matrix([[1., 2.,],  # 4[1, 3] + 2[2, 4] = [4, 12] + [4, 8] = [8, 20]
             	[3., 4.]])
	v = Vector([4., 2.])
	print(u.mul_vec(v))
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