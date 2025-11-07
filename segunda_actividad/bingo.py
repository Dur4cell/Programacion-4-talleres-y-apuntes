import random

class Bingo:
    def __init__(self, palabra="BINGO", max_num=75):
        # Validaciones:
        # 1. La palabra debe tener exactamente 5 letras distintas
        if len(palabra) != 5 or len(set(palabra)) != 5:
            raise ValueError("La palabra debe tener 5 letras sin repetir.")
        
        # 2. El número máximo debe estar entre 50 y 90 y ser múltiplo de 5
        if max_num < 50 or max_num > 90 or max_num % 5 != 0:
            raise ValueError("El número máximo debe estar entre 50 y 90 y ser múltiplo de 5.")
        
        # Guardamos atributos en el objeto
        self._palabra = palabra.upper()   # La palabra del juego (ej: BINGO, PLENO)
        self._max_num = max_num           # Número máximo permitido
        self._tamano = len(palabra)       # Tamaño de la palabra (siempre 5)
    
    def generar_tarjeta(self):
        """
        Genera una tarjeta aleatoria de bingo según:
        - La palabra (5 columnas, una por letra).
        - El número máximo elegido.
        """
        
        # Diccionario donde cada letra tendrá su lista de números
        tarjeta = {letra: [] for letra in self._palabra}
        
        # Rango de números por cada columna
        # Ejemplo: si max_num = 90 → cada columna cubre 18 números
        rango_columna = self._max_num // self._tamano
        
        # Generamos los números para cada columna
        for i, letra in enumerate(self._palabra):
            # Calculamos el inicio y fin del rango de esta columna
            inicio = i * rango_columna + 1
            fin = (i + 1) * rango_columna
            
            # Tomamos 'tamano' (5) números aleatorios del rango sin repetición
            numeros = random.sample(range(inicio, fin + 1), self._tamano)
            
            # Guardamos los números en la columna correspondiente
            tarjeta[letra] = numeros
        
        return tarjeta
    
    def mostrar_tarjeta(self, tarjeta):
        """
        Imprime la tarjeta en formato tabular (5x5).
        """
        
        # Encabezado con las letras de la palabra
        print(" ".join([f"{l:^5}" for l in self._palabra]))
        
        # Imprimir fila por fila
        for fila in range(self._tamano):
            for letra in self._palabra:
                print(f"{tarjeta[letra][fila]:^5}", end=" ")
            print()  # salto de línea al final de cada fila


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un juego con la palabra "PLENO" y máximo = 90
    juego = Bingo("BINGO", 90)
    
    # Generar la tarjeta
    tarjeta = juego.generar_tarjeta()
    
    # Mostrar la tarjeta en pantalla
    juego.mostrar_tarjeta(tarjeta)