#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones
import json

#Variable Tipo Socket
server= socket.socket()

#IP de Conexión y puerto
server.bind(("",35000))

#Número de Conexiones
server.listen(1)

ruta_c, direccion = server.accept()

validacion = ''

while True:
    if validacion == '':

        datos = funciones.menu()
        ruta_c.send(datos)

        validacion = 'true'

    else:

        resulta = []
        dato_entra = ruta_c.recv(1024)
        opcion = json.loads(dato_entra)

        print opcion[0]

        if opcion[0] == 'a':
            resulta = funciones.ListF()
        if opcion[0] == 'b':
            resulta = funciones.CreateF(opcion[1], opcion[2])
        if opcion[0] == 'c':
            resulta = funciones.EditF(opcion[1])
        if opcion[0] == 'n':
            resulta = funciones.UpdateF(opcion[1], opcion[2])
        if opcion[0] == 'd':
            resulta = funciones.DeleteF(opcion[1])
        if opcion[0] == 'e':
            print "Hasta la Vista"
            break
        
        ruta_c.send(resulta) #Regresar Respuesta al cliente

ruta_c.close()
server.close()