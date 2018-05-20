
import sys, os, socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipServidor = input('Introduzca direccion IP del servidor (si no sabe cual use la dir. de loopback 127.0.0.1): ')
puertoServidor = 12000

peticion = input('Introduzca la peticion que le quiere enviar al servidor "hora" o "fecha": ')

soc.connect((ipServidor,puertoServidor))

soc.send(bytes(peticion,'utf8'))

leido = soc.recv(100)

if leido == '404':
	
	print('Servidor informa de que tal recurso no existe. Cerrando programa cliente.')
	exit(0)

else:

	print('La %s es: %s' %(peticion,leido))
	print('\n\nCliente terminado')
	exit(0)
