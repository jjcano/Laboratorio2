import json

def menu(cadena):
    lista = json.loads(cadena)
    for i in lista:
        print i

