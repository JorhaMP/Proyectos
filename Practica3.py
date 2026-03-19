"""
Nombre: Jorhany Marin Perez
Carnet: B94541
Curso: Lenguajes para aplicaciones comerciales
Profesor: James Mcintosh Molina.


1. Desarrolle un programa que solicite al usuario una cadena de texto y
cuente la cantidad de caracteres únicos que contiene. Utiliza un conjunto
para almacenar los caracteres únicos.

2. Cree un programa que simule la gestión de inventario de una tienda.
Utilice un diccionario donde las claves sean los nombres de los productos 
y los valores sean las cantidades disponibles en stock. Permita al usuario
realizar operaciones como agregar productos, actualizar cantidades y
eliminar productos.

3. Escriba un programa que reciba una tupla de elementos y verifique si hay
duplicados en ella. Utiliza un conjunto para realizar esta verificación.

4. Crea un programa que permita al usuario ingresar el nombre y la edad de
varios estudiantes. Almacena esta información en un diccionario donde
las claves son los nombres y los valores son las edades. Al finalizar
muestre el diccionario construido.

5. Desarrolla un programa que combine dos diccionarios en uno solo. Si hay
claves duplicadas, conserva los valores del primer diccionario. Utilice la
función items() para la solución. Por ejemplo:

    mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
    for clave, valor in mi_diccionario.items():
     if clave not in mi_otro_diccionario:
     mi_otro_diccionario[nombre]= edad
"""

def main():
    print("Bienvenido a la práctica 3 de Lenguajes para aplicaciones comerciales.")
    print("A continuación, se realizarán los ejercicios solicitados.")

    play = 1
    while play == 1:
        opcion = int(input("\nSeleccione el ejercicio que desea ejecutar (1-5) o 0 para salir: "))
        match opcion:
            case 1:
                contar_caracteres_unicos()
            case 2:
                gestion_inventario()
            case 3:
                verificar_duplicados_tupla()
            case 4:
                almacenar_estudiantes()
            case 5:
                combinar_diccionarios()
            case 0:
                play = 0
                print("Saliendo del programa...")
            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")

#1 Contar caracteres únicos en una cadena de texto-----------------------------------------------------------------------------------
def contar_caracteres_unicos():
    print("\n~~~~~~~~~~~~~~~Contar caracteres únicos en una cadena de texto~~~~~~~~~~~~~~~")
    texto = input("Ingrese un texto: ")
    conjunto = set(texto)
    print("Su cadena " ,texto)
    print("Los caracteres únicos en el texto son:", conjunto)
    contador = 0
    for elemento in conjunto:
        contador += 1
    print("El número de caracteres únicos en el frase es:", contador)
    print("El número de caracteres únicos en el frase es:", len(conjunto))

#2 Gestión de inventario de una tienda----------------------------------------------------------------------------------------------
def gestion_inventario():
    print("\n~~~~~~~~~~~~~~~Gestión de inventario de una tienda~~~~~~~~~~~~~~~")
    inventario = {}
    play = 1

    while play == 1:
        print("\nSeleccione una opción:")
        opcion = int(input("1. Agregar producto\n2. Actualizar cantidad\n3. Eliminar producto\n4. Mostrar inventario\n0. Salir\n"))
        match opcion:

            case 1: #Agregar productos al inventario
                producto = str(input("Ingrese el nombre del producto: "))
                cantidad = int(input(f"Ingrese la cantidad disponible en stock para el producto '{producto}': "))
                inventario[producto] = cantidad
                print(f"\n\nProducto '{producto}' agregado con cantidad {cantidad}.")

            case 2: #Actualizar la cantidad de un producto en el inventario
                producto = str(input("Ingrese el nombre del producto a actualizar: "))
                if producto in inventario:
                    cantidad = int(input(f"Ingrese la nueva cantidad disponible para el producto '{producto}': "))
                    inventario[producto] = cantidad
                    print(f"Producto '{producto}' actualizado con nueva cantidad {cantidad}.")
                else:
                    print(f"Producto '{producto}' no encontrado en el inventario.")

            case 3:
                producto = str(input("Ingrese el nombre del producto a eliminar: "))
                if producto in inventario:
                    del inventario[producto]
                    print(f"Producto '{producto}' eliminado del inventario.")
                else:
                    print(f"Producto '{producto}' no encontrado en el inventario.")

            case 4: #Capacidad de revisar el stock actual del inventario
                print("\nInventario actual:")
                for producto, cantidad in inventario.items():
                    print(f"{producto}: {cantidad}")

            case 0: #Exit
                play = 0
                print("Saliendo del inventario...")
            case _: #Default
                print("Opción no válida. Por favor, seleccione una opción válida.")

#3 Verificar duplicados en una tupla----------------------------------------------------------------------------------------------
def verificar_duplicados_tupla():
    print("\n~~~~~~~~~~~~~~~Verificar duplicados en una tupla~~~~~~~~~~~~~~~")
    lista = []
    respuesta = 1

    #Ingresar elementos a la una lista temporal para luego convertirla a tupla
    while respuesta == 1:
        elemento = str(input("Ingrese un elemento para la tupla: "))
        lista.append(elemento)
        respuesta = int(input("¿Desea agregar más elementos a la tupla? (1 para sí, 0 para no): "))

    tupla = tuple(lista)
    conjunto = set(tupla)

    if len(conjunto) < len(tupla):
        print("La tupla contiene duplicados.")
    else:
        print("La tupla no contiene duplicados.")

#4 Almacenar información de estudiantes en un diccionario----------------------------------------------------------------------------------------------
def almacenar_estudiantes():
    print("\n~~~~~~~~~~~~~~~Almacenar información de estudiantes en un diccionario~~~~~~~~~~~~~~~")
    estudiantes = {}
    respuesta = 1
    while respuesta == 1:
        nombre = str(input("Ingrese el nombre del estudiante: "))
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        estudiantes[nombre] = edad
        respuesta = int(input("¿Desea agregar más estudiantes? (1 para sí, 0 para no): "))

    print("\nDiccionario de estudiantes:")
    for nombre, edad in estudiantes.items():
        print(f"{nombre}: {edad} años")

#5 Combinar dos diccionarios en uno solo----------------------------------------------------------------------------------------------
def combinar_diccionarios():
    print("\n~~~~~~~~~~~~~~~Combinar dos diccionarios en uno solo~~~~~~~~~~~~~~~")
    diccionario1 = {}
    diccionario2 = {}
    respuesta = 1

    print("Ingrese los elementos para el primer diccionario:")

    while respuesta == 1:
        clave = str(input("Ingrese una clave para el primer diccionario: "))
        valor = str(input(f"Ingrese un valor para la clave '{clave}': "))
        diccionario1[clave] = valor
        respuesta = int(input("¿Desea agregar más elementos al primer diccionario? (1 para sí, 0 para no): "))

    print("Ingrese los elementos para el segundo diccionario:")

    respuesta = 1

    while respuesta == 1:
        clave = str(input("Ingrese una clave para el segundo diccionario: "))
        valor = str(input(f"Ingrese un valor para la clave '{clave}': "))
        diccionario2[clave] = valor
        respuesta = int(input("¿Desea agregar más elementos al segundo diccionario? (1 para sí, 0 para no): "))

    # Combinar los dos diccionarios conservando los valores del primer diccionario si hay claves duplicadas
    diccionario_combinado = diccionario2.copy()
    for clave, valor in diccionario1.items():
        diccionario_combinado[clave] = valor

    print("\nDiccionario combinado:")
    for clave, valor in diccionario_combinado.items():
        print(f"{clave}: {valor}")

if __name__ == "__main__":
    main()
