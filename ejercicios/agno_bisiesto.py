#Ejercicio9
def  main():
    print("Digite un año ",end='')
    a = int(input())
    if a % 4 == 0 and a % 100 != 0:
        print("El año es bisiesto")
    else:
        print("El año es normal")

if __name__ == '__main__':
    main()