#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones
import os
import json

ruta_s= socket.socket()

#Dirección & Puerto de Conexión
ruta_s.connect(("localhost",35000))

Empty       = ''
operacion   = []
Oper_Data   = ''
LeerD       = ''
Filename    = ''

while True: # Mientras se cumpla la condición

 operacion  = []
 Oper_Data  = ''
 datos      = ''

 if Empty=='':
   
   datos      = ruta_s.recv(1000)
   operacion  = []
   Oper_Data  = ''
   listamenu  = funciones.menu_lista(datos)

   OpcElect=raw_input('Seleccione una opción: ')
   operacion.append(OpcElect)

   if OpcElect=='a':

        Oper_Data = json.dumps(operacion)
        ruta_s.send(Oper_Data)

   if (OpcElect == 'b'):

       archivo   = raw_input('Digite Nombre del Archivo: ')
       operacion.append(archivo)
       TextF      = raw_input('Ingrese el contenido que contendrá el archivo \n')
       operacion.append(TextF)
       Oper_Data  = json.dumps(operacion)
       ruta_s.send(Oper_Data)

   if OpcElect == 'c':

       archivo = raw_input('Digite Nombre del Archivo: ')
       operacion.append(archivo)
       Oper_Data = json.dumps(operacion)
       LeerD = 'true'
       Filename = archivo
       ruta_s.send(Oper_Data)

   if OpcElect == 'n':

       operacion.append(OpcElect)
       operacion.append(Filename)
       content    = raw_input('Ingrese el contenido que contendrá el archivo ')
       operacion.append(content)
       LeerD      = ''
       Filename   = ''
       Oper_Data  = json.dumps(operacion)
       ruta_s.send(Oper_Data)

   if OpcElect == 'd':

       archivo    = raw_input('Digite Nombre del Archivo: ')
       operacion.append(archivo)
       Oper_Data  = json.dumps(operacion)
       LeerD      = ''
       Filename   = ''
       ruta_s.send(Oper_Data)

   if OpcElect == 'e':

       operacion.append(OpcElect)
       Oper_Data = json.dumps(operacion)
       ruta_s.send(Oper_Data)
       print "Regrese Pronto"
       break

   Empty  = 'true'

 else:

   operacion  = []
   datos      = ruta_s.recv(1000)
   
   if LeerD == '':

    LlenarLista = funciones.menu_lista(datos)
    print(LlenarLista)
    OpcElect    = raw_input('Seleccione una opción: ')
    operacion.append(OpcElect)

   else:

    print(datos)
    OpcElect  = 'n'

   if OpcElect == 'a':

        Oper_Data = json.dumps(operacion)
        ruta_s.send(Oper_Data)

   if(OpcElect == 'b'):

       archivo    = raw_input('Digite Nombre del Archivo: ')
       operacion.append(archivo)
       TextF      = raw_input('Ingrese el contenido que contendrá el archivo\n')
       operacion.append(TextF)
       Oper_Data  = json.dumps(operacion)
       ruta_s.send(Oper_Data)

   if OpcElect == 'c':

       archivo    = raw_input('Digite Nombre del Archivo: ')
       operacion.append(archivo)
       Oper_Data  = json.dumps(operacion)
       LeerD      = 'true'
       Filename   = archivo
       ruta_s.send(Oper_Data)

   if  OpcElect =='n':

       operacion.append(OpcElect)
       operacion.append(Filename)
       content    = raw_input('Ingrese el contenido que contendrá el archivo ')
       operacion.append(content)
       LeerD      = ''
       Filename   = ''
       Oper_Data  = json.dumps(operacion)
       ruta_s.send(Oper_Data)
   if OpcElect == 'd':
       archivo    = raw_input('Digite Nombre del Archivo: ')
       operacion.append(archivo)
       Oper_Data  = json.dumps(operacion)
       LeerD      = ''
       Filename   = ''
       ruta_s.send(Oper_Data)

   if OpcElect == 'e':

       operacion.append(OpcElect)
       Oper_Data = json.dumps(operacion)
       ruta_s.send(Oper_Data)
       print "Regrese Pronto"
       break

#Termina la Conexión
ruta_s.close()