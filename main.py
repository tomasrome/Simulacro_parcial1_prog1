from menu import *
from validates import *

inventario = [
    ["Laptop", 1500.00, 10],
    ["Silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor", 300.00, 30],
]

opcion_menu = "0"

while opcion_menu != "6":
    print("\nEmpire Inventory")
    print("---------------------")

    mensaje = """
    1-Cargar producto.
    2-Buscar producto.
    3-Ordenar inventario.
    4-Mostrar producto más caro y más barato.
    5-Mostrar productos con precio mayor a 15000.
    6-Salir

    -Ingrese la opción de menu 1 al 4: """

    opcion_menu = input(mensaje)
    opcion_menu = validar_menu(opcion_menu)


    match opcion_menu:
        case "1":
            cargar_producto(inventario)
        case "2":
            buscar_producto(inventario)
        case "3":
            pass
        case "4":
            producto_mas_caro(inventario)
            producto_mas_barato(inventario)
        case "5":
            producto_mayor_15000(inventario)
        case "6":
            print("\nSaliendo del programa, gracias por usar Empire Inventory.")