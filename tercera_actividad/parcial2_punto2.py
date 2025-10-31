from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, id_empleado, salario_base, tipo="base", **kwargs):
        # Atributos privados
        self.__nombre = nombre
        self.__id_empleado = id_empleado
        self.__salario_base = salario_base
        self.tipo = tipo  # Para simular sobrecarga
        
        # Simulación de sobrecarga: atributos adicionales según tipo
        if tipo == "por_horas":
            self.__horas_trabajadas = kwargs.get("horas_trabajadas", 0)
            self.__tarifa_por_hora = kwargs.get("tarifa_por_hora", 0)
        elif tipo == "comision":
            self.__ventas = kwargs.get("ventas", 0)
            self.__porcentaje_comision = kwargs.get("porcentaje_comision", 0)
        # Para tiempo completo, no se necesitan extras

    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def id_empleado(self):
        return self.__id_empleado

    @property
    def salario_base(self):
        return self.__salario_base

    # Setters
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and len(valor) > 0:
            self.__nombre = valor
        else:
            raise ValueError("Nombre debe ser una cadena no vacía.")

    @id_empleado.setter
    def id_empleado(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__id_empleado = valor
        else:
            raise ValueError("ID debe ser un entero positivo.")

    @salario_base.setter
    def salario_base(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__salario_base = valor
        else:
            raise ValueError("Salario base debe ser un número no negativo.")

    @abstractmethod
    def calcular_salario(self):
        pass

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre} (ID: {self.id_empleado})\nTipo: {self.tipo}\nSalario Base: {self.salario_base}\nSalario Total: {self.calcular_salario()}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, bono_anual=0):
        super().__init__(nombre, id_empleado, salario_base, tipo="tiempo_completo")
        self.__bono_anual = bono_anual

    def calcular_salario(self):
        return self.salario_base + self.__bono_anual

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, id_empleado, salario_base, tipo="por_horas", 
                         horas_trabajadas=horas_trabajadas, tarifa_por_hora=tarifa_por_hora)

    def calcular_salario(self):
        return self._Empleado__horas_trabajadas * self._Empleado__tarifa_por_hora  # Acceso a privados de la base

class EmpleadoComision(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, ventas, porcentaje_comision):
        super().__init__(nombre, id_empleado, salario_base, tipo="comision", 
                         ventas=ventas, porcentaje_comision=porcentaje_comision)

    def calcular_salario(self):
        return self.salario_base + (self._Empleado__ventas * self._Empleado__porcentaje_comision / 100)

# Demostración de polimorfismo: lista de empleados
empleados = [
    EmpleadoTiempoCompleto("Ana López", 1, 3000, bono_anual=500),
    EmpleadoPorHoras("Carlos Ruiz", 2, 0, horas_trabajadas=160, tarifa_por_hora=15),
    EmpleadoComision("María García", 3, 2500, ventas=10000, porcentaje_comision=10)
]

print("Información de empleados:")
for emp in empleados:
    print(emp.mostrar_informacion())
    print("-" * 40)