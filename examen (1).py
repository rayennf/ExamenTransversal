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


def stock_marca(marca):
  while True:
    mca=input("ingrese nombre de la marca")
    if mca.isalpha():
       break
    else:
       print("ingrese solo letras")
       for clave, valor in productos:
          
          print()
    

def listadeproducto():
  print("--------Lista de Notebooks Ordenados--------")
  for clave, valor in productos.items():
    print(f"{valor[0]},{clave},{valor[2]},{valor[4]}")



def buscar_precio():
  while True:
    try:
      precio_min=int(input("ingrese el precio minimo: "))
      if precio_min:
        break
    except ValueError:
      print("debe ingresar valores entero!!")

      while True:
        try:
          precio_max=float(input("ingrese el precio maximo: "))
          if precio_max > precio_min:
             break
          print("debe ingresar un valor mayor al precio minimo")
        except ValueError:
           print("debe ingresar valores enteros!!")
        for clave, valor in stock.items():
           if valor[0]>= precio_min and valor[0]<=precio_max:
              if valor[1]>0:
                 break
              for clave, valor in productos.items():
                    print()
                   

                   
               

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