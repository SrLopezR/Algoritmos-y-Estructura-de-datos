'''3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario.
Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3.
Diseñe un programa que determine el monto de la compra, el monto del descuento, 
el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.'''

while True:
        try:
            docenas = int(input("Ingrese la cantidad de docenas compradas: "))
            precio_por_docena = float(input("Ingrese el precio por docena: "))
            
            
            monto_compra = docenas * precio_por_docena
            
         
            if docenas > 3:
                descuento = monto_compra * 0.15
                unidades_obsequio = docenas - 3
            else:
                descuento = monto_compra * 0.10
                unidades_obsequio = 0
                
            monto_con_descuento = monto_compra - descuento
            
           
            print(f"Monto de la compra: ${monto_compra:.2f}")
            print(f"Descuento aplicado: ${descuento:.2f}")
            print(f"Monto a pagar: ${monto_con_descuento:.2f}")
            print(f"Unidades obsequiadas: {unidades_obsequio} unidades")
            
            continuar = input("¿Desea realizar otro cálculo? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Por favor ingrese valores válidos.")
