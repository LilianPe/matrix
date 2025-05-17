from Vector import Vector
from Matrix import Matrix, K
from typing import List
from lerp import lerp

def subjectTests() -> None :
	result = lerp(0, 1, 0.5)
	print(result)
	result = lerp(21., 42., 0.3)
	print(result)
	result = lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)
	print(result)
	result = lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5)
	print(result)

def additionalTests() -> None :
	result = lerp("test", 2, 0)
	result = lerp("test", "2", 0.)
	result = lerp(0, 2, 5)
	result = lerp(Vector([1, 2, 3]), Vector([1, 2]), 1)
	result = lerp(Matrix([[1, 2, 3], [4, 5, 6]]), Matrix([[1, 2]]), 1)


def main() :
    subjectTests()
    additionalTests()
    
    
if __name__ == "__main__" :
    main()