
def validar_menu(opcion_menu:str)->str:
    '''
    Verifica que el valor ingresado se encuentre entre las opciones de menu.
    Parametro: valor_input (str)
    Retorno: opcion_menu (str)
    '''
    while opcion_menu != "1" and opcion_menu != "2" and opcion_menu != "3" and opcion_menu != "4" and opcion_menu != "5" and opcion_menu != "6":
        opcion_menu = input("Opción invalida. Vuelva a ingresar: ")
    return opcion_menu


def validar_numero_positivo(valor_input:str)->float:
    '''
    Verifica que el valor ingresado no sea un string vacio y que sea un número entero positivo. Finalmente convierte el str a float.
    Parametro: valor_input (str)
    Retorno: valor_input (float)
    '''
    while valor_input == "" or not valor_input.isdigit() or valor_input.startswith("-"):
        valor_input = input("Debe ingresar un número valido. Vuelva a intentar: ")
    valor_input = float(valor_input)
    return valor_input
