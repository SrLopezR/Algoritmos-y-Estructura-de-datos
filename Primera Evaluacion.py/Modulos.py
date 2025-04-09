
class productos:
    def __init__(self, nombre, categoria, precio, stock):
        self.productos = productos
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

def agregar_producto(nombre, categoria, precio, stock):
    nuevo_producto = productos(nombre, categoria, precio, stock)
    return nuevo_producto

def agregar_stock(producto, cantidad):
    producto.stock += cantidad
    return True
    
def retirar_stock(producto, cantidad): #Se verifica que la cantidad del producto sea suficiente para retirar stock
    if producto.stock >= cantidad:
        producto.stock -= cantidad
        return True
    else:
        return False
    
def mostrar_productos(productos):
    for producto in productos:
        print(f"Nombre: {producto.nombre}, Categoria: {producto.categoria}, Precio: {producto.precio}, Stock: {producto.stock}")
    #Se muestra la lista de productos