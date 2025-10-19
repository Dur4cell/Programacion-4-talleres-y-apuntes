class Persona:
    def __init__(self,nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

class Paciente(Persona):
    def __init__(self, nombre, edad, dni, reg_historia_clinica):
        super().__init__(nombre, edad, dni)
        self.__reg_historia_clinica = reg_historia_clinica     

    def quejarse(self):
        return "¡Me siento mal!"
    
class Doctor(Persona):
    def __init__(self, nombre, edad, dni, especialidad):
        super().__init__(nombre, edad, dni)
        self.__especialidad = especialidad

    def diagnosticar(self):
        return "Después de examinarte, te recetaré un acetaminofén."
    def crear_historia_clinica(self, paciente, historia):
        pass
    
class historia_clinica:
    def __init__(self):
        self.__registros = []

    def agregar_registro(self, registro):
        self.__registros.append(registro)

    def obtener_registros(self):
        return self.__registros