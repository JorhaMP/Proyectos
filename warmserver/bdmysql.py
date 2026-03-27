import mysql.connector

# Conexión a la base de datos MySQL
    #Por deffault el puerto es 3306, si se desea cambiar se debe agregar el parametro port="puerto" en la función mysql.connector.connect()
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba1"
)

# Verificar la conexión
print(str(database))

# Crear un cursor para ejecutar consultas sql/Buffered = True permite a la variable cursor ejecutar varias consultas sin necesidad de cerrar la conexión, es decir, permite mantener la conexión abierta para ejecutar múltiples consultas sin tener que volver a conectarse cada vez.
cursor = database.cursor(buffered=True)

# Crear la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS prueba2")

# Ejecutando consultas SQL
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int auto_increment not null,
    marca varchar(40)  not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo primary key(id)
)
""") #Dado que el curso le pertenece a la base de datos prueba1, la sentencia se creara en la bd prueba1

cursor.execute("SHOW TABLES")
for tb in cursor:
    print(tb)
    

cursor.execute("DELETE FROM vehiculos")
database.commit()

# Insertar en la base de datos
cursor.execute("INSERT INTO vehiculos values(dafault,'Nissan','Murano',15500)")
database.commit() # Para cerrar el query y que los cambios queden ejecutados

carros = [
    ('Hyundai','Sonata',15000),
    ('Honda','Accord',14000),
    ('Toyoto','Hilux',25000),
    ('Mercedes','GLE',35000)
]

cursor.executemany("INSERT INTO vehiculos values(null, %s, %s, %s)",carros) 
# executemany se usa para ejecutar varias veces el query, en el caso de %s es para que tome los datos de la tupla carros en cada iteracion
database.commit()

# Seleccionar informacion de la tabla

cursor.execute("SELECT * FROM vehiculos")
resultado = cursor.fetchall() # envia el dato obtenido desde el cursos a la variable resultado...
print(resultado)
print("Primer ejemplo de select: ")
for carro in resultado:
    print(carro) # Muestra cada uno de los registros uno por uno

print("Segundo ejemplo de select: ")
for carro in resultado:
    print(carro[1]) # Muestor una posicion en especifico de la tupla, en este caso solo la posicion 1 (Marca)
    
# Tercer ejemplo, seleccionar una posicion especifica de la tabla y traerla
cursor.execute(("SELECT marca FROM vehiculos"))
resultado = cursor.fetchall
print("Tercer Ejemplo de select: ")
for carro in resultado:
    print(carro)

# Cuarto ejemplo seleccionar con where
cursor.execute("select * from vehiculos where precio <=15000")
resultado = cursor.fetchall
for carro in resultado:
    print(carro[1],carro[2],carro[3])
# Seleccionar solo uno de los resultados obtenidos
cursor.execute("SELECT * FROM vehiculos")
resultado = cursor.fetchone()
print("Solamente el primer registro")
print(resultado)

# Eliminar vehiculos
cursor.execute("DELETE FROM vehiculos where marca='Toyota")
database.commit()

# Mostar cantidad de registro afectados
print(cursor.rowcount, " eliminados exitosamente")

# Actualizar
cursor.execute("UPDATE vehiculos set marca='Tesla where marca='Hyundai'")
database.commit()
print(cursor.rowcount, " actualizados en total")