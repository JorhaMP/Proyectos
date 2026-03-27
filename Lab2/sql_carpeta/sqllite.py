import sqlite3

def inicio():

    conexion = sqlite3.connect('inventario.db')

    # Crear cursor para ejecutar la consulta
    cursor = conexion.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    print("Prueba de cursor y la conexion en sqllite3")
    
    tablas = cursor.fetchall()
    
    print(tablas)

    if tablas:
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla[0])
    else:
        print("No hay tablas creadas aún")

    conexion.close()
    
def conectar_sqlite():
    try:
        conexion = sqlite3.connect("inventario.db")
        print("✅ Conectado a SQLite")
        return conexion
    except Exception as e:
        print("❌ Error SQLite:", e)
        return None
    
def crear_tb():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER not null,
        nombre TEXT  not null,
        cantidad INTEGER not null,
        precio REAL not null,
        CONSTRAINT pk_productos primary key(id)
    );
                   """)