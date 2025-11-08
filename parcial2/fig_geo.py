# Clase base Figura: Define atributos comunes y métodos abstractos para área y perímetro.
# Usamos herencia para que las subclases hereden y sobrescriban los métodos.
class Figura:
    def __init__(self, tipo):
        self.tipo = tipo  # Atributo común: tipo de figura
    
    # Método abstracto: debe ser sobrescrito en subclases. Calcula el área.
    def calcular_area(self):
        raise NotImplementedError("Este método debe ser implementado en subclases")
    
    # Método abstracto: debe ser sobrescrito en subclases. Calcula el perímetro.
    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser implementado en subclases")
    
    # Método para mostrar descripción: usa polimorfismo al ser llamado en cualquier subclase.
    def mostrar_descripcion(self):
        return f"Tipo: {self.tipo}, Área: {self.calcular_area()}, Perímetro: {self.calcular_perimetro()}"

# Subclase Cuadrado: Hereda de Figura y sobrescribe métodos. Simula sobrecarga con un método adicional.
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado
    
    # Sobrecarga simulada: método alternativo para calcular área con lado opcional (usando *args).
    def calcular_area_con_parametro(self, *args):
        if args:
            lado = args[0]
            return lado ** 2
        return self.calcular_area()

# Subclase Rectangulo: Hereda y sobrescribe.
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

# Subclase Triangulo: Hereda y sobrescribe (asumiendo triángulo equilátero para simplicidad).
class Triangulo(Figura):
    def __init__(self, lado):
        super().__init__("Triángulo")
        self.lado = lado
    
    def calcular_area(self):
        # Área de triángulo equilátero: (sqrt(3)/4) * lado^2
        import math
        return (math.sqrt(3) / 4) * (self.lado ** 2)
    
    def calcular_perimetro(self):
        return 3 * self.lado

# Subclase Hexagono: Hereda y sobrescribe (hexágono regular).
class Hexagono(Figura):
    def __init__(self, lado):
        super().__init__("Hexágono")
        self.lado = lado
    
    def calcular_area(self):
        # Área de hexágono regular: (3 * sqrt(3) / 2) * lado^2
        import math
        return (3 * math.sqrt(3) / 2) * (self.lado ** 2)
    
    def calcular_perimetro(self):
        return 6 * self.lado

# Demostración de polimorfismo: Lista de figuras, recorre y llama métodos sobrescritos.
figuras = [Cuadrado(5), Rectangulo(4, 6), Triangulo(3), Hexagono(2)]
for figura in figuras:
    print(figura.mostrar_descripcion())  # Polimorfismo: mismo método, comportamiento diferente.