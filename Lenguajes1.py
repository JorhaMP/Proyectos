"""
mis_numeros = []

cantidad_numeros = int(input("¿Cuántos números desea ingresar? "))

for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese un número {i + 1}: "))
    mis_numeros.append(numero)


print("Los números ingresados son: ", mis_numeros)
"""

#Input de forma
#f"Hola soy {i+1} y tengo {edad} años"


# Crear una lista vacía para almacenar los nombres
"""
mis_nombres = []
respuesta = 1
# Bucle para solicitar nombres hasta que el usuario decida salir
while respuesta == 1:
    nombre = input("Ingrese un nombre: ")
    

# Agregar el nombre a la lista
    mis_nombres.append(nombre)

    respuesta = int(input("¿Desea agregar más nombres? (1 para sí, 0 para no): "))

# Mostrar todos los nombres ingresados
print("Nombres ingresados:")
for i in mis_nombres:
    print(i)

lista_mixta = [1, "dos", True, [4, 5, 6]]
"""
mi_lista = [10, 20, 30, 40, 50]
primer_elemento = mi_lista[0] # Accede al primer elemento de la lista
segundo_elemento = mi_lista[1] # Accede al segundo elemento de la lista
ultimo_elemento = mi_lista[-1] # Accede al último elemento de la lista"""
"""
mi_lista[0] #devuelve el primer elemento de la lista, que es 10.
mi_lista[1] #devuelve el segundo elemento de la lista, que es 20.
mi_lista[-1] # devuelve el último elemento de la lista, que es 50.
"""

print("Último elemento:", ultimo_elemento) #Devuelve el último elemento de la lista, que es 50.
print("Último elemento:", mi_lista[-1]) #Devuelve el último elemento de la lista, que es 50.

sublista = mi_lista[1:4] # Obtiene una sublista desde el índice 1 hasta el índice 3 (excluyendo el índice 4)
print("Sublista:", sublista) # Devuelve la sublista [20, 30, 40]

#Recordar que las listas o array su primer elemento es el 0

mi_lista.extend([60, 70, 80]) # Agrega los elementos 60, 70 y 80 al final de la lista

mi_lista.insert(1,5) # Inserta el número 5 en el índice 1 de la lista

mi_lista.remove(30) # Elimina el número 30 de la lista

elemento_eliminado = mi_lista.pop(1) # Elimina el elemento en el índice 1 y lo devuelve

indice = mi_lista.index(40) # Devuelve el índice del primer elemento que es igual a 40

cantidad = mi_lista.count(20) # Devuelve la cantidad de veces que el número 20 aparece en la lista

mi_lista = ["Pedro", "Ana", "Luis", "María"]
mi_lista.sort() # Ordena la lista en orden ascendente

print("Lista ordenada:", mi_lista) # Devuelve la lista ordenada ['Ana', 'Luis', 'María', 'Pedro']

mi_lista.reverse() # Ordena la lista en orden descendente

print("Lista ordenada en orden descendente:", mi_lista) # Devuelve la lista ordenada en orden descendente ['Pedro', 'María', 'Luis', 'Ana']


#TUPLAS diferenciadas por ser hechas con parentesis en vez de corchetes, son inmutables, no se pueden modificar despues de creadas, no tienen métodos como append, remove, etc.

tupla = (1, 2, 3, 4, 5)
print("Tupla:", tupla)
print("Primer elemento de la tupla:", tupla[0]) # Devuelve el primer elemento de la tupla, que es 1
print("Subtupla:", tupla[1:4]) # Devuelve la subtupla (2, 3, 4)

#tambien se pueden crear tuplas sin usar parentesis, simplemente separando los elementos por comas, sin embargo esto no es recomendable ya que puede generar confusión con otros tipos de datos.
tupla_sin_parentesis = 1, 2, 3, 4, 5
print("Tupla sin paréntesis:", tupla_sin_parentesis)


#Crear una tupla de coordenadas (x, y)
punto = (10, 20)
print("Coordenadas: ", punto)

#Desempaquetar una tupla
x, y = punto
print("Coordenada x:", x)
print("Coordenada y:", y)

#punto.[0] = 30 # Esto generará un error ya que las tuplas son inmutables y no se pueden modificar después de creadas.

#Diccionarios, son estructuras de datos que almacenan pares de clave-valor, se crean con llaves {} y cada elemento se define como clave: valor.

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "San José"}
print("Diccionario:", mi_diccionario)
print("Valor de la clave 'nombre':", mi_diccionario["nombre"]) # Devuelve el valor asociado a la clave 'nombre', que es 'Juan'
print("Valor de la clave 'edad':", mi_diccionario["edad"]) # Devuelve el valor asociado a la clave 'edad', que es 30
print("Valor de la clave 'ciudad':", mi_diccionario["ciudad"]) # Devuelve el valor asociado a la clave 'ciudad', que es 'San José'

mi_ndiccionario = {}
mi_ndiccionario["nombre"] = "Juan"
mi_ndiccionario["edad"] = 25
mi_ndiccionario["ciudad"] = "Alajuela"

##la clave tambien puede ser una variable, por ejemplo:
clave = "nombre"
valor = "María"
mi_diccionario[clave] = valor # Esto agregará la clave 'nombre' con el valor 'María' al diccionario mi_diccionario 

##Las claves no se pueden elimiar, pero se pueden modificar su valor, por ejemplo:
mi_diccionario["nombre"] = "Carlos" # Esto modificará el valor de la clave 'nombre' a 'Carlos' en el diccionario mi_diccionario


#Verificacion si una clave existe en el diccionario
if "nombre" in mi_diccionario:
    print("La clave 'nombre' existe en el diccionario.")
else:    print("La clave 'nombre' no existe en el diccionario.")

#Conjuntos set() son estructuras de datos que almacenan elementos únicos, no tienen un orden específico y se crean con la función set() o con llaves {}.
mi_conjunto = {1, 2, 3, 4, 5}
#No permite elementos duplicados, por ejemplo:
mi_conjunto = {1, 2, 2, 3, 4, 5}
print("Conjunto:", mi_conjunto) # Devuelve el conjunto {1, 2, 3, 4, 5} sin el número 2 duplicado

"""Si se pasa una lista a un conjunto, se eliminarán los elementos duplicados de la lista."""


#Operaciones con conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Unión
union = conjunto1 | conjunto2
print("Unión:", union)

# Intersección
interseccion = conjunto1 & conjunto2
print("Intersección:", interseccion)

# Diferencia
diferencia = conjunto1 - conjunto2
print("Diferencia:", diferencia)

# Diferencia simétrica
diferencia_simetrica = conjunto1 ^ conjunto2
print("Diferencia simétrica:", diferencia_simetrica)