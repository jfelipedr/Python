class Persona():
    def __init__(self, nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print(f"Nombe: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.lugar_residencia}")


class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} \nAntigüedad: {self.antiguedad}")


Manuel=Empleado(1550,15,"Manuel",55,"Colombia")
Manuel.descripcion()
print(isinstance(Manuel,Persona))
