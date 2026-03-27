def es_sqlite(conn):
    import sqlite3
    return isinstance(conn, sqlite3.Connection)

def menu_operaciones(conn):
    while True:
        print("\n===== MENÚ DE OPERACIONES =====")
        print("1. Insertar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar(conn)
        elif opcion == "2":
            listar(conn)
        elif opcion == "3":
            buscar(conn)
        elif opcion == "4":
            actualizar(conn)
        elif opcion == "5":
            eliminar(conn)
        elif opcion == "6":
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("⚠️ Opción inválida")
            
            
def insertar(conn):
    try:
        print("\n\n-------------Agregando Nuevo Producto...-----------------")
        nombre = input("Ingrese el Nombre del producto: ")

        cantidad = int(input("Ingrese la Cantidad disponible del producto: "))
        if cantidad < 0:
            print("❌ La cantidad no puede ser negativa")
            return

        precio = float(input("Ingrese el Precio del producto (USE \".\" para separa los decimales): "))
        if precio <= 0:
            print("❌ El precio debe ser positivo")
            return

        cursor = conn.cursor()

        if es_sqlite(conn):
            cursor.execute(
                "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                (nombre, cantidad, precio)
            )
        else:
            cursor.execute(
                "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)",
                (nombre, cantidad, precio)
            )

        conn.commit()
        print("\n---------------------------------------------")
        print("✅ Producto insertado correctamente")
        print(f"Informacion del producto: \nNombre: {nombre} \nCantidad: {cantidad} \nPrecio: {precio}")

    except Exception as e:
        print("❌ Error al insertar:", e)

def listar(conn):
    try:
        print("\n\n-------------Enlistando productos...-----------------")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")

        productos = cursor.fetchall()

        if not productos:
            print("📭 No hay productos")
            return

        print("\n📦 LISTA DE PRODUCTOS")
        for p in productos:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[2]} | Precio: {p[3]}")

    except Exception as e:
        print("❌ Error al listar:", e)
        
def buscar(conn):
    try:
        print("\n\n-------------Buscando producto...-----------------")
        nombre = input("Ingrese nombre a buscar: ")

        cursor = conn.cursor()

        if es_sqlite(conn):
            cursor.execute(
                "SELECT * FROM productos WHERE nombre LIKE ?",
                ('%' + nombre + '%',)
            )
        else:
            cursor.execute(
                "SELECT * FROM productos WHERE nombre LIKE %s",
                ('%' + nombre + '%',)
            )

        resultados = cursor.fetchall()

        if resultados:
            print("\n🔍 RESULTADOS")
            for p in resultados:
                print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[2]} | Precio: {p[3]}")
        else:
            print("❌ No se encontraron productos")

    except Exception as e:
        print("❌ Error en búsqueda:", e)
        
def actualizar(conn):
    running = True
    try:
        print("\n\n-------------Actualizando un producto...-----------------")
        while running:
        
            id_prod = input("Ingrese ID del producto a actualizar: ")

            #catch id producto
            try:
                id_prod = int(id_prod)
                
                if id_prod < 0:
                    print("❌ El id no puede ser negativo...")
                
                else:
                    running = False
                
            except Exception as e:
                if id_prod == "":
                    running = False
                    print("Actualizacion Cancelada...")
                    
                print("❌ Debe ingresar valores validos...")
            
        cursor = conn.cursor()

        if es_sqlite(conn):
            cursor.execute("SELECT * FROM productos WHERE id = ?", (id_prod,))
        else:
            cursor.execute("SELECT * FROM productos WHERE id = %s", (id_prod,))

        producto = cursor.fetchone()

        if not producto:
            print("❌ Producto no existe")
            return
        else:
            print(f"\nID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[2]} | Precio: {producto[3]}\n")
            print("Debe dejar vacio si no desea cambiar un valor")

            nuevo_nombre = str(input("Nuevo NOMBRE para el producto: ")) or producto[1] #sino toma el valor guardado en la lista
            
            #catch de cantidad------------------------------------------------------------------------------------------
            play = True
            while play:
                try:
                    nueva_cantidad = input("Nueva CANTIDAD para el producto: ")
                except Exception as e:
                    print("")
                
                if nueva_cantidad == "":
                    nueva_cantidad = producto[2] #sino toma el valor guardado en la lista
                    play = False
                else:
                    try:
                        nueva_cantidad = int(nueva_cantidad)
                        if nueva_cantidad < 0:
                            print("❌ Cantidad no puede ser negativa")
                        else:
                            play = False
                    except Exception as e:
                        print("❌ Cantidad debe ser un valor ENTERO")
                        
            #catch de precio------------------------------------------------------------------------------------------
            play = True
            while play:
                try:
                    nuevo_precio = input("Nuevo PRECIO para el producto (USE \".\" para separa los decimales): ")
                except Exception as e:
                    print("")
                
                if nuevo_precio == "":
                    nuevo_precio = producto[3] #sino toma el valor guardado en la lista
                    play = False
                else:
                    try:
                        nuevo_precio = float(nuevo_precio)
                        if nuevo_precio < 0:
                            print("❌ Cantidad no puede ser negativa")
                        else:
                            play = False
                    except Exception as e:
                        print("❌ Cantidad debe ser un valor FLOTANTE")
                
                """
                try:
                    
                except Exception as e:
                    print("")
                    
                if nuevo_precio == "":
                    nuevo_precio = producto[3] #sino toma el valor guardado en la lista
                else:
                    nuevo_precio = float(nuevo_precio)
                    if nuevo_precio <= 0:
                        print("❌ El precio no puede ser negattio")
                        return
                """
            # Actualizar
            if es_sqlite(conn):
                cursor.execute(
                    "UPDATE productos SET nombre=?, cantidad=?, precio=? WHERE id=?",
                    (nuevo_nombre, nueva_cantidad, nuevo_precio, id_prod)
                )
            else:
                cursor.execute(
                    "UPDATE productos SET nombre=%s, cantidad=%s, precio=%s WHERE id=%s",
                    (nuevo_nombre, nueva_cantidad, nuevo_precio, id_prod)
                )

            conn.commit()
            print("✅ Producto actualizado exitosamente")

    except Exception as e:
        print("❌ Error al actualizar:", e)
        
def eliminar(conn):
    try:
        print("\n\n-------------Eliminando producto...-----------------")
        play = True
        while play:
            try:
                id_prod = int(input("Ingrese ID del producto a eliminar: "))
                
                if id_prod <= 0:
                    print ("❌ El ID debe ser un valor entero positivo")
                else:
                    play = False
                
            except Exception as E:
                if id_prod =="":
                    play = False
                print("❌ Ingrese valores validos... | ",e)
        
        confirm = input(f"¿Seguro que desea eliminar {id_prod}? (s/n): ")
        if confirm.lower() != "s":
            print("Eliminacion cancelada")
            return

        cursor = conn.cursor()

        if es_sqlite(conn):
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
        else:
            cursor.execute("DELETE FROM productos WHERE id = %s", (id_prod,))

        if cursor.rowcount == 0:
            print("❌ Producto no encontrado")
        else:
            conn.commit()
            print("🗑️ Producto eliminado")

    except Exception as e:
        print("❌ Error al eliminar:", e)