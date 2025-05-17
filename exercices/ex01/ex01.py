from Vector import Vector
from Matrix import Matrix, K
from typing import List
from linear_combination import linear_combination

e1: Vector[float] = Vector([1., 0., 0.])
e2: Vector[float] = Vector([0., 1., 0.])
e3: Vector[float] = Vector([0., 0., 1.])

v1: Vector[float] = Vector([1., 2., 3.])
v1: Vector[float] = Vector([0., 10., -100.])

linear_combination([e1, e2, e3], [10., -2., 0.5])