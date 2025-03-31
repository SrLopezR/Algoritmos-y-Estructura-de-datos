'''Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número.'''

while True:
        try:
            numero = int(input("Ingrese un número de tres cifras: "))
            
            if 100 <= numero <= 999:
                numero_str = str(numero)
                numero_reves = numero_str[::-1]
                
                if numero_str == numero_reves:
                    print(f"El número {numero} es igual al revés.")
                else:
                    print(f"El número {numero} no es igual al revés.")
            else:
                print("El número debe ser de tres cifras.")
            
            continuar = input("¿Desea ingresar otro número? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Por favor ingrese un número válido.")