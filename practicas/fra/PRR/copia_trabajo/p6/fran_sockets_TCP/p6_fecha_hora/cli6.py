import os, sys, socket

def cli6():
		#creamos socket UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

		#nombre_servidor = 'localhost'
	nombre_servidor = input('Introduzca el nombre del servidor: ')

		#obtenemos la ip del servidor........127.0.0.1	
	ip_servidor = socket.gethostbyname(nombre_servidor)
	print('La IP asociada a este servidor es: %s\n'%ip_servidor)

	print('Introduzca lo que quiere del servidor, hora o fecha ')
	print('\n          Si desea salir, ponga "salir"\n')
	peticion = input('Peticion: ')
	peticion_cod = peticion.encode('utf8')
		
	puerto_servidor = 1200
	direccion = (ip_servidor, puerto_servidor)
	
		#Establecemos la conexion
	s.connect(direccion)
		#Pedimos el fichero mandando la peticion
	s.send(peticion_cod)

	if peticion != 'salir':
		leer = s.recv(1024)
		leer_dec = leer.decode('utf8')
		print('\nLa peticion se ha recibido correctamente\n')
		print('La %s es: %s\n' %(peticion,leer_dec))

		s.close()

	else:
		s.close()
		print('\nSALIR DEL CLIENTE Y SERVIDOR\n')


cli6()

