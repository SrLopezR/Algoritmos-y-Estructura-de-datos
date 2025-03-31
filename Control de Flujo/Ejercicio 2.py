'''2. Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de un artículo determinado,
 del que se adquieren una o varias unidades. El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad),
   es mayor de 1000, se aplicará un descuento del 12%.'''
while True:
  try:
    prod=input("Ingrese el nombre del producto: ")
    cant=int(input("Ingrese la cantidad del producto: "))
    pre=int(input("Ingrese el precio del producto: C$"))
    sub=cant*pre
    iva=sub *0.15
    desc= sub *0.12
    total = (sub +iva) -desc

    print("═"*40)
    print("\tFactura Comercial\n\n")
    print("Producto: \t  ",prod,"\nCantidad: \t  ",cant,"\nUnidad \t\tC$",pre,"\nSubTotal: \tC$",(sub))
    if sub>1000:
        print("IVA \t\tC$",iva,"\nDescuento \tC$",sub*0.12,"\nTotal: \t\tC$",total,"\n\n")
    else:
      print("IVA  \t\tC$",sub*0.15,"\nTotal \t\tC$",sub+(sub*0.15),"\n\n")
    print("═"*40)

    continuar = input("¿Desea realizar otra factura? (s/n): ")
    if continuar.lower() != 's':
      break
  except ValueError:
    print("Por favor ingrese valores válidos.")
