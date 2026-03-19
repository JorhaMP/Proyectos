"""
Laboratorio 1

Curso: Lenguajes para Aplicaciones Comerciales

Estudiante: Jorhany Marin Perez
Carnet: B94541
Profesor: James Mcintosh Molina

"""
def main():
    print("Ejercicio 1: Conjuntos Frozenset")
    ejercicio1()

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
        
        
        
if __name__ == "__main__":
    main()