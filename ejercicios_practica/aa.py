class Calculadora:
    def __init__(self, *args):
        if len(args) == 0:
            self._operando1, self._operando2, self._operador = 0, 0, '+'
        elif len(args) == 2:
            self._operando1, self._operando2, self._operador = args[0], args[1], '+'
        elif len(args) == 3:
            self._operando1, self._operando2, self._operador = args
        else: 
            raise ValueError("Número de argumentos inválido")
    def calcular(self):
        if self._operador == '+':
            return self._operando1 + self._operando2
        elif self._operador == '-':
            return self._operando1 - self._operando2
        elif self._operador == '*':
            return self._operando1 * self._operando2
        elif self._operador == '/':
            if self._operando2 == 0:
                raise ValueError("División por cero")
            return self._operando1 / self._operando2
        else:
            raise ValueError("Operador inválido")
# ---- Prueba ----
c1 = Calculadora()
c2 = Calculadora(10, 5)
c3 = Calculadora(10, 5, '*')
print(c1.calcular())  # 0
print(c2.calcular())  # 15
print(c3.calcular())  # 50