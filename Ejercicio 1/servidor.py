#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import funciones
import json
import time

#variable de conexión
server= socket.socket()

#Se establece la dirección del servidor y el puerto, si la dirección es local se deja vacío
server.bind(("",35000))

#número de conexiones a establecer
server.listen(1)

ruta_c, direccion = server.accept()

validacion=''

while True: # mientras sea verdadero

   if validacion == '':

    dato_recibo = ''

    envio_client = ''

    dato_recibo = ruta_c.recv(1024)

    envio_client = ''

    datos = funciones.usuarios()

    envio_client=json.loads(dato_recibo)

    conexion = json.loads(datos)

    fec_act = time.strftime("%c")

    if envio_client[0] in conexion:
        
        if envio_client[1] == '12345':

            f = open("registro.txt", "a");
            
            f.write("Datos de Ingreso \n User: " + envio_client[0]+", Clave: " + envio_client[1] + "\n IP: " + direccion[0] + "\n Fecha Ingreso:" + fec_act + "\n");
            
            f.close()
            
            datos = 'true'
            
            validacion = datos

            ruta_c.send(datos)

        else:

            validacion=''
            ruta_c.send('false')

    else: # si falla la validación de usuarios

        validacion = ''
        ruta_c.send('Datos Incorrectos, Por Favor intente de Nuevo ')

   else:
       
       dato_recibo = ruta_c.recv(1024)

       parametros = json.loads(dato_recibo)

       if parametros[0] == 'a':
           resp = funciones.Suma(parametros[1],parametros[2])
       if parametros[0] == 'b':
           resp = funciones.Restar(parametros[1],parametros[2])
       if parametros[0] == 'c':
           resp = funciones.Multiplicar(parametros[1],parametros[2])
       if parametros[0] == 'd':
           resp = funciones.Division(parametros[1], parametros[2])

       if parametros[0] == 'e':
            break
       ruta_c.send(resp)

# Terminar la Conexión
print "Conexión Cerrada, Regrese Pronto"

ruta_c.close()
server.close()