import os, sys, socket

from modulo import Codificador, ClaseExcepcion

def cliente():

    i = 0
    while i <=3:
        c = Codificador()
        i = i +1
        print('        Iteracion %s\n' %i)
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        
            #pedimos al usuario la direccion del servidor
            #nombre = localhost
        nombre_servidor = input('Introduzca el nombre del servidor: ')
    
        ip_servidor = socket.gethostbyname(nombre_servidor)
        print('La IP asociada a este servidor es: %s\n'%ip_servidor)

        print('Introduzca lo que quiere del servidor, FECHA o HORA...(RESPETE LAS MAYUSCULAS)')
        peticion = input('Peticion: ')

        peticion_cod = c.codificar(peticion)

        puerto_servidor = 16012
        direccion = (ip_servidor, puerto_servidor)

        s.connect(direccion)

        s.send(peticion_cod)

        if peticion == 'FECHA' or peticion == 'HORA':
            leer_cod =  s.recv(2048)
            leer = c.decodificar(leer_cod)
            print('\nLa peticion se ha recibido correctamente\n')
            print('La %s es: %s\n' %(peticion,leer))
            s.close()

        else:
            mensaje_cod = s.recv(2048)
            mensaje = c.decodificar(mensaje_cod)
            print(mensaje)









cliente()
