import json

def usuarios():
    
    lista  = ['admin','james']
    cadena = json.dumps(lista)
    return cadena

def menu():
    lista  = ['a.Suma','b.Resta','c.Multiplicacion','d.Division','e.Salir']
    cadena = json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista = json.loads(cadena)
    for i in lista:
        print i

def Suma(val1,val2):
    resp  = int(val1) + int(val2)
    return  str(resp)

def Restar(val1,val2):
    resp  = int(val1) - int(val2)
    return  str(resp)

def Multiplicar(val1,val2):
    resp  = int(val1)*int(val2)
    return  str(resp)

def Division(val1,val2):
    resp  = float(val1) / float(val2)
    return str(resp)