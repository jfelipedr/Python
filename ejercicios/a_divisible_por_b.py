#Ejercicio4
print("EVALUE SI 'a' ES DIVISIBLE POR 'b'")
a = int(input("Digite el numero 'a': "))
b = int(input("Digite el numero 'b': "))
c = a / b
if a % b == 0:
    print(str(a) + " es divisibles por " + str(b))
    print("El resultado es = " + str(c))
#se pueden imprimir varios valores concatenandolos con una suma pero quedan
#impresos sin espacios antes o despues de cada dato
else:
    print(str(a),"no es divisibles por",str(b))
    print("El resultado es =",str(c))