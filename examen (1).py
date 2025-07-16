productos = {
                '8475HD'  : ['HP'  , 15.6, '8GB' ,  'DD',  '1T'   , 'Intel Core i5', 'Nvidia GTX1050'],
                '2175HD'  : ['Acer', 14,   '4GB' ,  'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                'JjfFHD'  : ['Asus', 14,   '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                'fgdxFHD' : ['HP'  , 15.6, '8GB' ,  'DD',  '1T'   , 'Intel Core i3', 'integrada'],
                'GF75HD'  : ['Asus', 15.6, '8GB' ,  'DD',  '1T'   , 'Intel Core i7', 'Nvidia GTX1050'],
                '123FHD'  : ['Acer', 14,   '6GB' ,  'DD',  '1T'   , 'AMD Ryzen 5'  , 'integrada'],
                '342FHD'  : ['Acer', 15.6, '8GB' ,  'DD',  '1T'   , 'AMD Ryzen 7'  , 'Nvidia GTX1050'],
                'UWU131HD': ['Dell', 15.6, '8GB' ,  'DD',  '1T'   , 'AMD Ryzen 3'  , 'Nvidia GTX1050'],
            }

stock =    {   '8475HD'  : [387990,10], 
               '2175HD'  : [327990,4], 
               'JjfFHD'  : [424990,1],
               'fgdxFHD' : [664990,21], 
               '123FHD'  : [290890,32], 
               '342FHD'  : [444990,7],
               'GF75HD'  : [749990,2], 
               'UWU131HD': [349990,1], 
               'FS1230HD': [249990,0], 
            }


def stock_marca():
    while True:
        mca = input("Ingrese nombre de la marca: ").capitalize()
        if mca.isalpha():
            break
        else:
            print("Ingrese solo letras.")
    
    print(f"Productos de la marca {mca}:")
    print("Código\t\tStock\t\tPrecio")
    print("========================================")
    encontrado = False
    for clave, valor in productos.items():
        if valor[0] == mca:
            if clave in stock:
                print(f"{clave}\t\t{stock[clave][1]}\t\t${stock[clave][0]}")
                encontrado = True
    if not encontrado:
        print("No se encontraron productos de esa marca.")

def listadeproducto():
    print("-------- Lista de Notebooks Ordenados --------")
    print("Marca\t\tCódigo\t\tRAM\t\tDisco")
    print("==============================================")
    for clave, valor in sorted(productos.items(), key=lambda x: x[1][0]):
        print(f"{valor[0]}\t\t{clave}\t\t{valor[2]}\t\t{valor[4]}")



def buscar_precio():
    while True:
        try:
            precio_min = int(input("Ingrese el precio mínimo: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    while True:
        try:
            precio_max = int(input("Ingrese el precio máximo: "))
            if precio_max > precio_min:
                break
            else:
                print("El precio máximo debe ser mayor que el mínimo.")
        except ValueError:
            print("Debe ingresar un número entero válido.")

    print("\nProductos en ese rango de precios:")
    print("Código\t\tPrecio\t\tStock")
    print("========================================")
    encontrado = False
    for clave, datos in stock.items():
        precio, cantidad = datos
        if precio_min <= precio <= precio_max and cantidad > 0:
            print(f"{clave}\t\t${precio}\t\t{cantidad}")
            encontrado = True
    if not encontrado:
        print("No se encontraron productos en ese rango.")

                   

                   
               

def menu():   
  
  while True:
    print('MENÚ PRINCIPAL ')
    print('====================================')
    print('1. Stock marca.')
    print('2. busqueda por precio.')
    print('3. listado de productos.')
    print('4. Salir.')
    opc=input('Ingrese Opción: ')
    if opc=='1':
       stock_marca()
    elif opc=='2':
         buscar_precio()
    elif opc=='3':
        listadeproducto()
    elif opc=='4':
        print('Programa finalizado')
        break
    else:
        print('Opción Incorrecta')
    
menu()