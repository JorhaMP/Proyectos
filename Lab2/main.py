import csv
from sql_carpeta import mysql_wamserver
from sql_carpeta import sqllite
from crud import *

def main():
    
    print("Bienvenido al lab 2 de Lenguajes para aplicaciones comerciales")
    
    mysql_wamserver.inicio()
    sqllite.inicio()

    mysql_conn = None
    sqlite_conn = None
    
    while True:
        print(f"\n===== Bienvenido al sistema =====")
        print("1. Usar MySQL")
        print("2. Usar SQLite")
        print("3. Sincronizar MySQL → SQLite")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mysql_conn = mysql_wamserver.conectar_mysql()
            if mysql_conn:
                mysql_wamserver.crear_tb()
                menu_operaciones(mysql_conn)

        elif opcion == "2":
            sqlite_conn = sqllite.conectar_sqlite()
            if sqlite_conn:
                sqllite.crear_tb()
                menu_operaciones(sqlite_conn)

        elif opcion == "3":
            if not mysql_conn:
                mysql_conn = mysql_wamserver.conectar_mysql()
                mysql_wamserver.crear_tb()
            if not sqlite_conn:
                sqlite_conn = sqllite.conectar_sqlite()
                sqllite.crear_tb()

            if mysql_conn and sqlite_conn:
                sincronizar(mysql_conn, sqlite_conn)
                            
        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opcion no valida")
    

def sincronizar(mysql_conn, sqlite_conn):
    try:
        print("\n🔄 Sincronizacion iniciada...")

        mysql_cursor = mysql_conn.cursor()
        sqlite_cursor = sqlite_conn.cursor()

        # Obtenciond e datos
        mysql_cursor.execute("SELECT * FROM productos")
        productos_mysql = {p[0]: p for p in mysql_cursor.fetchall()}

        sqlite_cursor.execute("SELECT * FROM productos")
        productos_sqlite = {p[0]: p for p in sqlite_cursor.fetchall()}

        insert_mysql = 0 #INserts hechos en mysql
        insert_sqlite = 0 #INserts hechos en sqlite
        actualizados = 0 #actualizaciones hechas

        # REcorrrido de las id para buscar que se tiene
        todos_ids = set(productos_mysql.keys()) | set(productos_sqlite.keys()) # devuelve solo las keys de los diccionarios

        for id_p in todos_ids:

            prod_mysql = productos_mysql.get(id_p)
            prod_sqlite = productos_sqlite.get(id_p)

            #caso donde solo existen en mysql... en este caso sincroniza hacia sqlite
            if prod_mysql and not prod_sqlite:
                sqlite_cursor.execute(
                    "INSERT INTO productos (id, nombre, cantidad, precio) VALUES (?, ?, ?, ?)",
                    prod_mysql
                )
                insert_sqlite += 1

            #caso donde existe en sqlite pero no en mysql
            elif prod_sqlite and not prod_mysql:
                mysql_cursor.execute(
                    "INSERT INTO productos (id, nombre, cantidad, precio) VALUES (%s, %s, %s, %s)",
                    prod_sqlite
                )
                insert_mysql += 1

            #caso donde el producto existe en ambos, por tanto es necesaria una actualizacion
            else:
                # Comparacion der datos
                if prod_mysql[1:] != prod_sqlite[1:]:

                    # ESTRATEGIA USADA: Se busca el que tenga mayor cantidad y se usa este
                    if prod_mysql[2] >= prod_sqlite[2]:
                        # actualizar sqlite
                        sqlite_cursor.execute(
                            "UPDATE productos SET nombre=?, cantidad=?, precio=? WHERE id=?",
                            (prod_mysql[1], prod_mysql[2], prod_mysql[3], id_p)
                        )
                    else:
                        # actualizar mysql
                        mysql_cursor.execute(
                            "UPDATE productos SET nombre=%s, cantidad=%s, precio=%s WHERE id=%s",
                            (prod_sqlite[1], prod_sqlite[2], prod_sqlite[3], id_p)
                        )

                    actualizados += 1

        #Guardar cambios
        mysql_conn.commit()
        sqlite_conn.commit()

        print("\n✅ Sincronización completada")
        print(f"📥 Insertados en SQLite: {insert_sqlite}")
        print(f"📥 Insertados en MySQL: {insert_mysql}")
        print(f"🔄 Registros actualizados: {actualizados}")

    except Exception as e:
        print("❌ Error en sincronización:", e)


if __name__ == "__main__":
    main()