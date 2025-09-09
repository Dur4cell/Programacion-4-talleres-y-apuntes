class Calculadora:
    def __init__(self):
        self.historial = []
    
    def suma(self, a, b):
        resultado = a + b
        self._agregar_al_historial(a, b, '+', resultado)
        return resultado
    
    def resta(self, a, b):
        resultado = a - b
        self._agregar_al_historial(a, b, '-', resultado)
        return resultado
    
    def multiplicacion(self, a, b):
        resultado = a * b
        self._agregar_al_historial(a, b, '*', resultado)
        return resultado
    
    def division(self, a, b):
        if b != 0:
            resultado = a / b
            self._agregar_al_historial(a, b, '/', resultado)
            return resultado
        else:
            error = "Error: División por cero"
            self._agregar_al_historial(a, b, '/', error)
            return error
    
    def _agregar_al_historial(self, a, b, operador, resultado):
        """Método privado para agregar operaciones al historial"""
        operacion = {
            'operando1': a,
            'operando2': b,
            'operador': operador,
            'resultado': resultado
        }
        self.historial.append(operacion)
    
    def realizar_operacion(self, a, b, operador):
        """Realiza una operación basada en el operador proporcionado"""
        if operador == "+":
            return self.suma(a, b)
        elif operador == "-":
            return self.resta(a, b)
        elif operador == "*":
            return self.multiplicacion(a, b)
        elif operador == "/":
            return self.division(a, b)
        else:
            return "Operador no válido"
    
    def mostrar_historial(self):
        """Muestra el historial de operaciones realizadas"""
        if not self.historial:
            print("No hay operaciones en el historial")
            return
        
        print("\n--- Historial de Operaciones ---")
        for i, operacion in enumerate(self.historial, 1):
            print(f"{i}. {operacion['operando1']} {operacion['operador']} "
                  f"{operacion['operando2']} = {operacion['resultado']}")
    
    def limpiar_historial(self):
        """Limpia el historial de operaciones"""
        self.historial.clear()
        print("Historial limpiado")


class InterfazCalculadora:
    def __init__(self):
        self.calculadora = Calculadora()
    
    def obtener_datos(self):
        """Obtiene los datos del usuario"""
        try:
            operando1 = float(input("Introduce el primer operando: "))
            operando2 = float(input("Introduce el segundo operando: "))
            operador = input("Introduce la operación (+, -, *, /): ").strip()
            
            return operando1, operando2, operador
        except ValueError:
            print("Error: Por favor ingresa números válidos")
            return None, None, None
    
    def ejecutar(self):
        """Método principal para ejecutar la calculadora"""
        print("=== CALCULADORA POO ===")
        
        while True:
            print("\nOpciones:")
            print("1. Realizar operación")
            print("2. Ver historial")
            print("3. Limpiar historial")
            print("4. Salir")
            
            opcion = input("Selecciona una opción (1-4): ")
            
            if opcion == "1":
                self._realizar_operacion()
            elif opcion == "2":
                self.calculadora.mostrar_historial()
            elif opcion == "3":
                self.calculadora.limpiar_historial()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
    
    def _realizar_operacion(self):
        """Método privado para realizar una operación"""
        a, b, op = self.obtener_datos()
        
        if a is not None and b is not None and op:
            resultado = self.calculadora.realizar_operacion(a, b, op)
            print(f"Resultado: {resultado}")


# Ejecutar la calculadora
if __name__ == "__main__":
    interfaz = InterfazCalculadora()
    interfaz.ejecutar()