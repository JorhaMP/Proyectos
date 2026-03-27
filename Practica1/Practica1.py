import mysql.connector

# Conexión a la base de datos MySQL
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba1"
)

cursor = database.cursor(buffered=True)

# Crear la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS NetHBO")
database.commit()
database.close()

# Reinicio de la conexion

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="NetHBO"
)
cursor = database.cursor(buffered=True)
