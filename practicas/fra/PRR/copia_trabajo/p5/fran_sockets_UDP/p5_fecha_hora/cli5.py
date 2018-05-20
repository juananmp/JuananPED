import os, sys, socket

def cli5():
		#creamos socket UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

		#ligamos la socket a algun puerto
	s.bind(('',1100))
	
		#nombre_servidor = 'localhost'
	nombre_servidor = input('Introduzca el nombre del servidor: ')
		#obtenemos la ip del servidor........127.0.0.1
	
	ip_servidor = socket.gethostbyname(nombre_servidor)
	print('La IP asociada a este servidor es: %s\n'%ip_servidor)
		
	peticion = input('Introduzca lo que quiere del servidor, hora o fecha: ')
	peticion_cod = peticion.encode('utf8')
		
	puerto_servidor = 1200
	direccion = (ip_servidor, puerto_servidor)
	s.sendto(peticion_cod, direccion)

	leer, address = s.recvfrom(1024)
	leer_dec = leer.decode('utf8')
	print('\nLa peticion se ha recibido correctamente\n')
	print('La %s es: %s\n' %(peticion,leer_dec))

	s.close()


cli5()

