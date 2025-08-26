def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
def operaciones(a, b, op):
    if op == "+":
        return suma(a, b)
    elif op == "-":
        return resta(a, b)
    elif op == "*":
        return multiplicacion(a, b)
    elif op == "/":
        return division(a, b)
    else:
        return "Operador no válido"

def datos():
    operando1 = int(input("Introduce el primer operando: "))
    operando2 = int(input("Introduce el segundo operando: "))
    operador = input("Introduce la operación (+, -, *, /): ")
    resultado = operaciones(operando1, operando2, operador)
    print("Resultado:", resultado)
    return operando1, operando2, operador

datos()