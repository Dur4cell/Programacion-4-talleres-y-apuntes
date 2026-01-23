from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def mostrar_descripcion(self):
        return f"Figura: {self.nombre}\nÁrea: {self.calcular_area()}\nPerímetro: {self.calcular_perimetro()}"

    # Método con sobrecarga simulada: permite calcular área con diferentes parámetros (ej. para triángulo)
    def calcular_area_con_parametros(self, *args):
        if len(args) == 1:
            # Asumiendo un cuadrado o hexágono con lado
            lado = args[0]
            return lado ** 2 if self.nombre == "Cuadrado" else (3 * math.sqrt(3) / 2) * lado ** 2
        elif len(args) == 2:
            # Para rectángulo o triángulo
            if self.nombre == "Rectangulo":
                ancho, alto = args
                return ancho * alto
            elif self.nombre == "Triangulo":
                base, altura = args
                return (base * altura) / 2
        else:
            raise ValueError("Número de parámetros no válido para esta figura.")

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        super().__init__("Rectangulo")
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        super().__init__("Triangulo")
        self.base = base
        self.altura = altura
        self.lados = [lado1, lado2, lado3]

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return sum(self.lados)

class Hexagono(Figura):
    def __init__(self, lado):
        super().__init__("Hexagono")
        self.lado = lado

    def calcular_area(self):
        return (3 * math.sqrt(3) / 2) * self.lado ** 2

    def calcular_perimetro(self):
        return 6 * self.lado

# Demostración de polimorfismo: lista de figuras y recorrido
figuras = [
    Cuadrado(5),
    Rectangulo(4, 6),
    Triangulo(3, 4, 3, 4, 5),
    Hexagono(7)
]

print("Información de las figuras:")
for figura in figuras:
    print(figura.mostrar_descripcion())
    print("-" * 30)

# Ejemplo de sobrecarga simulada
cuadrado = Cuadrado(5)
print("Área del cuadrado usando sobrecarga simulada:", cuadrado.calcular_area_con_parametros(5))