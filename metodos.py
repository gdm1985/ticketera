import os


def menu():
    print('''\t\t\tMenu
        [1] Ingresar nuevo reclamo
        [2] Consultar reclamos abiertos
        [3] Consultar reclamos cerrados
        [4] Cerrar un reclamo
        [Q]: Salir''')


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')