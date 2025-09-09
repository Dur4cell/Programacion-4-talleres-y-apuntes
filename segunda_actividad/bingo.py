import random

class Bingo:
    def __init__(self, palabra="BINGO", max_num=75):
        # Validaciones
        if len(palabra) != 5 or len(set(palabra)) != 5:
            raise ValueError("La palabra debe tener 5 letras sin repetir.")
        if max_num < 50 or max_num > 90 or max_num % 5 != 0:
            raise ValueError("El número máximo debe estar entre 50 y 90 y ser múltiplo de 5.")
        
        self.palabra = palabra.upper()
        self.max_num = max_num
        self.tamano = len(palabra)  # siempre 5
    
    def generar_tarjeta(self):
        """Genera una tarjeta de Bingo válida según los parámetros"""
        tarjeta = {letra: [] for letra in self.palabra}
        
        rango_columna = self.max_num // self.tamano
        
        for i, letra in enumerate(self.palabra):
            inicio = i * rango_columna + 1
            fin = (i + 1) * rango_columna
            numeros = random.sample(range(inicio, fin + 1), self.tamano)
            tarjeta[letra] = numeros
        
        return tarjeta
    
    def mostrar_tarjeta(self, tarjeta):
        """Imprime la tarjeta en formato tabular"""
        print(" ".join([f"{l:^5}" for l in self.palabra]))
        for fila in range(self.tamano):
            for letra in self.palabra:
                print(f"{tarjeta[letra][fila]:^5}", end=" ")
            print()

# Ejemplo de uso
if __name__ == "__main__":
    juego = Bingo("BINGO", 90)  # se puede cambiar palabra y número máximo
    tarjeta = juego.generar_tarjeta()
    juego.mostrar_tarjeta(tarjeta)
