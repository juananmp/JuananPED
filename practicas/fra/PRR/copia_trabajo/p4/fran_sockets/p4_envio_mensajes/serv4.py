
import socket, os, sys


def serv4():

	s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
	
	dir_local = '/home/fran/Escritorio/PRR/copia_trabajo/p4/fran_sockets/misocket'
	if os.path.exists(dir_local):
		os.remove(dir_local)

	s.bind(dir_local)
	s.listen(1)

	nueva_s, nueva_dir = s.accept()
	
			#s.read(bytes(mensaje, 'utf8'))
	respuesta = nueva_s.recv(512)
	respuesta_decodificada = respuesta.decode('utf8')
	print(respuesta_decodificada)

	mensaje = 'hola cliente'
	nueva_s.send(bytes(mensaje ,'utf8'))
	print('\nlos mensajes han sido enviados\n')
			
	nueva_s.close()


serv4()





