class Cuenta_bancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.__titular = titular
        self.__saldo = saldo
        self.__numero_cuenta = numero_cuenta
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_numero_cuenta(self):
        return self.__numero_cuenta
    
    def depositar(self, cantidad):
        """Deposita una cantidad en la cuenta bancaria"""
        
        if cantidad > 0:
            saldo_actual = self.get_saldo()
            return saldo_actual + cantidad 
        else:
            return "Cantidad inválida para depositar"  

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta bancaria si hay saldo suficiente"""

        saldo_actual = self.get_saldo()
        if cantidad > 0 and cantidad <= saldo_actual:
            return saldo_actual - cantidad
        else:
            return "Cantidad inválida para retirar"

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
            return "Cantidad excede el límite de retiro"
        else:
            return super().retirar(cantidad)
        
    def depositar(self, cantidad):
        return super().depositar(cantidad)

cuenta1 = Cuenta_ahorro("Juan Perez", 2000, "123456789")
print(cuenta1.retirar(900)) 

class Cuenta_corriente(Cuenta_bancaria):
    def __init__(self, titular, saldo, numero_cuenta, sobreGiro_permitido=500):
        super().__init__(titular, saldo, numero_cuenta)
        self.__sobreGiro_permitido = sobreGiro_permitido

    def get_sobreGiro_permitido(self):
        return self.__sobreGiro_permitido  
    
    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta corriente si no excede el sobregiro permitido"""

        saldo_actual = self.get_saldo()
        if cantidad > (saldo_actual + self.get_sobreGiro_permitido()):
            return "SobregiroError: Cantidad excede el sobregiro permitido"
        else:
            return super().retirar(cantidad)
        
    def depositar(self, cantidad):
        return super().depositar(cantidad)