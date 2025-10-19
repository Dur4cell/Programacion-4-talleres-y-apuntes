class Persona:
    def __init__(self,nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

class Paciente(Persona):
    def __init__(self, nombre, edad, dni, reg_historia_clinica):
        super().__init__(nombre, edad, dni)
        self.__reg_historia_clinica = reg_historia_clinica        