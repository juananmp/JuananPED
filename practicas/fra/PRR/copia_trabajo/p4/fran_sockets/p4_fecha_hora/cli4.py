import os, sys, time, socket

def cli4():
	
	#Creamos el socket
	s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)

	print('El servidor se conectará a la dirección local "misocket" ')
	dir_local = '/home/fran/Escritorio/PRR/copia_trabajo/p4/fran_sockets/p4_fecha_hora/misocket'

	s.connect(dir_local)
	
	#Recibe el contenido del servidor con el tamaño maximo indicado
	datos = s.recv(512)
	time.sleep(1)
	print('\nLa fecha y hora actual es: ',datos.decode('utf8'),'\n')

	s.close()

cli4()







