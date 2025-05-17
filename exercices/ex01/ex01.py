from Vector import Vector
from Matrix import Matrix, K
from typing import List
from linear_combination import linear_combination

def subjectTests() :
	e1: Vector[float] = Vector([1., 0., 0.])
	e2: Vector[float] = Vector([0., 1., 0.])
	e3: Vector[float] = Vector([0., 0., 1.])

	v1: Vector[float] = Vector([1., 2., 3.])
	v2: Vector[float] = Vector([0., 10., -100.])

	combi: Vector = linear_combination([e1, e2, e3], [10., -2., 0.5])
	combi.display()

	combi = linear_combination([v1, v2], [10., -2.])
	combi.display()

def additionalTests() :
	e1: Vector[float] = Vector([1., 0., 0.])
	e2: Vector[float] = Vector([0., 1., 0.])
	e3: Vector[float] = Vector([0., 0., 1.])
	e4: Vector[float] = Vector([0., 1])

	combi: Vector = linear_combination([e1, e2, e3], [10., -2.])
	combi= linear_combination([e1, e2, e4], [10., -2., 0.5])



def main() :
	subjectTests()
	additionalTests()

if __name__ == "__main__" :
	main()