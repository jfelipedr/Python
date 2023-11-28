#Ejercicio5 uso de "in"
def main():
    print("Clases de 2020")
    print("Clases: Fisica - Calculo - Informática")
    clase = input("Escriba la clase escogida: ")
    clase_escogida = clase.lower()
    if clase_escogida in ("fisica","calculo","informática"):
        print("Escogió " + clase_escogida)
    else:
        print("Revise su selección")

if __name__ == '__main__':
    main()