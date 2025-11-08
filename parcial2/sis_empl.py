# Clase base Empleado: Usa encapsulamiento con atributos privados y getters/setters.
class Empleado:
    def __init__(self, nombre, id, salario_base):
        self.__nombre = nombre  # Privado
        self.__id = id  # Privado
        self.__salario_base = salario_base  # Privado
    
    # Getters y setters para encapsulamiento
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor
    
    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, valor):
        self.__salario_base = valor
    
    # Método abstracto: debe ser sobrescrito.
    def calcular_salario(self):
        raise NotImplementedError("Implementar en subclases")
    
    # Método polimórfico: muestra información.
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, ID: {self.id}, Salario Base: {self.salario_base}, Salario Calculado: {self.calcular_salario()}"

# Subclase EmpleadoTiempoCompleto: Hereda y sobrescribe. Simula sobrecarga de constructor con *args.
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id, salario_base, bono=0):
        super().__init__(nombre, id, salario_base)
        self.bono = bono  # Atributo adicional
    
    # Sobrecarga simulada: constructor alternativo con *args para flexibilidad.
    def __init_alternativo(self, *args):
        if len(args) == 4:
            super().__init__(args[0], args[1], args[2])
            self.bono = args[3]
        else:
            super().__init__(args[0], args[1], args[2])
            self.bono = 0
    
    def calcular_salario(self):
        return self.salario_base + self.bono

# Subclase EmpleadoPorHoras: Hereda y sobrescribe.
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, id, salario_base, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, id, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Subclase EmpleadoComision: Hereda y sobrescribe.
class EmpleadoComision(Empleado):
    def __init__(self, nombre, id, salario_base, ventas, porcentaje_comision):
        super().__init__(nombre, id, salario_base)
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision
    
    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.porcentaje_comision / 100)

# Demostración: Instancias y polimorfismo.
empleados = [
    EmpleadoTiempoCompleto("Ana", 124194, 3000, 500),
    EmpleadoPorHoras("Luis", 221409, 0, 40, 20),
    EmpleadoComision("Carlos", 352904, 2500, 10000, 10)
]
for emp in empleados:
    print(emp.mostrar_informacion())  # Polimorfismo: mismo método, comportamientos diferentes.