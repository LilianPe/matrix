from Vector import Vector
from Matrix import Matrix, K
from typing import List

# Linear combinaison: scale each vector with his corresponding scale, then add them together

def linear_combination(u: List[Vector], coefs: List[K]) -> Vector[K] :
    """Make a linear combinaison of all the vectors scaled by coefs"""
    scaledVectors: List[Vector] = u.copy()
    for i, coef in enumerate(coefs) :
        for vectors in scaledVectors[i] :
            vectors *= coef
    print(u)
    print(scaledVectors)
