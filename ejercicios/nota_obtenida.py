print("programa de nota obtenida")
nota_al=input("introduzca la nota: ")

def evalua(nota):
    valor = "aprobado"
    if nota < 5:
        valor = "suspendido"
    return valor

print(evalua(int(nota_al)))