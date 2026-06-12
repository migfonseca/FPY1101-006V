#Sistema de gestion de ventas

#Valores
def calcular_subtotal(precio, cantidad):
    return precio*cantidad

def calcular_descuento(subtotal):
    if subtotal>=100000:
        return subtotal*0.15
    elif subtotal>=50000 and subtotal<100000:
        return subtotal*0.10
    else:
        return 0
    
def calcular_iva(monto):
    return monto*0.19

def calcular_total(subtotal,descuento,iva):
    return subtotal - descuento + iva

def mostrar_resumen(producto,precio,cantidad,subtotal,
                    descuento,iva,total):
                        
#Muestra del resumen de la compra
    print("\n===RESUMEN DE COMPRA===")
    print(f"-Nombre del producto: {producto} ")
    print(f"-Precio unitario: {precio}$")
    print(f"-Cantidad comprada: {cantidad}")
    print(f"-Subtotal: ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"IVA: {iva}$")
    print(f"Total a pagar: ${total}")

#Acumulador de las ventas
valor_acumulado=0

while True:
    print("\n====SISTEMA GESTION DE VENTAS====")
    print("\n1-Registrar venta.")
    print("2-Mostrar total de ventas acumuladas.")
    print("3-Salir.")

    try:
        opcion = int(input("\n=Elija una opcion: "))

        #Opcion 1
        if opcion == 1:

            producto=input("\nIngrese nombre del producto: ")
            precio=float(input("Ingrese precio unitario: "))
            cantidad=int(input("Ingrese cantidad: "))

            subtotal = calcular_subtotal(precio,cantidad)
            descuento = calcular_descuento(subtotal)

            #Calcular iva y total
            iva = calcular_iva(subtotal - descuento)

            total = calcular_total(subtotal,descuento,iva)

            valor_acumulado += total

            mostrar_resumen(
                producto,
                precio,
                cantidad,
                subtotal,
                descuento,
                iva,
                total
            )

        #Opcion 2
        elif opcion == 2:
            print(f"\n=Total ventas acumuladas: ${valor_acumulado}")

        #Opcion 3
        elif opcion == 3:
            print("\n=Saliendo del programa...")
            break

        #Alerta de termino invalido
        else:
            print("¡Ingrese una opcion valida!")
    except ValueError:
        print ("¡ERROR! Ingrese un numero entero valido.")
