#Diccionario inicial de productos con detalle.
productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
} 

#Diccionario inicial del stock de productos con precio y cantidad.
stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}

#Opcion 1.
def unidades_categoria(categoria):
    total = 0
    cat_buscar = categoria.strip().lower()
    for sku in productos:
        if productos[sku][1].lower() == cat_buscar:
            total += stock[sku][1]
    print(f"El total de unidades disponibles es: {total}")

#Opcion 2.
def busqueda_precio(p_min, p_max):
    resultados = []
    for sku in stock:
        precio = stock[sku][0]
        unidades = stock[sku][1]
        if precio >= p_min and precio <= p_max and unidades > 0:
            nombre = productos[sku][0]
            resultados.append(f"{nombre}--{sku}")
    if len(resultados) > 0:
        resultados.sort()
        print(f"Productos encontrados: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")

#Opcion 3.
def actualizar_precio(codigo, nuevo_precio):
    sku = codigo.strip().upper()
    if sku in stock:
        stock[sku][0] = nuevo_precio
        return True
    return False

#Validadores para opcion 4.
def validar_codigo(codigo):
    sku = codigo.strip().upper()
    return sku != "" and sku not in productos

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(nombre_categoria):
    return nombre_categoria.strip() != ""

def validar_nombre_marca(nombre_marca):
    return nombre_marca.strip() != ""

def validar_peso(peso):
    try:
        return float(peso) > 0
    except ValueError:
        return False

def validar_importado(opcion):
    return opcion.strip().lower() in ['s', 'n']

def validar_es_para_cachorro(opcion):
    return opcion.strip().lower() in ['s', 'n']

def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def validar_unidades(unidades):
    try:
        return int(unidades) >= 0
    except ValueError:
        return False

#Opcion 4.
def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    print("\n=Agregar producto")
    sku = codigo.strip().upper()
    if sku in productos:
        return False
        
    productos[sku] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[sku] = [precio, unidades]
    return True

#Opcion 5.
def eliminar_producto(sku):
    print("\n=Eliminar producto=")
    codigo = sku.strip().upper()
    if codigo in productos:
        del productos[codigo]
        del stock[codigo]
        return True
    return False

#Menu principal.
def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")
        
        opcion = input("Elija una opción: ").strip()
        
        if opcion == "1":
            print("\n=Buscar producto por categoria=")
            cat = input("Ingrese categoría a consultar: ")
            unidades_categoria(cat)
            
        elif opcion == "2":
            print("\n=Buscar producto por precio=")
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("Debe ingresar valores enteros")
                
        elif opcion == "3":
            print("\n=Actualizacion de productos=")
            while True:
                cod = input("Ingrese código del producto: ")
                try:
                    nuevo_p = int(input("Ingrese nuevo precio: "))
                    if actualizar_precio(cod, nuevo_p):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                except ValueError:
                    print("Debe ingresar valores enteros")
                
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp == "n":
                    break

        elif opcion == "4":
            prod = input("Ingrese código del producto: ")
            if not validar_codigo(prod):
                print("Error: El código está vacío o ya existe en el sistema.")
                continue
                
            name = input("Ingrese nombre: ")
            if not validar_nombre(name):
                print("Error: El nombre no puede estar vacío.")
                continue
                
            category = input("Ingrese categoría: ")
            if not validar_categoria(category):
                print("Error: La categoría no puede estar vacía.")
                continue
                
            brand = input("Ingrese marca: ")
            if not validar_nombre_marca(brand):
                print("Error: La marca no puede estar vacía.")
                continue
                
            weight = input("Ingrese peso (kg): ")
            if not validar_peso(weight):
                print("Error: El peso debe ser un número mayor a cero.")
                continue
            weight_float = float(weight)
                
            imported = input("¿Es importado? (s/n): ")
            if not validar_importado(imported):
                print("Error: Debe ingresar 's' o 'n'.")
                continue
            product_imported = True if imported.strip().lower() == 's' else False
                
            puppy = input("¿Es para cachorro? (s/n): ")
            if not validar_es_para_cachorro(puppy):
                print("Error: Debe ingresar 's' o 'n'.")
                continue
            puppy_product = True if puppy.strip().lower() == 's' else False
                
            price = input("Ingrese precio: ")
            if not validar_precio(price):
                print("Error: El precio debe ser un entero mayor a cero.")
                continue
            price_int = int(price)
                
            unit = input("Ingrese unidades: ")
            if not validar_unidades(unit):
                print("Error: Las unidades deben ser un entero mayor o igual a cero.")
                continue
            unit_int = int(unit)
            
            if agregar_producto(prod, name, category, brand, weight_float, product_imported, puppy_product, price_int, unit_int):
                print("Producto agregado")
            else:
                print("El código ya existe")
                
        elif opcion == "5":
            cod_eliminar = input("Ingrese código del producto a eliminar: ")
            if eliminar_producto(cod_eliminar):
                print("Producto eliminado")
            else:
                print("El código no existe")
                
        elif opcion == "6":
            print("Programa finalizado.")
            break
            
        else:
            print("Debe seleccionar una opción válida")

# Para realizar la ejecucion del programa
if __name__ == "__main__":
    menu_principal()
