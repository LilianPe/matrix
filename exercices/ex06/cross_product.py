from Vector import Vector
from Matrix import Matrix, K
from typing import List, TypeVar
from colorama import init, Fore

def cross_product(u: Vector[K], v: Vector[K]) -> Vector[K] :
    if (u.getSize() != 3 or v.getSize() != 3) :
        return None
    result: Vector[K] = Vector([u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]])
    return result