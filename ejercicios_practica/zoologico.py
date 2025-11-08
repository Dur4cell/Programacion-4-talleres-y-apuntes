class Animal:
    def __init__(self, nombre, edad, salud):
        self.__nombre = nombre
        self.__edad = edad
        self.__salud = salud
    
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_salud(self):
        return self.__salud

    def tipo(self):
        return "Soy un animal"
    
    def __add__(self, other):
        return self.get_edad() + other.get_edad()


class Mamifero(Animal):
    def __init__(self, nombre, edad, salud, pelaje):
        super().__init__(nombre, edad, salud)
        self.__pelaje = pelaje

    def get_pelaje(self):
        return self.__pelaje


    def tipo(self):
        return "Soy un mamífero"


class Ave(Animal):
    def __init__(self, nombre, edad, salud, alas):
        super().__init__(nombre, edad, salud)
        self.__alas = alas

    def get_alas(self):
        return self.__alas

    
    def tipo(self):
        return "Soy un ave"


# ---- Prueba ----
animales = [
    Mamifero("Simba", 5, "Buena", True),
    Ave("Piolín", 2, "Excelente", True),
    Animal("Genérico", 1, "Normal")
]

for a in animales:
    print(f"{a.get_nombre()} dice: {a.tipo()}")

print("Suma de edades:", animales[0] + animales[1]) 