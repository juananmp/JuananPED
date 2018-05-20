import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

flag = True

while flag:

    server_address = raw_input('Introduzca direccion a la que el cliente se conectara: ')

    print >>sys.stderr, 'Conectando con: %s' % server_address

    try:
        sock.connect(server_address)
        flag = False
    except socket.error, msg:
        print('La direccion proporcionada no es valida, introduzca otra por favor')
        flag = True

peticion = 'Dame hora'
print >>sys.stderr, 'Cliente enviando: "%s"' % peticion
print('\n')
sock.send(peticion)

respuesta = sock.recv(100)
print( 'La hora recibida es "%s"' % respuesta)
print('.\n.\n')
print('Fin de cliente')
    
sock.close()
exit(0)
