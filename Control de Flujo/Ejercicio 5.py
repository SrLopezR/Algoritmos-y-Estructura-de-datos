'''5. Se desea escribir un programa para el cálculo del área de diversas superficies: cuadrado, rectángulo, círculo, triángulo y trapecio. 
Seguidamente leerá de la entrada estándar un valor que estará comprendido entre 1 y 5,
indicando el tipo de superficie cuya área se desea calcular.  
El programa leerá entonces los datos que necesite para calcular el área en cuestión. 
El resultado se mostrará en la salida estándar, tras lo cual el programa terminará.
'''

import math
while True:
        print ("═"*40)
        print("Calculo de Superficies:")
        print ("═"*40)
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Círculo")
        print("4. Triángulo")
        print("5. Trapecio")
        print ("═"*40)
        
        try:
            opcion = int(input("Seleccione el número de la figura (1-5): "))
            
            if opcion == 1:  # Cuadrado
                lado = float(input("Ingrese la longitud del lado del cuadrado: "))
                area = lado ** 2
                print(f"El área del cuadrado es: {area:.2f}")
                
            elif opcion == 2:  # Rectángulo
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                area = base * altura
                print(f"El área del rectángulo es: {area:.2f}")
                
            elif opcion == 3:  # Círculo
                radio = float(input("Ingrese el radio del círculo: "))
                area = math.pi * radio ** 2
                print(f"El área del círculo es: {area:.2f}")
                
            elif opcion == 4:  # Triángulo
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                area = (base * altura) / 2
                print(f"El área del triángulo es: {area:.2f}")
                
            elif opcion == 5:  # Trapecio
                base_mayor = float(input("Ingrese la base mayor del trapecio: "))
                base_menor = float(input("Ingrese la base menor del trapecio: "))
                altura = float(input("Ingrese la altura del trapecio: "))
                area = ((base_mayor + base_menor) * altura) / 2
                print(f"El área del trapecio es: {area:.2f}")
                
            else:
                print("Opción no válida. Intente nuevamente.")
                continue
            
            continuar = input("¿Desea calcular otra área? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Por favor ingrese valores válidos.")

