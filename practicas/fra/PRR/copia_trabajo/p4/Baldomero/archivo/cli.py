import socket, os
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

flag = True

while flag:

    server_address = input('Introduzca la ruta a la que el cliente se conectara: ')

    print ('Conectando con: %s' % server_address)

    try:
        sock.connect(server_address)
        flag = False
    except socket.error as msg:
        print('La direccion proporcionada no es valida, introduzca otra por favor')
        flag = True
ruta = input('Introduce la ruta del archivo que solicitas al servidor: ')
print('\n')
sock.send(bytes(ruta,'utf8'))
respuesta = sock.recv(1000)
respuesta_decode = respuesta.decode('utf8')
print( 'El contenido del archivo es: \n %s' % respuesta_decode)

sock.close()
exit(0)
