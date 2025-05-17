from Vector import Vector
from Matrice import Matrice
from colorama import init, Fore

init(autoreset=True)

def vectorTesting() :
    print(Fore.GREEN + "Testing Vectors:\n")
    v1: Vector[int] = Vector([1, 5.0, 6])
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

def matriceTesting() :
    print(Fore.GREEN + "Testing Matrices:\n")
    m1: Matrice = Matrice([[1, 4, 5], [4, 2, 1], [4, 2, 1], [4, 2, 1]])
    # bad: Matrice = Matrice([[1, 4, 5], [4, 4, 2, 1], [4, 2, 1], [4, 2, 1]])
    m1.display()

def main() -> None :
    """entrypoint of the program"""
    vectorTesting()
    matriceTesting()


if __name__ == "__main__":
    main()

# Enlever les protection type:
# if (type(scalar) != type(self.matrice[0][0])) :
# 			print(Fore.RED + "Invalid scalar, not the same type than the matrice elements.")
# 			return False

# Remplacer partout par des try except, et faire crash le programme plutot que juste mettre un message d'erreure