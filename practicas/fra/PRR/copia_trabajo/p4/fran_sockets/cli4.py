
import os, sys, socket

def cli4():

		#Creamos el socket
	s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)

		#establecemos la conexion
	#dir_local = '/home/fran/Escritorio/PRR/copia_trabajo/p4/fran_sockets/misocket'
	dir_local = input('Introduzca la ruta del socket a la que se conectara el cliente: ')
	s.connect(dir_local)

	path_fichero= input('\nIntroduzca la ruta del archivo que desea que lea el servidor: ')
		#enviamos la ruta del fichero
	s.send(bytes(path_fichero, 'utf8'))

		#Recibimos el contenido del fichero
	respuesta = s.recv(2048)

		#lo decodificamos para poder mostrarlo en formato real
	respuesta_decod = respuesta.decode('utf8')
	print('\nEl fichero seleccionado contiene lo siguiente: \n')
	print(respuesta_decod)

	#s.shutdown(socket.SHUT_RD)
	s.close()
	
cli4()





