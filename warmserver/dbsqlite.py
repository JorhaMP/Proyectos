#IMportar modulo de bases de datos SQLite
#Este modulo es propio del lenguaje
import sqlite3

# Realizar la conexion
conexion = sqlite3.connect('prueba1.db')

# Crear cursor para ejecutar la consulta
cursor = conexion.cursor() # No es un metodo robusto. no puede manejar grande cantidades de db, tb y registros 1 o 2 los aguanta

# Crear tabla
cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos(
                id_producto interger primary key autoincrement,
                nombre varchar(60),
                description text,
                precio int
               );
               """)
#text es un campo de caracteres de 255
#es necesario en este caso usar siempre al final el ";"

# Guardar cambios
conexion.commit()

#Insertar datos
cursor.execute("INSERT INTO productos VALUES(null, 'Arroz de oro', 'Arroz 95 de grano entero', 550);")
conexion.commit()

# Seleccionar los datos
cursor.execute("select * from productos")
print(cursor) #Muestra la posicion de memoria donde esta el objeto
productos = cursor.fetchall()
print(productos)

#Mostrar cada campo del producto
for producto in productos:
    print(producto)
    
# Mostrar cada campo del producto con un formato especifico:
for producto in productos:
    print("-------------------------------------------")
    print(f"Codigo: {producto[0]}\nNombre: {producto[1]}\nDescripcion: {producto[2]}\nPrecio: {producto[3]}")
    print("-------------------------------------------")
    
# Sacar el primer registro del cursos
cursor.execute("select * from vehiculos where precio >= 300")
productos = cursor.fetchone()
print(productos)

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar varios registros a la vez
productos = [
    ('Celular XYZ','Telefono Movil',360),
    ('Mouse','Teclado con luz',55),
    ('Monitor LCD','Monitor cableado',467)
]
cursor.executemany("insert into productos values(null,?,?,?)",productos)
conexion.commit()

#Modifocar registros
cursor.execute("update productos set nombre = 'Prueba' where precio = 467;" )
conexion.commit()

# Cerrar conexion
conexion.close()

"""POr recomendacion lo mejor es ir cerrando y abriendo las conexiones segun se requiera

conexion = sqlite3.connect('prueba1.db')
cursor.execute("DELETE FROM productos")
conexion.commit()
conexion.close()

"""