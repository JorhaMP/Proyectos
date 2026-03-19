"""
Estudiante: Jorhany Marin Perez
Carnet: B94541
Curso: IF4101 - Lenguajes para Aplicaciones Comerciales

Realice los siguientes ejercicios:
1. Cree un programa que muestre la frase: “Hola Mundo”.
2. Cree un programa que solicite el valor de una variable y la muestre en
pantalla.
3. Cree un programa que solicite 2 valores numéricos y mostrar al usuario
la: suma, resta, multiplicación y división.
4. Cree un programa que solicite el valor de un producto y calcular el total a
pagar + impuesto de venta.
5. Cree un programa que lea del usuario 2 números enteros, los sume y
muestre el resultado.
6. Cree un programa que permita leer la edad y peso de una persona y
posteriormente mostrarla en pantalla.
7. Cree un programa que calcule el área de un círculo, a partir del radio
solicitado al usuario.
19
8. Crea una aplicación que solicite al usuario un día de la semana y le
muestre si es un día laboral o no. Sábado y Domingo son días NO
laborables.
9. Cree un programa que al introducir un número por teclado y que nos diga
si es positivo o negativo.
10. Cree un programa que solicite la edad al usuario e indique si es mayor o
menor de edad.
11. Cree un programa que permita saber si un número es mayor o menor que
cero.
12. Cree un programa que lea del usuario 3 números e indique cual es el
mayor de ellos.
13. Cree un programa que permita saber si un número es mayor, menor o
igual que cero.
14. Cree un programa que nos muestre el resultado de multiplicar el número
que introduzca el usuario, desde 1 hasta 10, utilice un bucle para
resolverlo.
15. Cree un programa calcule el cuadrado de los 9 primeros números
naturales, utilice un bucle para resolverlo.

"""
"""
Importaciones necesarias
"""
import math



"""Resolucion de los ejercicios"""
#1
print("Hola Mundo")

#2
variable = input("Digite algo: ")
print("Usted digito: ",variable)

#3
x = int(input("\nDigite el primer valor x: "))
y = int(input("\nDigite el segundo valor y: "))

print("Suma: ",x+y)
print("Resta: ",x-y)
print("Multiplicacion: ",x*y)
print("Division: ",x/y)

#4
producto = float(input("\nDigite el valor del producto: "))
print("El valor con impuestos es: ", producto+(producto*0.13))

#5
x = int(input("\nDigite el primer valor x: "))
y = int(input("\nDigite el segundo valor y: "))

print("Suma: ",x+y)

#6
edad = int(input("\nIngrese su edad: "))
peso = int(input("\nIngrese su peso: "))
print("Usted ingreso una edad de: ",edad," y un peso de: ", peso)

#7
radio = float(input("\nIngrese el radio del circulo: "))
print("El area del circulo es: ", math.pi*radio**2)

#8
dia = str(input("\nIngrese un dia de la semana: "))
if dia == ("Sabado","Domingo","sabado","domingo","SABADO","DOMINGO"):
    print(dia, " NO es un dia laboral")
else:
    print(dia, " ES un dia laboral")
    
#9
numero = int(input("\nIngrese un entero: "))
if numero < 0:
    print("El numero ",numero," es negativo")
elif numero > 0:
    print("El numero ",numero," es positivo")
else:
    print("El numero ",numero," no es ninguno de los 2")
    
#10
edad = int(input("\nIngrese su edad: "))
if edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")
    
#11
numero = int(input("\nIngrese un entero: "))
if numero < 0:
    print("El numero ",numero," es menor que 0")
elif numero > 0:
    print("El numero ",numero," es mayor que 0")
else:
    print("El numero ",numero," es 0")

#12
x = int(input("\nDigite el primer valor x: "))
y = int(input("\nDigite el segundo valor y: "))
z = int(input("\nDigite el tercer valor z: "))

if x > y and x > z and x != y and x != z:
    print(x," es le numero mayor")
elif y > z and y != z and y != x:
    print(y," es le numero mayor")
elif z != x and z != y:
    print(z," es le numero mayor")
else:
    print("Algunos numero son iguales...")

#13
numero = int(input("\nIngrese un entero: "))
if numero < 0:
    print("El numero ",numero," es menor que 0")
elif numero > 0:
    print("El numero ",numero," es mayor que 0")
else:
    print("El numero ",numero," es 0")
    
#14
numero = int(input("\nIngrese un entero: "))
for i in range(1,11):
    print(numero," x ",i," = ",numero*i)

#15
for i in range(1,10):
    print("El cuadrado de ",i," es: ",i**2)
    
##Tiene pendientes los ejercicios 16,17,18 y 19, pero por el momento no se han podido resolver.
