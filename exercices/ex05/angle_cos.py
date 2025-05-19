from Vector import Vector
from Matrix import Matrix, K
from typing import List, TypeVar
from colorama import init, Fore

# cos can be calculate with this formula: ( (u⋅v) / (∥u∥⋅∥v∥) )
def angle_cos(u: Vector[K], v: Vector[K]) -> float :
    if (u.isNull() or v.isNull() or u.getSize() != v.getSize()) :
        return None
    return float(u.dot(v) / (u.norm() * v.norm()))