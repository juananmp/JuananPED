import os, sys, socket, time, threading, signal

from datetime import datetime
from modulo import Codificador, ClaseExcepcion

def servidor():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    s.bind(('',16012))
    s.listen(5)

    def worker(*args):
        c = Codificador()
        peticion_cod = nueva_s.recv(1024)
        peticion = c.decodificar(peticion_cod)

        if peticion == 'FECHA':
            print('\nSe ha recibido la peticion de fecha correctamente\n')
            fecha = time.strftime("%d/%m/%y")
            fecha_cod = c.codificar(fecha)
            nueva_s.send(fecha_cod)

        elif peticion == 'HORA':
            print('\nSe ha recibido la peticion de hora correctamente\n')
            hora = time.strftime("%H:%M:%S")
            hora_cod = c.codificar(hora)
            nueva_s.send(hora_cod)
        else:
            mensaje = 'ERROR'
            mensaje_cod = c.codificar(mensaje)
            nueva_s.send(mensaje_cod)
        

        print('\nEl servidor ha hecho su trabajo\n')
        nueva_s.close()


    while 1:
        nueva_s, direccion = s.accept()
        threading.Thread(target=worker, args=(nueva_s,direccion)).start()






servidor()

