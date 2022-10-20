#Ejercicio9
print("Digite un año")
a = int(input())
if a % 4 == 0 and a % 100 != 0:
    print("Bisiesto")
else:
    print("Normal")