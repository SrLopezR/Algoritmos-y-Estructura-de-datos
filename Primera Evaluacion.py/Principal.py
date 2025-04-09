from Modulos import *

# Programa Principal
# Iniciamos una lista vacía para guardar los elementos
# Realizamos el menú de opciones
while True:
    print("")
    print("═" * 35)
    print("1. Agregar producto")
    print("2. Agregar stock")
    print("3. Retirar stock producto")
    print("4. Mostrar productos")
    print("5. Salir\n")
    print("═" * 35)
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Pedimos los datos del producto al usuario
        print("Ingrese los datos del producto:")
        # Validamos que el nombre no esté vacío
        while True:
            nombre = input("Nombre del producto: ")
            if nombre.strip() != "":
                break
            else:
                print("El nombre no puede estar vacío. Intente nuevamente.")
        # Validamos que la categoría del producto no esté vacía
        while True:
            categoria = input("Categoria del producto: ")
            if categoria.strip() != "":
                break
            else:
                print("La categoria no puede estar vacía. Intente nuevamente.")
        # Validamos que el precio sea un número positivo
        while True:
            try:
                precio = float(input("Precio del producto: "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser un número positivo. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
        # Validamos que el stock sea un número positivo
        while True:
            try:
                stock = int(input("Stock del producto: "))
                if stock >= 0:
                    break
                else:
                    print("El stock debe ser un número entero positivo. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")
        # Se agrega el producto a la lista de productos
        nuevo_producto = agregar_producto(nombre, categoria, precio, stock)
        print(f"Producto {nuevo_producto.nombre} agregado con éxito.")
        
    elif opcion == "2":
        # Opción para agregar stock
        nombre = input("Nombre del producto a modificar: ")
        # Buscamos el producto en la lista
        producto_encontrado = None
        for producto in productos_lista:
            if producto.nombre.lower() == nombre.lower():
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            # Validamos que la cantidad sea un número positivo
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad a agregar: "))
                    if cantidad > 0:
                        break
                    else:
                        print("La cantidad debe ser un número entero positivo. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número entero.")
            # Se agrega stock al producto
            if agregar_stock(producto_encontrado, cantidad):
                print(f"Se agregaron {cantidad} unidades a {producto_encontrado.nombre}.")
            else:
                print(f"No se pudo agregar stock a {producto_encontrado.nombre}.")
        else:
            print(f"No se encontró el producto con el nombre '{nombre}'.")
            
    elif opcion == "3":
        # Opción para retirar stock
        nombre = input("Nombre del producto a modificar: ")
        # Buscamos el producto en la lista
        producto_encontrado = None
        for producto in productos_lista:
            if producto.nombre.lower() == nombre.lower():
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            # Validamos que la cantidad sea un número positivo
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad a retirar: "))
                    if cantidad > 0:
                        break
                    else:
                        print("La cantidad debe ser un número entero positivo. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número entero.")
            # Se retira stock al producto
            if retirar_stock(producto_encontrado, cantidad):
                print(f"Se retiraron {cantidad} unidades de {producto_encontrado.nombre}.")
            else:
                print(f"No se pudo retirar stock de {producto_encontrado.nombre}. Stock insuficiente.")
        else:
            print(f"No se encontró el producto con el nombre '{nombre}'.")
    
    elif opcion == "4":
        # Opción para mostrar los productos
        print("Productos disponibles:")
        mostrar_productos()
        
    elif opcion == "5":
        # Opción para salir del programa
        print("Gracias por usar el programa.")
        print("Saliendo del programa....")
        break  # Termina el bucle y cierra el programa
    
    else:
        print("Opción no válida. Intente nuevamente.")
