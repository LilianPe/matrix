from Vector import Vector
from Matrix import Matrix
from colorama import init, Fore

init(autoreset=True)

def vectorTesting() :
    print(Fore.GREEN + "Testing Vectors:\n")
    v1: Vector[int] = Vector([1, 5, 6])
    v2: Vector[int] = Vector([2, 7, 5])
    invalid: Vector = Vector([7, 5])
    v1.display()
    v1.display()
    v1.add(v2)
    v1.add(5)
    v1.add(invalid)
    print(v1)
    v1.sub(v2)
    v1.sub(invalid)
    v1.sub(6)
    print(v1)
    v1.scl(2)
    v1.scl(v2)
    print(v1)
    print("\n")

def matrixTesting() :
    # init
	print(Fore.GREEN + "Testing matrixs:\n")
	m1: Matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	m2: Matrix = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
	m3: Matrix = Matrix([[8, 7], [5, 4], [2, 1]])
	# bad: Matrix = Matrix([[1, 4, 5], [4, 4, 2, 1], [4, 2, 1], [4, 2, 1]])
	print("m1:")
	m1.display()
	print("m2:")
	m2.display()
	print("m3:")
	m3.display()

	print(Fore.GREEN + "Tests add")
	m1.add(m2)
	m1.display()
	m1.add(m3)
	print(Fore.GREEN + "\nTest sub")
	m1.sub(m2)
	m1.display()
	m1.sub(m3)
	print(Fore.GREEN + "\nTest scl")
	m1.scl(2)
	m1.display()
	m1.scl(m2)

def main() -> None :
    """entrypoint of the program"""
    vectorTesting()
    matrixTesting()


if __name__ == "__main__":
    main()
