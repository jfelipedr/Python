def evalua(nota):
    valor = "aprobado"
    if nota < 6:
        valor = "suspendido"
    return valor

def main():
    print("programa de nota obtenida")
    nota_al = input("introduzca la nota: ")

    print(evalua( int(nota_al) ))

if __name__ == '__main__':
    main()