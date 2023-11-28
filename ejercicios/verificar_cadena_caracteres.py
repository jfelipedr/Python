def main():
    print("Verificacion de correo")
    veridicador = 0
    email = input("introduzca su email: ")
    for i in email:
        if i == "@" or i == ".":
            veridicador += 1
    if veridicador == 2:
        print("email correcto")
    else:
        print("email incorrecto")

    print("Otra forma de Verificacion")
    valido = False
    email = input("introduzca su email: ")
    for i in range(len(email)):
# len da la longitud de email, osea todos los caracteres ingresados incluyendo espacios
#range hace que se lean todos los caracteres menos uno, osea el ultimo
        if email[i] == "@":
# email[i] indica que si email de i, depende del rango de arriba y la lectura de los caracteres
            valido = True
    if valido:
# al escribir solo valido indica que si valido es = a True continue el if
        print("email correcto")
    else:
        print("email incorrecto")

if __name__ == '__main__':
    main()