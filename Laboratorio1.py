"""
Laboratorio 1

Curso: Lenguajes para Aplicaciones Comerciales

Estudiante: Jorhany Marin Perez
Carnet: B94541
Profesor: James Mcintosh Molina

"""
def main():
    print("Programa Principal")
    
    print("Ejercicio 1: Conjuntos Frozenset")
    ejercicio1()
    
    print("\nEjercicio 2: Funciones en Python")
    saludar() 
    n1 = int(input("Ingrese el primer número para sumar: "))
    n2 = int(input("Ingrese el segundo número para sumar: "))

    sumar(n1, n2)
    sumado = suma_retorno(n1, n2)
    print(f"La suma de {n1} y {n2} es: {sumado}")
    print(f"La suma de {n1} y {n2} es: {suma_retorno(n1, n2)}")
    saludar_con_default() #Esta función se llama sin argumentos, por lo que usará el valor predeterminado "mundo"
    nombre_usuario = input("Ingrese su nombre para saludar: ")
    saludar_con_default(nombre_usuario) #Esta función se llama con un argumento, por lo que usará el nombre ingresado por el usuario en lugar del valor predeterminado "mundo"
    
    #Por posicion
    restar(5, 9)
    #Por palabra clave
    restar(b=5, a=9)
    #Por argumentos
    saludar_con_default()
    saludar_con_default(nombre="Jorhany") # Llamada a la función con un argumento específico para el parámetro "nombre"
    #POr argumetnos variables
    sumar_varios(1, 2, 3, 4, 5) # Llamada a la función con una cantidad variable de argumentos para sumar varios números a la vez
    #Por **kwargs
    imprimir_info(nombre="Jorhany", edad=25, curso="Lenguajes para aplicaciones comerciales") # Llamada a la función con argumentos de palabra clave que se pasan como un diccionario utilizando **kwargs para imprimir información diversa sobre una persona o entidad.
    imprimir_info(producto="Laptop", precio=999.99)
    imprimir_info(ciudad="San José", país="Costa Rica", población=500000, clima="Tropical")
    #Combinado
    combinar_tipos(1)
    combinar_tipos(1, 3, 4, 5, nombre="Jorhany", edad=25)
    
# Termina main()



# Ejercicio 1: COnjuntos Frozenset
def ejercicio1():
    # Crear un diccionario con frozenset con algunos elementos
    conjunto_frozenset = {
        frozenset(["-852036","-96352"]):"Alajuela", # Se utiliza frozenset para crear un conjunto inmutable como clave del diccionario
        frozenset(["-852037","-96352"]):"Limon",
        frozenset(["-852038","-96352"]):"Puntarenas"
        
        }

    # Imprimir el conjunto frozenset
    print("Conjunto Frozenset:", conjunto_frozenset)
    print("Provincia:", conjunto_frozenset[frozenset(["-852036","-96352"])])
    print("Provincia:", conjunto_frozenset[frozenset(["-852037","-96352"])])
    print("Provincia:", conjunto_frozenset[frozenset(["-852038","-96352"])])
    
        
    # Intentar modificar el conjunto (esto generará un error)
    try:
        conjunto_frozenset.add(6)
    except AttributeError as e:
        print("Error al intentar modificar el conjunto frozenset:", e)
        
# Ejercicio 2: Funciones en Python

def saludar():
    print("¡Hola! ¿Cómo estás?")
    
def sumar(a, b):
    print(f"La suma de {a} y {b} es: {a + b}")

def suma_retorno(a,b):
    return a + b

def saludar_con_default(nombre="mundo"):
    print(f"¡Hola, {nombre}! ¿Cómo estás?")

# Ejercicio 3: Paso de Argumentos

def restar(a, b):
    print(f"La resta de {a} y {b} es: {a - b}")
    
def sumar_varios(*numeros):
    resultado = sum(numeros)
    print(f"La suma de los números {numeros} es: {resultado}")

def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

def combinar_tipos(a, b=2, *args, **kwargs):
    print(f"Valor de a: {a}")
    print(f"Valor de b: {b}")
    print(f"Argumentos adicionales (args): {args}")
    print(f"Argumentos de palabra clave (kwargs): {kwargs}")


if __name__ == "__main__":
    main()