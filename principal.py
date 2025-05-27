productos = [["nombre", "categoria", "precio"]]

while True:
    print("\nMenú Principal:")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ").strip()

    # Opción 1: Agregar productos en un bucle que permite seguir cargando
    if opcion == "1":
        while True:  #  Bucle principal que permite agregar varios productos
            # Ingreso del nombre      
            while True:
                nombre_producto = input("Ingresa el nombre del producto: ").strip().lower()
                if nombre_producto == "" :
                    print("El nombre del producto no puede estar vacío.")
                else:      
                    break
                          

            # Ingreso de la categoría
            while True:
                categoria_producto = input("Ingresa la categoría del producto: ").strip().lower()
                if categoria_producto:
                    break
                print("La categoría del producto no puede estar vacía.")            

            # Ingreso del precio
            while True:
                precio_producto = input("Ingresa el precio del producto: ").strip()
                if precio_producto.isdigit():
                    precio_producto = int(precio_producto)
                    if precio_producto > 0:
                        break
                    print("El precio no puede ser cero.")
                else:
                    print("El precio no es válido (debe ser un número entero y no negativo).")

            # Cargar sublista a la lista principal
            productos.append([nombre_producto, categoria_producto, precio_producto])

            # Preguntar si el usuario quiere seguir cargando productos
            while True:
                salida = input("¿Deseas agregar otro producto? (Ingrese s/n): ").strip().lower()
                if salida == "n":
                    print("Carga de productos completa.")
                    print(productos)
                    break  # Ahora rompe el bucle de carga de productos y regresa al menú
                elif salida == "s":
                    break  # Ahora rompe solo la pregunta, pero deja el bucle principal activo
                else:
                    print("La respuesta no es válida.")
                    continue 

            if salida == "n":
                break
              #Rompe el bucle principal y regresa al menú

      

    # Opción 2: Mostrar productos
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos cargados.\n")
        else:
            print("Productos cargados:")
            
            indice = 0
            for producto in productos:
                nombre = producto[0]
                categoria = producto[1]
                precio = producto[2]
                print(f"{indice}. Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")
                indice += 1
            
            print()  # Línea en blanco para mejorar la presentación.

        continue  # Regresar al menú

    # Opción 3: Buscar producto
    elif opcion == "3":
        busqueda = input("Ingresa el nombre del producto a buscar: ").strip().lower()
        productos_encontrados = []
        
        for producto in productos:
            if busqueda in producto[0].lower():
                productos_encontrados.append(producto)
        
        if len(productos_encontrados) == 0:
            print("No se encontraron resultados.\n")
        else:
            print("Productos encontrados:")
            for prod in productos_encontrados:
                nombre = prod[0]
                categoria = prod[1]
                precio = prod[2]
                print(f"Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")
            print()

        continue  # Regresar al menú

    # Opción 4: Eliminar producto
    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos para eliminar.\n")
        else:
            print("Productos cargados:")
            
            indice = 0
            for producto in productos:
                nombre = producto[0]
                categoria = producto[1]
                precio = producto[2]
                print(f"{indice}. Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")
                indice += 1
            print()
            
            while True:
                pos_eliminar = input("Ingresa la posición (número) del producto a eliminar: ").strip()
                
                if pos_eliminar.isdigit():
                    pos = int(pos_eliminar)
                    if 0 < pos < len(productos):
                        break
                
                print("Posición inválida. Intenta nuevamente.")  # Mensaje de error si es inválido

            # Eliminamos el producto
            producto_eliminado = productos.pop(pos)
            print(f"Producto eliminado: Nombre: {producto_eliminado[0]}, Categoría: {producto_eliminado[1]}, Precio: ${producto_eliminado[2]}\n")

        continue  # Regresar al menú

    # Opción 5: Salir del programa
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta la vista!")
        break

    # Opción inválida
    else:
        print("Opción inválida. Por favor, selecciona una opción del 1 al 5.\n")
        continue  # Regresar al menú si la opción no es válida