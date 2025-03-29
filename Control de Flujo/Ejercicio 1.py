'''1. Desarrolla un programa que calcule el importe a pagar por un vehículo al circular por una autopista. 
El vehículo puede ser una bicicleta, una moto, un carro o un camión. 
Para definir el conjunto de vehículos deben utilizar una estructura adecuada. 
El importe se calculará según los siguientes datos:

a) Un importe fijo de 100 córdobas para la bicicleta.
b) Las motos y los carros pagarán 30 córdobas por Km.
c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas.
'''
bandera = False
while bandera == False:
    print("Seleccione el tipo de vehiculo segun se le indica")
    opc=input("A) Bicicleta\nB)Moto o Vehiculo Liviano\nC)Vehiculo Pesado\n->")
    print("═"*35)
    if opc.lower() == "a":
        print("Las bicicletas tienen un importe fijo, Pague C$100")
        sig=int(input("Desea calcular otro importe?\n1)Si\n2)No\n->"))
        if sig == 1:
            bandera = False
        else:
            bandera= True
    if opc.lower() == "b":
        km=int(input("Ingrese la cantida de Kilometros recorridos: "))
        print("Debe pagar C$",km*30)
        sig=int(input("Desea calcular otro importe?\n1)Si\n2)No\n->"))
        if sig == 1:
            bandera = False
        else:
            bandera= True
    if opc.lower() == "c":
        km=int(input("Ingrese la cantida de Kilometros recorridos: "))
        tn=int(input("Ingrese las toneladas del Camion: "))
        print("Debe pagar C$",(km*30)+(tn*25))
        sig=int(input("Desea calcular otro importe?\n1)Si\n2)No\n->"))
        if sig == 1:
            bandera = False
        else:
            bandera= True