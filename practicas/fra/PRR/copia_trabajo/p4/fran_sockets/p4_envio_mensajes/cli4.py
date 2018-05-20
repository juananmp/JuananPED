
import os, sys, socket

def cli4():

	#Creamos el socket
	s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
	
	dir_local = '/home/fran/Escritorio/PRR/copia_trabajo/p4/fran_sockets/misocket'
	#dir_local = input('\nIntroduzca la direccion a la que se conectara el cliente: ')
	s.connect(dir_local)

	mensaje = 'hola servidor'
			#s.write(bytes(mensaje,'utf8'))
	s.send(bytes(mensaje, 'utf8'))

	
	#Recibimos la respuesta
	respuesta = s.recv(512)
	respuesta_decodificada = respuesta.decode('utf8')
	print(respuesta_decodificada)

	#s.shutdown(socket.SHUT_RD)
	s.close()

cli4()





