#Ejercicio3 comparacion
def main ():
    print("Evalue cual numero es mayor")
    a = int(input("Digite un numero a: "))
    b = int(input("Digite otro numero b: "))
    if a == b:
        print(str(a), "es igual que", str(b))
    #al separar con comas se crea un espacio antes y despues
    else:
        if a > b:
            print(str(a), "es mayor que", str(b))
        else:
            print(str(a), "es menor que", str(b))

if __name__ == '__main__':
    main()