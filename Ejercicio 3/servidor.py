# -*- coding: utf-8 -*-

# Creación de un Chat Cliente Servidor Usando Sockets en Python
import socket
import funciones_servidor

def main():

    servidor = socket.socket()
    servidor.bind(("", 5000))
    servidor.listen(1)
    socket_cliente, datos_conexion = servidor.accept()

    mostrar_menu = False

    while True:


        if mostrar_menu == False:
            mensaje_servidor = funciones_servidor.menu()
            mostrar_menu = True
        elif mensaje_cliente == "1":
            mensaje_servidor =  funciones_servidor.comprar_productos()
        elif mensaje_cliente == "2":
            mensaje_servidor = funciones_servidor.ventas_dia()
        elif mensaje_cliente == "3":
            mensaje_servidor = funciones_servidor.inventarios()
        elif mensaje_cliente == "4":
            mensaje_servidor = "salir"
        else: mensaje_servidor = "No es una opcion valida"

        socket_cliente.send(mensaje_servidor)
        mensaje_cliente = socket_cliente.recv(1024)


        if mensaje_cliente == "salir":
            break

        print str(datos_conexion[0]) + " escribio: ", mensaje_cliente

    print "Hasta Pronto"
    socket_cliente.close()
    servidor.close()

if __name__ == '__main__':
    main()