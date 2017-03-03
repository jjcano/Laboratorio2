# -*- coding: utf-8 -*-
import json
import os

def menu():
    lista=['Menú: ','a.Listar Archivos','b.Crear Archivo','c.Modificar Archivo','d.Eliminar Archivo','e.Salir']
    cadena=json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def ListF():
    path = 'E:\JJ\Ingeniería\Semestre XI\Sistemas Distribuidos\Taller 2\Ejercicio 2'
    # Se crea la lista vacía para incluir los ficheros
    lstFiles = []
    # Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)  # os.walk() Lista directorios y ficheros
    # Crea una lista de los ficheros txt que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if (extension == ".txt"):
                lstFiles.append(nombreFichero + extension)
    cadena = json.dumps(lstFiles)
    return cadena

def CreateF(nfile,contenido):
    fo = open(nfile + ".txt", "a")
    fo.write(contenido)
    fo.close()
    lista=["Archivo Creado  ",'Menú de Opciones','a. Listar Archivos','b. Crear archivo','c. Modificar archivo','d. Eliminar archivo','e. Salir']
    cadena = json.dumps(lista)
    return cadena

def EditF(file):
    
    if os.path.isfile(file + ".txt"):
        fo = open(file+ ".txt", "r")
        contenido=fo.read()
    else:
        contenido="El Archivo No Existe"
    return contenido

def UpdateF(file,content):

    if os.path.isfile(file + ".txt"): # si encuentra el archivo
        fo = open(file+".txt", "a")   # Lo abre
        fo.write(content+"\n")        # Escribe el contenido
        fo.close()                    # Cierra el Archivo
        lista = ["Archivo Modificado ", 'Menú: ', 'a.Listar Archivos', 'b. Crear archivo','c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir','Digite una opcion']
    else:
        lista = ["El Archivo No Existe", 'Menú de Opciones', 'a. Listar Archivos', 'b. Crear archivo',
                 'c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir', 'Digite una opcion']
    cadena = json.dumps(lista)
    return cadena

def DeleteF(file):

    if os.path.isfile(file+".txt"): # Si encuentra el archivo
        os.remove(file+".txt")      # Elimina el Archivo
        lista = ["Archivo Eliminado ", 'Menú de Opciones', 'a. Listar Archivos', 'b. Crear archivo',
             'c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir']
    else:
        lista = ["Archivo No existe", 'Menú de Opciones', 'a. Listar Archivos', 'b. Crear archivo',
                 'c. Modificar archivo', 'd. Eliminar archivo', 'e. Salir']
    cadena = json.dumps(lista)
    return cadena


