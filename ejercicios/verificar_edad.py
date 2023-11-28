#Ejercicio12
def main():
    print("VERIFICADOR DE EDAD")
    edad = input("Escriba su edad: ")
    while edad.isdigit() == False:
#isdigit evalua que la cadena de string sea un valor numerico
        print("introduzca un valor numerico")
        edad = input("Escriba su edad: ")

    if int(edad) < 18:
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")

if __name__ == '__main__':
    main()
