from Vector import Vector

def main() -> None :
    """entrypoint of the program"""
    v1: Vector = Vector([1, 5.0, 6])
    v2: Vector = Vector([2, 7, 5])
    invalid: Vector = Vector([7, 5])
    print(v1)
    print(v2)
    v1.add(v2)
    v1.add(5)
    v1.add(invalid)
    print(v1)
    v1.substract(v2)
    v1.substract(invalid)
    v1.substract(6)
    print(v1)
    v1.multiply(2)
    v1.multiply(v2)
    print(v1)
    
if __name__ == "__main__":
    main()

# Rajouter 