import math

def main():
    print("Calcular una raiz cuadrada")
    intentos = 0
    num = float(input("introduzca un numero: "))
    while  num < 0:
        print("Este programa no calcula raices negativas, intentelo de nuevo")
        if intentos == 2:
            print("Ha incurrido en muchos errores. Finalizo el programa")
            break
#la instruccion break termina el while
        num = float(input("introduzca un numero: "))
        if num < 0:
            intentos += 1
    if intentos < 2:
        sol = math.sqrt(num)
        print(f"La raiz cuadrada de {num} es {sol}")

if __name__ == '__main__':
    main()