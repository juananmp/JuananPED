import sys, os, socket, time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind(('',10000))

ipServidor = input('Introduzca direccion IP del servidor (si no sabe cual use la dir. de loopback 127.0.0.1): ')
#gethostbyname

#puertoServidor = input('Introduzca puerto del servidor (en este caso usamos 12000): ')

peticion = input('Introduzca la peticion que le quiere hacer al servidor "hora" o "fecha" : ')
peticion_cod = peticion.encode('utf8')
puertoServidor = 12000
serverSocket.sendto(peticion_cod,(ipServidor,puertoServidor))

leido, direc = serverSocket.recvfrom(100)
leido_dec = leido.decode('utf8')

print('\nLa peticion se ha recibido correctamente\n')
print('La %s es: %s' % (peticion,leido_dec))

serverSocket.close()

exit(0)
