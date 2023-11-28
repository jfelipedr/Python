#Ejercicio8
def main():
    a1 = 0
    a2 = 0
    a3 = 0
    print("Escriba un numero de dos cifras")
    n = int(input())
    if 10 <= n <= 99:
        if 10 <= n <= 40:
            a1 += 1
        elif n >= 41 and n <= 60:
            a2 += 1
        else:
            a3 += 1
# se puede usar otro elif poniendo el intervalo de n
    else:
        print("Su número no es de dos cifras")

    print(str(a1),"numeros estan en el intervalo [10,40]")
    print(str(a2),"numeros estan en el intervalo [41,60]")
    print(str(a3),"numeros estan en el intervalo [61,99]")

if __name__ == '__main__':
    main()