#Ejercicio7 uso de while
def main():
    print('Escriba dos numeros ("a" y "b")')
    a = float(input())
    b = float(input())
    if a <= b:
        while a <= b:
            a = a + 1
            print(str(a))
    else:
        while b <= a:
            b += 1
# el operador += suma el valor a la variable
            print(str(b))
    print(str(a), str(b))

if __name__ == '__main__':
    main()