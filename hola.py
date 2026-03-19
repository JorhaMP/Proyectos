#print("Hello World")

nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True #False

#Para uso de constantes estas se deben poner en mayusculas por convencion de programacion
IMPUESTO = 13

#NO se usan espacio en blanco
IMPUESTO_VENTAS = 13

#Snake Case
tiene_licencia_conducir = False



#Conversiones
altura_entera=int(altura)
print(altura_entera)

edad_float = float(edad)
print(edad_float)

edad_string = str(edad)
print(edad_string)

#Comentario unilinea se usa #

"""
Comentario en bloque uso de " o ''' 3 veces

"""

'''
Comentario en bloque

'''


#Captura desde consola

nombre = input("Por favor, digita el nombre: ") #dependiendo de la version hay que poner un espacio para que no salga pegado
edad = int(input("Digita la edad: "))
edad_aumentada = edad + 5 

print ("El nombre digitado es:",nombre)
print ("Edad aumentada: ", edad_aumentada)


#Operaciones

"""
Suma +
Division /
Resta -
Multiplicacion * 

Exponencial **
Modulo %
Division entera //

"""

#Comparacion

"""
Igualdad ==
Desigualdad !=
Mayor que >
Menor que <

Mayor o igual que >=
Menor o igual que <=

"""
# Operadores de comparación
x = 5
y = 10
igual = x == y # False
print("Igualdad: ",igual)

desigual = x != y # True
print("Desigualdad: ", desigual)

mayor_que = x > y # False
print("Mayor que: ",mayor_que)

menor_que = x < y # True
print("Menor que: ",menor_que)

mayor_o_igual = x >= y # False
print("Mayor o igual que: ",mayor_o_igual)

menor_o_igual = x <= y # True
print("Menor o igual que: ", menor_o_igual)


#Operadores Logicos
# Operadores lógicos
a = True
b = False
y = a and b # False
o = a or b # True
no = not a # False

#Estructura básica de “if”, “elif” y “else”:
#if condicion_1:
# Bloque de código que se ejecuta si la condición_1 es verdadera
# Puede contener múltiples líneas de código
# ...
#elif condicion_2:
# Bloque de código que se ejecuta si la condicion_1 es falsa
# y la condicion_2 es verdadera
# Puede contener múltiples líneas de código
# ...
#else:
# Bloque de código que se ejecuta si ninguna de las condiciones anteriores es
#verdadera
# Puede contener múltiples líneas de código

edad = 20
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres mayor de edad pero no eres un adulto mayor")
else:
    print("Eres un adulto mayor")

#Nota
#Shift + Tab y selecionar todo el bloque de texto para mover el codigo

#While
contador = 0
while contador < 5:
    print(contador)
    #Es necesario ponerle un final 
    contador += 1
    
    
#For varias maneras

#For x in range (#,##-1)
for numero in range (1,11):
    print(numero)

for numero in range (11):
    print(numero)
    