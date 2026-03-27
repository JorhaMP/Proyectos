import mysql.connector

def inicio ():

    # Conexión a la base de datos MySQL
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="prueba1"
    )


    cursor = database.cursor(buffered=True)

    # Crear la base de datos
    cursor.execute("CREATE DATABASE IF NOT EXISTS inventario")
    database.commit()
    database.close()

    # Reinicio de la conexion

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventario"
    )
    cursor = database.cursor(buffered=True)
    
    cursor.execute("SHOW DATABASES")
    print("Prueba de cursor y la conexion en mysqll")
    for bd in cursor:
        print(bd)
    
    database.commit()
    database.close()

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventario"
        )
        print("✅ Conectado a MySQL")
        return conexion
    except Exception as e:
        print("❌ Error MySQL:", e)
        return None

def crear_tb():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventario"
    )
    cursor = database.cursor(buffered=True)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id int auto_increment not null,
        nombre varchar(40)  not null,
        cantidad integer not null,
        precio float(10,2) not null,
        CONSTRAINT pk_productos primary key(id)
    )
                   """)
    
