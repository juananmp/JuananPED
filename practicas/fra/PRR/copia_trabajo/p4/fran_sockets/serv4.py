
import socket, os, sys, time


def serv4():

	s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
	
	#dir_local = '/home/fran/Escritorio/PRR/copia_trabajo/p4/fran_sockets/misocket'
	dir_local = input('Introduzca la ruta del socket a la que se conectara el servidor: ')
	if os.path.exists(dir_local):
		os.remove(dir_local)

	s.bind(dir_local)
	s.listen(1)

	while True:
			#aceptamos la conexion, donde se crea un nuevo socket
		nueva_s, nueva_dir = s.accept()	
	
			#recibimos la peticion del fichero que quiere y decodificamos
		peticion = nueva_s.recv(1024)
		peticion_decod = peticion.decode('utf8')
		print('\nEl servidor esta preparando el contenido del fichero\n->%s'%peticion_decod)
		time.sleep(1)

			#abrimos el fichero en modo lectura y lo leemos
		fichero = os.open(peticion_decod, os.O_RDONLY)
		leer = os.read(fichero, 1024)

			#enviamos el contenido leido del fichero
		nueva_s.send(leer)
		print('\nEl contenido del archivo solicitado ha sido enviado\n')	
		nueva_s.close()


serv4()





