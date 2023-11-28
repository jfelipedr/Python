#Ejercicio 2
def main():
    print("Verifique si un numero es par")
    a = int(input("Digite un numero: "))
    b = a%2
    if b == 0:
        print(str(a), "es un numero par")
    else:
        print(str(a), "es un numero impar")

if __name__ == '__main__':
    main()