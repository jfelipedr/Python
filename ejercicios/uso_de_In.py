#Ejercicio5 uso de "in"
print("Clases de 2020")
print("Clases: Fisica - Calculo - Informática")
clase = input("Escriba la clase escogida: ")
clase_escogida = clase.lower()
if clase_escogida in ("fisica","calculo","informática"):
    print("Escogio " + clase_escogida)
else:
    print("Revise su seleccion")