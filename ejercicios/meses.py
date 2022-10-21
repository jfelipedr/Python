#Ejercicio10
def seleccionar_mes(a):
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    if (a<1 or a>12):
        mensaje = print("Revise su entrada")
    else:
        mensaje =  print(f"el mes que selecciono es: {meses[a-1]}")

    return mensaje

def main ():
    print("Digite el numero de un mes")
    entrada = int( input() )
    seleccionar_mes(entrada)

if __name__ == '__main__':
    main()

"""def seleccionar_mes(a):
    if 1 <= a <= 12:
        if a == 1:
            nmes = "enero"
        elif a == 2:
            nmes = "febrero"
        elif a == 3:
            nmes = "marzo"
        elif a == 4:
            nmes = "abril"
        elif a == 5:
            nmes = "mayo"
        elif a == 6:
            nmes = "junio"
        elif a == 7:
            nmes = "julio"
        elif a == 8:
            nmes = "agosto"
        elif a == 9:
            nmes = "septiembre"
        elif a == 10:
            nmes = "octubre"
        elif a == 11:
            nmes = "noviembre"
        else:
            nmes = "diciembre"
        mensaje = print(f"el mes que selecciono es: {nmes}")
    else:
        mensaje = print("Revise su entrada")
        
    return mensaje"""