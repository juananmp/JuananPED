import os, sys, socket

def cli6():
		#creamos socket 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

		#nombre_servidor = 'localhost'
	nombre_servidor = input('Introduzca el nombre del servidor: ')

		#obtenemos la ip del servidor........127.0.0.1	
	ip_servidor = socket.gethostbyname(nombre_servidor)
	print('La IP asociada a este servidor es: %s\n'%ip_servidor)

	#/home/fran/Escritorio/PRR/copia_trabajo/p6/fran_sockets_TCP/p6_archivos/probando.txt
	print('Introduzca la direccion del archivo que quiere del servidor')
	print('\n      Si desea salir y apagar el servidor, ponga "salir"\n')
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
		print('\nEl fichero pedido contiene lo siguiente\n')
		print(leer_dec)

		s.close()

	else:
		s.close


cli6()

