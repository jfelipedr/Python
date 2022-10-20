#funcion filter permite filtrar con una condicion y un a lista
def numero_par(num):
    if num%2 == 0:
        return True

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = filter(numero_par, numeros)
b = list(filter(numero_par,numeros))

c = list(filter(lambda numero_par:numero_par%2 == 0, numeros))


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.cargo = cargo
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

lista_empleado=[
Empleado("sara", "director", 22540),
Empleado("pepe", "presidente",34030),
Empleado("mario", "cajero", 7400),
Empleado("ana", "secretaria", 8400),
Empleado("carlos", "pintor", 6300),
Empleado("atonio", "guia", 2100),
]

d=filter(lambda empleado:empleado.salario>15000, lista_empleado)
for empleado_salario in d:
    print(empleado_salario )

print(f'los numeros pares son: {a} \no de forma mas clara: {b} \ncon funciones lambda: {c}')

def calculo_comision(empleado):
    if empleado.salario <= 8000:
        empleado.salario *= 1.05
    return empleado
#funcino map permite filtrar con una funcion y una lista
lista_comisiones = map(calculo_comision,lista_empleado)
for empleado in lista_comisiones:
    print(f"los salarios incluyendo comisiones son: {empleado}")
