class BancoError(Exception):
    """Base para excepciones del sistema bancario"""
    pass

class CantidadInvalidaError(BancoError):
    pass

class SaldoInsuficienteError(BancoError):
    pass

class SobregiroError(BancoError):
    pass


class Cuenta_bancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.__titular = titular
        self.__saldo = float(saldo)
        self.__numero_cuenta = numero_cuenta
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    # Método protegido para actualizar saldo desde subclases
    def _set_saldo(self, nuevo_saldo):
        self.__saldo = float(nuevo_saldo)
    
    def depositar(self, cantidad):
        """Deposita una cantidad en la cuenta bancaria"""
        if cantidad <= 0:
            raise CantidadInvalidaError("Cantidad inválida para depositar")
        nuevo = self.get_saldo() + cantidad
        self._set_saldo(nuevo)
        return f"Depósito exitoso. Nuevo saldo: {nuevo}"

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta bancaria si hay saldo suficiente"""
        if cantidad <= 0:
            raise CantidadInvalidaError("Cantidad inválida para retirar")
        saldo_actual = self.get_saldo()
        if cantidad > saldo_actual:
            raise SaldoInsuficienteError("Saldo insuficiente")
        nuevo = saldo_actual - cantidad
        self._set_saldo(nuevo)
        return f"Retiro exitoso.\n Nuevo saldo: {nuevo}"


    def mostrar_saldo(self):
        """Muestra el saldo actual de la cuenta bancaria"""
        return f"El saldo actual de la cuenta {self.get_numero_cuenta()} es: {self.get_saldo()}"                 

class Cuenta_ahorro(Cuenta_bancaria):
    def __init__(self, titular, saldo, numero_cuenta, limite_retiro=1000):
        super().__init__(titular, saldo, numero_cuenta)
        self.__limite_retiro = limite_retiro 

    def get_limite_retiro(self):
        return self.__limite_retiro    

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta de ahorro si no excede el límite de retiro"""
        if cantidad > self.get_limite_retiro():
            raise CantidadInvalidaError("La cantidad excede el límite de retiro")
        return super().retirar(cantidad)
        
    def depositar(self, cantidad):
        return super().depositar(cantidad)

class Cuenta_corriente(Cuenta_bancaria):
    def __init__(self, titular, saldo, numero_cuenta, sobreGiro_permitido=500):
        super().__init__(titular, saldo, numero_cuenta)
        self.__sobreGiro_permitido = sobreGiro_permitido

    def get_sobreGiro_permitido(self):
        return self.__sobreGiro_permitido  
    
    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta corriente si no excede el sobregiro permitido"""
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad es inválida para retirar")
        saldo_actual = self.get_saldo()
        if cantidad > (saldo_actual + self.get_sobreGiro_permitido()):
            raise SobregiroError("La cantidad excede el sobregiro permitido")
        nuevo = saldo_actual - cantidad
        return f"Retiro exitoso.\n Nuevo saldo: {nuevo}"
        # permitir saldo negativo (sobregiro)
        self._set_saldo(nuevo)
        return f"Retiro exitoso.\n Nuevo saldo: {nuevo}"
        
    def depositar(self, cantidad):
        return super().depositar(cantidad)
    
class menu_bancario:
    @staticmethod
    def mostrar_menu():
        return """Menú Bancario:
1. Depositar
2. Retirar
3. Mostrar saldo
4. Salir"""
    @staticmethod
    def ejecutar_opcion(opcion, cuenta, cantidad=0):
        try:
            if opcion == 1:
                return cuenta.depositar(cantidad)
            elif opcion == 2:
                return cuenta.retirar(cantidad)
            elif opcion == 3:
                return cuenta.mostrar_saldo()
            elif opcion == 4:
                return "Saliendo del menú bancario."
            else:
                return "Opción inválida."
        except BancoError as e:
            return f"Error: {e}"


if __name__ == "__main__":
    cuenta1 = Cuenta_ahorro("Juan Perez", 2000, "123456789")
    cuenta2 = Cuenta_corriente("Ana", 100, "987654321")

    cuentas = {"1": cuenta1, "2": cuenta2}
    print("\n")
    print("----------Bienvenido al sistema bancario----------")

    while True:
        print("\nCuentas disponibles:")
        for k, c in cuentas.items():
            print(f"{k}. {c.get_titular()} - {c.get_numero_cuenta()}")
        print("\n")       
        sel = input("Seleccione cuenta ó ('q' para salir): ").strip()
        if sel.lower() in ("q", "salir", "exit"):
            print("Saliendo.")
            break
        if sel not in cuentas:
            print("Cuenta inválida. Intente de nuevo.")
            continue

        cuenta = cuentas[sel]
        while True:
            print("\n" + menu_bancario.mostrar_menu())
            try:
                opcion = int(input("Elija una opción: ").strip())
            except ValueError:
                print("Entrada inválida. Introduzca un número.")
                continue

            if opcion == 4:
                print("Volviendo a selección de cuenta.")
                break

            cantidad = 0.0
            if opcion in (1, 2):
                try:
                    cantidad = float(input("Ingrese cantidad: ").strip())
                except ValueError:
                    print("Cantidad inválida. Intente de nuevo.")
                    continue

            resultado = menu_bancario.ejecutar_opcion(opcion, cuenta, cantidad)
            print(resultado)