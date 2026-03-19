"""
    Nombre: Jorhany Marin Perez
    Carnet: B94541
    Curso: Lenguajes para aplicaciones comerciales
    Profesor: James Mcintosh Molina.

Realice los siguientes ejercicios:
1. Suma de Elementos: Escribe un programa que calcule la suma de todos
los elementos en una lista de números que previamente fue solicitada al
usuario. No utilizar la función sum(mi_lista).
2. Promedio de Elementos: Escribe un programa que calcule el promedio de
todos los elementos en una lista de números que previamente fue
solicitada al usuario.
3. Duplicar Elementos: Escribe un programa que eleve al cuadrado cada
elemento en una lista que previamente fue solicitada al usuario y guarde
los resultados en una nueva lista.
4. Ordenar Lista: Escribe un programa que ordene una lista de números de
menor a mayor que previamente fue solicitada al usuario.
5. Eliminar Duplicados: Escribe un programa que elimine los elementos
duplicados de una lista que previamente fue solicitada al usuario y guarde
los resultados en una nueva lista. No utilice la función set(mi_lista).
30
6. Contar Elementos: Escribe un programa que cuente cuántas veces
aparece un elemento específico (este se le solicita al usuario) en una lista
que previamente fue solicitada al usuario. No utilizar la función count().
7. Combinar Listas: Escribe un programa que combine dos listas en una sola
lista alternando los elementos ambas listas previamente deben ser
solicitadas al usuario. No utilizar las funciones: len(mi_lista) y
zip(mi_lista1. mi_lista2).
8. Eliminar Elementos Impares: Escribe un programa que elimine todos los
elementos impares de una lista que previamente fue solicitada al usuario,
almacene los números pares en una nueva lista.
9. Multiplicar Listas: Escribe un programa que multiplique cada elemento en
una lista por un número específico (tanto la lista como el número
específico a multiplicar son solicitados al usuario) y guarde los resultados
en una nueva lista.
10.Encontrar Máximo y Mínimo: Escribe un programa que encuentre el valor
máximo y mínimo en una lista de números que previamente fue solicitada
al usuario y los imprima.
11.Solicite nombres y edades de personas al usuario y almacénelos en una
lista hasta que el mismo decida salir del sistema. Al finalizar muestre todos
los nombres y sus respectivas edades ingresadas. No utilizar la función
len(mi_lista).

"""

Nueva_lista = []
respuesta = 1
while respuesta == 1:
    numero = int(input("Ingrese un número: "))
    Nueva_lista.append(numero)
    respuesta = int(input("¿Desea agregar más números? (1 para sí, 0 para no): "))

#1 Suma de Elementos

suma = 0
for n in Nueva_lista:
    suma += n
print("La suma de los elementos es:", suma)

#2 Promedio de Elementos
promedio = 0
if len(Nueva_lista) > 0 :
    promedio = suma / len(Nueva_lista)
    print("El promedio de los elementos es:", promedio)
else:
    print("No se ingresaron números para calcular el promedio.")

#3 Elevar Elementos
elevados = []
for n in Nueva_lista:
    elevados.append(n ** 2)
print("Los elementos elevados al cuadrado son:", elevados)

#4 Ordenar Lista
Nueva_lista.sort()
print("La lista ordenada de menor a mayor es:", Nueva_lista)

#5 Eliminar Duplicados
sin_duplicados = []
for n in Nueva_lista: #Itera a través de cada número n en la lista Nueva_lista
    if n not in sin_duplicados: #Revisa si el número n no está ya en la lista sin_duplicados
        sin_duplicados.append(n) #Si el número n no está en sin_duplicados, se agrega a esa lista. Esto asegura que solo se mantengan los números únicos, eliminando así los duplicados.
print("La lista sin duplicados es:", sin_duplicados)

#6 Contar Elementos
elemento = int(input("Ingrese el elemento a contar: "))
contador = 0
for n in Nueva_lista:
    if n == elemento: #Compara cada número n en la lista Nueva_lista con el elemento que el usuario desea contar. Si n es igual al elemento, entonces se incrementa el contador en 1.
        contador += 1
print(f"El elemento {elemento} aparece {contador} veces en la lista.")

#7 Combinar Listas
lista1 = []
lista2 = []
respuesta = 1

while respuesta == 1:
    numero = int(input("Ingrese un número para la primera lista: "))
    lista1.append(numero)
    respuesta = int(input("¿Desea agregar más números a la primera lista? (1 para sí, 0 para no): "))

respuesta = 1

while respuesta == 1:
    numero = int(input("Ingrese un número para la segunda lista: "))
    lista2.append(numero)
    respuesta = int(input("¿Desea agregar más números a la segunda lista? (1 para sí, 0 para no): "))

lista_combinada = []
rango_superior = 0

#Se busca la lista con tamanio superior para determinar el rango superior a usarse en el bucle for.
if len(lista1) > len(lista2):
    rango_superior = len(lista1)
else:    
    rango_superior = len(lista2)


for i in range(rango_superior): 
    if i < len(lista1): #Si el índice i es menor que el tamaño de lista1, se agrega el elemento correspondiente de lista1 a lista_combinada.
        lista_combinada.append(lista1[i])
    if i < len(lista2): #Si el índice i es menor que el tamaño de lista2, se agrega el elemento correspondiente de lista2 a lista_combinada.
        lista_combinada.append(lista2[i])
print("La lista combinada es:", lista_combinada)

#8 Eliminar Elementos Impares
pares = []
for n in Nueva_lista:
    if n % 2 == 0: #Usando el modulo en 2, si un numero es par el modulo dara como resto 0.
        pares.append(n) #Si n es par, se agrega a la lista pares.
    else:
        Nueva_lista.remove(n) #Si n es impar se elimina de la lista.
print("Los números pares son:", pares)
print("La lista sin números impares es:", Nueva_lista)


#9 Multiplicar Listas
Nueva_lista =  [] #Limpiar la lista para ingresar nuevos números
respuesta = 1
Lista_multiplicada = []

#Carga de numeros a la lista
while respuesta == 1:
    numero = int(input("Ingrese un número: "))
    Nueva_lista.append(numero)
    respuesta = int(input("¿Desea agregar más números? (1 para sí, 0 para no): "))

numero_multiplicar = int(input("Ingrese el número por el cual desea multiplicar los elementos de la lista: "))
i = 0
for n in Nueva_lista:
    Lista_multiplicada.append(n * numero_multiplicar)
    i += 1

print("La lista multiplicada es:", Lista_multiplicada)

#10 Encontrar Máximo y Mínimo
Nueva_lista.sort() #Ordenar la lista de menor a mayor para facilitar la obtención del máximo y mínimo
mayor = Nueva_lista[-1] #mayor con el último elemento de la lista
menor = Nueva_lista[0] # menor con el primer elemento de la lista

#Comprobacion doble para asegurar que se obtiene el máximo y mínimo correcto
for n in Nueva_lista:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n


print("El máximo es:", mayor)
print("El mínimo es:", menor)

#11 Nombres y Edades
nombres_edades = [[],[]] #Lista de dos sublistas, una para nombres y otra para edades
respuesta = 1
while respuesta == 1:
    nombre = input("Ingrese un nombre: ")
    edad = int(input("Ingrese la edad de esa persona: "))
    nombres_edades[0].append(nombre) #Agrega el nombre a la primera sublista
    nombres_edades[1].append(edad) #Agrega la edad a la segunda sublista
    respuesta = int(input("¿Desea agregar más nombres y edades? (1 para sí, 0 para no): "))

print("\nNombres y edades ingresados:")
for i in range(len(nombres_edades[0])): #Se basa el en tamanio de la primera sublista para iterar en el for
    print(f"{nombres_edades[0][i]} tiene {nombres_edades[1][i]} años.") #Imprime el nombre y la edad correspondiente usando el mismo índice i para acceder a ambas sublistas