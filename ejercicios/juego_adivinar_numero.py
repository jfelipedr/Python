#Ejercicio11
import random
seguir="s"
print("juego para adivinar un numero")
while seguir=="s":
    numero_aleatorio=random.randint(0,100)
    entrada=int(input("ADIVINE UN NUMERO entre 0 y 100 "))
    while numero_aleatorio!=entrada:
        if entrada < numero_aleatorio:
            print("EL NÚMERO ES MAYOR")
            entrada=int(input("ESCRIBA OTRO NUMERO "))
        else:
            print("EL NÚMERO ES MENOR")
            entrada=int(input("ESCRIBA OTRO NUMERO "))
    print("USTED ADIVINO EL NUMERO")
    seguir=(input("DESEA SEGUIR ? s/N "))
if seguir=="n":
    print("El programa termino")
else:
    while seguir!="s" and seguir!="n":
        seguir=(input("DESEA SEGUIR ? s/N "))