#Ejemplificando la creación de una lista enlazada simple

# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
    
    def cantidadNodos(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def sumaValores(self):
        actual = self.cabeza
        suma = 0
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma
    
    def ImprimirCabeza(self):
        if self.cabeza:
            print("El primer valor de la lista es:", self.cabeza.valor)
        else:
            print("La lista está vacía")
    
    def InsertarInicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo


"""Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente, y no cuando es importado como módulo en otro archivo"""

print("Bienvenido a la lista enlazada")
lista = ListaEnlazada()
case = 0
while case != 9:
    print("")
    print("═"*40)
    print("\n\tSeleccione una opción:")
    print("1. Insertar un valor al inico de la lista")
    print("2. Insertar un valor al final de la lista")
    print("3. Eliminar un valor de la lista")
    print("4. Buscar un valor en la lista")
    print("5. Imprimir la lista")
    print("6. Imprimir la cantidad de nodos")
    print("7. Imprimir la suma de los valores de la lista")
    print("8. Imprimir el primer valor de la lista")
    print("9. Salir\n")
    print("═"*40)
    case = int(input("Seleccione una opción: "))

    if case == 1:
        while True: #Validación de entrada de datos, debe ser un número entero
            try:
                valor = int(input("Ingrese el valor a insertar al inicio: "))
                break
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")
        lista.InsertarInicio(valor)
        print(f"Valor {valor} insertado al inicio de la lista.")
    elif case == 2:
        while True:
            try:
                valor = int(input("Ingrese el valor a insertar al final: "))
                break
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")
        lista.insertar(valor)
        print(f"Valor {valor} insertado al final de la lista.")
    elif case == 3:
        valor = int(input("Ingrese el valor a eliminar: "))
        if lista.eliminar(valor):
            print(f"Valor {valor} eliminado de la lista.")
        else:
            print(f"Valor {valor} no encontrado en la lista.")
    elif case == 4:
        valor = int(input("Ingrese el valor a buscar: "))
        if lista.buscar(valor):
            print(f"Valor {valor} encontrado en la lista.")
        else:
            print(f"Valor {valor} no encontrado en la lista.")
    elif case == 5:
        lista.imprimir()
    elif case == 6:
        cantidad = lista.cantidadNodos()
        print(f"La lista contiene {cantidad} nodos.")
    elif case == 7:
        suma = lista.sumaValores()
        print(f"La suma de los valores de la lista es: {suma}")
    elif case == 8:
        lista.ImprimirCabeza()
    elif case == 9:
        print("Saliendo del programa...")
