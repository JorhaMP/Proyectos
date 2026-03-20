def modularidad_sumar(a,b):
    return a + b
def modularidad_restar(a,b):
    return a - b
def modularidad_multiplicar(a,b):
    return a * b
def modularidad_dividir(a,b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"
    
def calculadora_modular(a,b):
    suma = modularidad_sumar(a,b)
    resta = modularidad_restar(a,b)
    multiplicacion = modularidad_multiplicar(a,b)
    division = modularidad_dividir(a,b)
    
    return suma, resta, multiplicacion, division