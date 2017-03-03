#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import funciones
import json

ruta_s= socket.socket()

#Conexión con el server
ruta_s.connect(("localhost",35000))

user_data   = []
operaciones = []

validacion  = ''

while True: # mientras sea verdadero

    operadores  = ''
    operaciones = []

    if validacion == '':

        datos       =   ''
        paramsSend  =   ''
        operadores  =   ''

        User = raw_input("Ingrese Nombre de Usuario ")

        user_data.append(User)

        password = raw_input("Digite la Clave de Acceso ")

        user_data.append(password)
        paramsSend = json.dumps(user_data)

        ruta_s.send(paramsSend)
        user_data=[]
        datos = ruta_s.recv(1000)

        if datos == 'true':
            print "Bienvenido\n"

            validacion = 'true'

            acceso      =   funciones.menu()
            listamenu   =   funciones.menu_lista(acceso)

            opcion      =   raw_input("Seleccione una opción: ")
            operaciones.append(opcion)

            if opcion == 'e':

                operaciones.append('')
                operaciones.append('')
                operadores = json.dumps(operaciones)
                ruta_s.send(operadores)
                #break
                exit()

            val1 = raw_input("Digite Primer Valor ")
            operaciones.append(val1)
            val2 = raw_input("Digite Segundo Valor ")
            operaciones.append(val2)

            if opcion == 'd':
                if val2 == '0':
                    print "La División entre cero (0) no está permitida"
                    val2 = raw_input("ingrese segundo Número ")
                    operaciones[2]=(val2)

            operadores  =   json.dumps(operaciones)
            ruta_s.send(operadores)

        else:
            validacion  =''
            print 'Datos Incorrectos'
    else:

        datos = ruta_s.recv(1000)
        print 'El Resultado de la Operación es: '+datos

        acceso = funciones.menu()
        listamenu = funciones.menu_lista(acceso)

        opcion = raw_input("Seleccione una opción: ")
        operaciones.append(opcion)

        if opcion == 'e':
            operaciones.append('')
            operaciones.append('')
            operadores = json.dumps(operaciones)
            ruta_s.send(operadores)
            break

        val1 = raw_input("Digite Primer Valor: ")
        operaciones.append(val1)
        val2 = raw_input("Digite Segundo Valor ")
        operaciones.append(val2)

        if opcion == 'd':
            if val2 == '0': # Se comprueba si el segundo valor es 0, de ser así se solicita de nuevo el segundo valor
                print "La División entre cero (0) no está permitida"
                val2 = raw_input("Digite Segundo Valor ")
                operaciones[2] = (val2)

        operadores = json.dumps(operaciones)
        ruta_s.send(operadores)

#Termina la conexión
ruta_s.close()