import json

def menu():
    lista = ["Bienvenido SuperMarket JJ","1.Comprar Productos", "2.Ventas del Día", "3.Inventarios", "4.Salir"]
    cadena = json.dumps(lista)
    return cadena

def comprar_productos():
    lista = ["1.Frijoles => $ 1800","1.Comprar Productos", "2.Ventas del Día", "3.Inventarios", "4.Salir"]
    cadena = "Comprar Productos"
    return cadena

def ventas_dia():
    cadena = "Ventas del Día"
    return cadena

def inventarios():
    cadena = "Inventarios"
    return cadena

