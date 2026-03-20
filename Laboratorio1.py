"""
Laboratorio 1

Curso: Lenguajes para Aplicaciones Comerciales

Estudiante: Jorhany Marin Perez
Carnet: B94541
Profesor: James Mcintosh Molina

"""
#import Laboratorio1_operaciones
from Laboratorio1_operaciones import modularidad_sumar, modularidad_restar, modularidad_multiplicar, modularidad_dividir, calculadora_modular
from mi_paquete.operaciones import *
from mi_paquete.algebra import *
import math
#import datetime
import requests
from Clases.Persona import Persona
from Clases.Carro import Carro
from Clases.Moto import Moto
from Clases.circulo import Circulo
from Clases.cuadrado import Cuadrado
from Clases.Gato import Gato
from Clases.Perro import Perro

def main():
    print("Programa Principal")
    
    #Ejercicio 1: Conjuntos Frozenset
    print("Ejercicio 1: Conjuntos Frozenset")
    ejercicio1()
    
    #Ejercicio 2: Funciones en Python
    print("\nEjercicio 2: Funciones en Python")
    saludar() 
    n1 = int(input("Ingrese el primer número para sumar: "))
    n2 = int(input("Ingrese el segundo número para sumar: "))

    #Ejercicio 3: Paso de Argumentos
    print("Ejercicio 3: Paso de Argumentos")
    sumar(n1, n2)
    sumado = suma_retorno(n1, n2)
    print(f"La suma de {n1} y {n2} es: {sumado}")
    print(f"La suma de {n1} y {n2} es: {suma_retorno(n1, n2)}")
    saludar_con_default() #Esta función se llama sin argumentos, por lo que usará el valor predeterminado "mundo"
    nombre_usuario = input("Ingrese su nombre para saludar: ")
    saludar_con_default(nombre_usuario) #Esta función se llama con un argumento, por lo que usará el nombre ingresado por el usuario en lugar del valor predeterminado "mundo"
    
    #Ejercicio 4: Paso de Argumentos + Combinado
    print("\nEjercicio 4: Paso de Argumentos + Combinado")
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
    
    
    # Ejercicio 5: Retorno de valores
    
    print("\nEjercicio 5: Retorno de Valores")
    resultado_suma = suma_retorno(10, 20)
    print(f"El resultado de la suma es: {resultado_suma}")
    resultado_calculadora = calculadora(10, 5)
    print(f"Resultados de la calculadora: Suma={resultado_calculadora[0]}, Resta={resultado_calculadora[1]}, Multiplicación={resultado_calculadora[2]}, División={resultado_calculadora[3]}")   
    
    print(f"Tipo numérico de 10: {tipo_numerico(10)}")
    print(f"Tipo numérico de -5: {tipo_numerico(-5)}")
    print(f"Tipo numérico de 0: {tipo_numerico(0)}")
    
    # Ejercicio 6: Retornar de estructura de datos
    print("\nEjercicio 6: Retornar de Estructura de Datos")
    lista_creada = crear_lista(10)
    print(f"Lista creada con números del 1 al 10: {lista_creada}")
    
    
    #Ejercicio 7 Alcance de Variables
    print("\nEjercicio 7: Alcance de Variables")
    funcion_1()
    funcion_2()
    aumentar_contador()
    valor_x()
    valor_x_global()
    
    funcion_anidada()
    
    #Ejercicio 8: Modularidad
    suma = modularidad_sumar(5, 3)
    resta = modularidad_restar(5, 3)
    multiplicacion = modularidad_multiplicar(5, 3)
    division = modularidad_dividir(5, 3)
    print("\nEjercicio 8: Modularidad")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

    suma,resta,multiplicacion,division = calculadora_modular(10, 5)
    print(f"Resultados de la calculadora modular: Suma={suma}, Resta={resta}, Multiplicación={multiplicacion}, División={division}")

    #Ejercicio 9: Paquetes
    #Un paquete es un conjunto de modulos
    print("\nEjercicio 9: Paquetes")
    print(f"Resultado de paq_sumar(10, 5): {paq_sumar(10, 5)}")
    print(f"Resultado de paq_restar(10, 5): {paq_restar(10, 5)}")
    print(f"Resultado de paq_multiplicar(10, 5): {paq_multiplicar(10, 5)}")
    print(f"Resultado de paq_dividir(10, 5): {paq_dividir(10, 5)}")
    print(f"Resultado de cuadrado(5): {cuadrado(5)}")
    
    #Ejercicio 10: Módulos internos
    print("\nEjercicio 10: Módulos internos")
    print(f"Valor de PI: {PI}")
    print(f"Raíz cuadrada de 16: {raiz}")
    
    #Ejercicio 11: Módulos externos
    print("\nEjercicio 11: Módulos externos")
    print(f"Respuesta de la solicitud a la API de GitHub: {respuesta}")
    
    #Ejercicio 12: if __name__
    
    #Ejercicio 13: Manejo de excepciones
    try:
        cociente = input("Ingrese el cociente para dividir: ")
        divisor = input("Ingrese el divisor para dividir: ")
        resultado_division = division(int(cociente), int(divisor))
        print(f"Resultado de dividir {cociente} entre {divisor}: {resultado_division}")
        #print("Resultado de la división:"+ resultado_division)
    except ValueError as e: #Si el usuario ingresa un valor que no se puede convertir a entero, se generará una excepción ValueError, que se captura en este bloque except para imprimir un mensaje de error indicando que se deben ingresar valores numéricos válidos.
        print("Error: Por favor, ingrese valores numéricos válidos para el cociente y el divisor.", str(e))
    else: #Si no ocurre ninguna excepción, se ejecutará el bloque else, que en este caso imprime un mensaje indicando que la división se realizó correctamente.
        print("La división se realizó correctamente.")
    finally: #Si todo se ejecuta correctamente, o si ocurre una excepción, se ejecutará el bloque finally, que en este caso imprime un mensaje indicando que se ha terminado el manejo de excepciones.
        print("Fin del manejo de excepciones.")
        
    #Ejercicio 14: Clases y objetos
    
    per = Persona("Jorhany", 25)
    saludo = per.saludar()
    print("\nEjercicio 14: Clases y objetos")
    print(per) #Esto imprimirá la representación de la persona utilizando el método __str__ que se ha definido en la clase Persona, mostrando el nombre y la edad de la persona.
    
    #Ejercicio 15: Propertys
    #Las propertys son una forma de controlar el acceso a los atributos de una clase,
    print("\nEjercicio 15: Propertys")
    per.nombre = "Juan"
    print(per)
    
    nombre = input("Ingrese un nuevo nombre para la persona: ")
    edad = int(input("Ingrese una nueva edad para la persona: "))
    per2 = Persona(nombre, edad)
    
    print(per)
    
    per3 = Persona("Maria", 30)
    print(per3.nombre)
    
    per3.nombre = "Ana"
    per3._edad = 35
    print(per3)
    
    #EJercicio 16: Errores en Atributos
    #per4 = Persona("Carlos", -40)
    per4 = Persona(None,None)
    print(per4)
    try:
        per4.nombre = input("Ingrese un nombre para la persona: ")
        per4.edad = int(input("Ingrese una edad para la persona: "))
        print(per4)
    except ValueError as e:
        print("Error", str(e))
        
    annio = 2026 - per4.edad
    print(f"El año de nacimiento de {per4.nombre} es: {annio}")
     
    #Ejercicio 17: Atributos error
    try:
        del per4.edad
        print(per4)
    except AttributeError as e:
        print("Error: ", type(e),"\n", str(e))
    print("Edad eliminada correctamente.")
    print(per4.nombre)

    #Ejercicio 18: Herencia
    car = Carro(None, None, None)
    car.marca = input("Ingrese la marca del carro: ")
    car.modelo = input("Ingrese el modelo del carro: ")
    try:
        car.puertas = int(input("Ingrese el número de puertas del carro: "))
        print(car)
    except ValueError as e:
        print("Error: ",type(e),"\n", str(e))
    else:
        print("Carro creado correctamente.")
    finally:
        print("Fin del proceso de creación del carro.")

    moto = Moto("Yamaha", "MT-07", 689)
    print(moto)
    
    #Ejercicio 19: Abstracción
    cir = Circulo("Rojo", 5)
    cua = Cuadrado("Azul", 4)
    print(cir)
    print(cua)
    
    print(cir, "Área del círculo:", cir.area())
    print(cua, "Área del cuadrado:", cua.area())
    
    #Ejercicio 20: Polimorfismo
    animales = [Perro("Rex", 3, "Labrador"), Gato("Whiskers", 2, "Siames")]
    for animal in animales:
        print(animal.descripcion())

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
    
# Ejercicio 3: Paso de Argumentos
def sumar(a, b):
    print(f"La suma de {a} y {b} es: {a + b}")

def suma_retorno(a,b):
    return a + b

def saludar_con_default(nombre="mundo"):
    print(f"¡Hola, {nombre}! ¿Cómo estás?")

#Ejercicio 4: Paso de Argumentos + Combinado

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

#Ejercicio 5: Retorno de Valores
def suma_retorno(a, b):
    return a + b

def calculadora(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    
    return suma, resta, multiplicacion, division

def tipo_numerico(a):
    if a > 0:
        return "Mayor que cero"
    elif a < 0:
        return "Menor que cero"
    else:
        return "Igual a cero"

#Ejercicio 6: Retornar de Estructura de Datos

def crear_lista(n):
    return [i for i in range(1, n + 1)]


#Ejercicio 7: Alcance de Variables

variable_global = "Soy una variable global"
contador = 0
x = 10

def funcion_1():
    print(variable_global)  # Acceso a la variable global

def funcion_2():
    variable_local = "Soy una variable local"
    print(variable_local)  # Acceso a la variable local

def aumentar_contador():
    global contador  # Indica que se va a modificar la variable global 'contador'
    contador += 1
    print(f"Contador incrementado: {contador}")

#Combinar global y local

def valor_x():
    x = 5  # Variable local 'x' dentro de la función
    print(f"Valor de x dentro de la función: {x}")

def valor_x_global():
    global x
    print(f"Valor de x global: {x}")

#Funciones anidadas
def funcion_anidada():
    y=5
    print(f"Valor de y dentro de la función: {y}")
    
    def funcion_interna():
        y = 10  # Variable local 'y' dentro de la función interna
        print(f"Valor de y dentro de la función interna: {y}")
    
    funcion_interna()
    print(f"Valor de y después de la función interna: {y}")  # Muestra el valor de 'y' en la función externa, que no se ve afectado por la función interna

    def funcion_interna_2():
        nonlocal y  # Indica que se va a modificar la variable 'y' de la función externa
        y = 15
        print(f"Valor de y dentro de la función interna 2: {y}")
    funcion_interna_2()
    print(f"Valor de y después de la función interna 2: {y}")  # Muestra el valor de 'y' en la función externa, que ahora se ve afectado por la función interna 2

#Ejercicio 8: Modularidad
#Operaciones realizadas en un archivo aparte llamado Laboratorio1_operaciones.py, que se importa al inicio de este archivo para utilizar sus funciones.

#Ejercicio 9: Paquetes
#Operaciones realizadas en un archivo aparte llamado mi_paquete/operaciones.py, que se importa al inicio de este archivo para utilizar sus funciones.

#Ejercicio 10: Módulos internos
PI = math.pi
raiz = math.sqrt(16)

#Ejercicio 11: Módulos externos
#respuesta = requests.get("https://api.github.com")
respuesta = requests.get("https://www.amazon.com")

#Ejercicio 12: if __name__
def Saludar12():
    print("¡Hola! Bienvenido al ejercicio 12.")
def sumar12(a, b):
    return a + b

#Ejercicio 13: Manejo de excepciones

#Ejercicio 14: Clases y objetos

#Ejercicio 15: Propertys

#Seguridad que se realiza cuando el modulo es ejecutado directamente, y no importado por otro modulo. Esto es útil para evitar que ciertas partes del código se ejecuten cuando el módulo es importado como parte de otro programa, pero se ejecuten cuando el módulo es ejecutado directamente.
#Tambien permite mayor modularidad, ya que se pueden definir funciones y variables que solo se ejecutan cuando el módulo es ejecutado directamente, y no cuando es importado por otro módulo. Esto es especialmente útil para pruebas o para ejecutar código específico que no debe ser ejecutado cuando el módulo es importado como parte de otro programa.
if __name__ == "__main__":
    Saludar12()
    numero1 = int(input("Ingrese el primer número para sumar en el ejercicio 12: "))
    numero2 = int(input("Ingrese el segundo número para sumar en el ejercicio 12: "))
    resultado12 = sumar12(numero1, numero2)
    print(f"El resultado de la suma en el ejercicio 12 es: {resultado12}")
    
    
    main()
    
    