def area(base,altura):
    return base*altura/2

base1=float(input("Base del triangulo 1: "))
altura1=float(input("Altura del triangulo 1: "))

print(area(base1,altura1))

#funciones lambda permiten simplidicar funciones, por ejemplo al calculo de un area
area2=lambda base,altura:base*altura/2

base2=float(input("Base del triangulo 2: "))
altura2=float(input("Altura del triangulo 2: "))
print(area2(base2,altura2))
