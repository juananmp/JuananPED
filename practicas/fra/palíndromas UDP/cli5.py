

import sys, os, socket, time


# Crea socket UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Lo liga a algun puerto
serverSocket.bind(('',10000))


ipServidor = raw_input('Introduzca direccion IP del servidor (si no sabe cual use la dir. de loopback 127.0.0.1): ')
puertoServidor = input('Introduzca puerto del servidor (en este caso usamos 12000): ')

opcion = raw_input('Introduzca la opcion de la consulta que le quiere realizar al servidor:\n1.Frase\n2.Numero ')

serverSocket.sendto(opcion,(ipServidor,puertoServidor))

if opcion=="1":
	palabra = raw_input('Introduzca la frase que quiere comprobar:  ')
	serverSocket.sendto(palabra,(ipServidor,puertoServidor))

elif opcion=="2":
	numero = raw_input('Introduzca el numero que quiere comprobar:  ')
	serverSocket.sendto(numero,(ipServidor,puertoServidor))

respuesta = ""
leido = True

while leido: #Guarda el contenido enviado por el servidor
	
	leido, direc = serverSocket.recvfrom(100)
	respuesta = respuesta + leido

if opcion=="1":
	print('La frase %s : %s' % (palabra,respuesta))
elif opcion=="2":
	print('El numero %s : %s' % (numero,respuesta))

exit(0)