class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

# Lista global de productos
productos_lista = []

def agregar_producto(nombre, categoria, precio, stock):
    nuevo_producto = Producto(nombre, categoria, precio, stock)
    #El nuevo producto se agrega a la lista de productos, tomando las caracteristicas definidas en la clase Producto
    productos_lista.append(nuevo_producto)
    return nuevo_producto

def agregar_stock(producto, cantidad):
    producto.stock += cantidad
    return True
    
def retirar_stock(producto, cantidad):
    #Se devuelve True si el stock es suficiente para retirar la cantidad solicitada
    #De lo contrario, se devuelve False
    #Esto se debe a que el proceso de retirar es un bucle y segun el resultado se ejecuta o no
    if producto.stock >= cantidad:
        producto.stock -= cantidad
        return True
    else:
        return False
    
def mostrar_productos():
    if productos_lista:
        for producto in productos_lista:
            print(f"Nombre: {producto.nombre}, Categoria: {producto.categoria}, Precio: {producto.precio}, Stock: {producto.stock}")
    else:
        print("No hay productos disponibles.")

