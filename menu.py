from validates import *

def cargar_producto(inventario:list)->list:
    '''
    Carga un nuevo producto al invetario.
    Parametro: inventario (list)
    Retorno: inventario (list)
    '''
    nombre_producto = input("Ingrese el producto a cargar: ")
    precio_producto = input("Ingrese el precio: ")
    precio_producto = validar_numero_positivo(precio_producto)
    cantidad_producto = input("Ingrese la cantidad: ")
    cantidad_producto = validar_numero_positivo(cantidad_producto)


    inventario.append([nombre_producto,precio_producto,cantidad_producto])
    print(inventario)
    return inventario



def buscar_producto(inventario:list)->None:
    '''
    Busca un producto en el inventario y si lo encuetra imprime toda su información.
    Parametro: inventario (list)
    Retorno: None
    '''
    print("\n-Buscar producto-")
    producto_a_buscar = input("Ingrese el producto que desea buscar: ").capitalize()
    producto_encontrado = []
    for producto in inventario:
        if producto_a_buscar in producto:
            producto_encontrado = producto
    
    if producto_encontrado != []:
        print(f"\nProducto: {producto_encontrado[0]} - Precio: {producto_encontrado[1]} - Cantidad: {producto_encontrado[2]}")
    else:
        print("El producto NO se econtro.")


def ordenar_inventario(inventario:list):

    longitud = len(inventario)

    for i in range(longitud):
        for j in range(longitud-1):
            if inventario[j][1] > inventario[j+1][1]:
                pass
    


def producto_mas_caro(inventario:list)->None:
    '''
    Busca en el invetario el producto mas caro y lo muestra en pantalla.
    Parametro: inventario (list)
    Retorno: None
    '''
    producto_mas_caro = inventario[0]

    for producto in inventario:
        if producto[1] > producto_mas_caro[1]:
            producto_mas_caro = producto
    
    respuesta =f'''\nEl producto mas caro es {producto_mas_caro[0]} con un precio de ${producto_mas_caro[1]} y {producto_mas_caro[2]} unidades.'''
    print(respuesta)

def producto_mas_barato(inventario:list)->None:
    '''
    Busca en el invetario el producto mas barato y lo muestra en pantalla.
    Parametro: inventario (list)
    Retorno: None
    '''
    producto_mas_barato = inventario[0]

    for producto in inventario:
        if producto[1] < producto_mas_barato[1]:
            producto_mas_barato = producto
    
    respuesta =f'''\nEl producto mas barato es {producto_mas_barato[0]} con un precio de ${producto_mas_barato[1]} y {producto_mas_barato[2]} unidades.'''
    print(respuesta)


def producto_mayor_15000(inventario:list):
    '''
    Busca en el inventario si hay productos cuyo precio sea mayor a $15.000 y los muestra en pantalla.
    Parametro: inventario (list)
    Retorno: None
    '''
    productos_mayor_15000 = []

    for producto in inventario:
        if producto[1] > 15000:
            productos_mayor_15000 += [producto]
    
    if productos_mayor_15000 != []:
        print("\nPRODUCTOS CUYO PRECIO ES MAYOR A $15.000:")
        for i in range(len(productos_mayor_15000)):
            print("-------------------------------------")
            print(f"[{i+1}] Nombre: {productos_mayor_15000[i][0]} | Precio: ${productos_mayor_15000[i][1]} | Stock: {productos_mayor_15000[i][2]}")
    else:
        print("No hay productos con su precio mayor a $15.000")
