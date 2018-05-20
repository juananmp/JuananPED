
import os, sys, socket, time

def serv5():
		#Creamos socket UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

                #ligamos la socket al puerto 1200
	s.bind(('',1200))

	while True:
        	#leemos la peticion y la direccion enviados por el cliente
		peticion_codificada, direccion = s.recvfrom(1024)
		peticion = peticion_codificada.decode('utf8')

		ip = direccion[0]
		puerto = direccion[1]

		print('\nLa peticion llega a traves de la ip: %s ' %ip)
		print('\nUsted ha pedido el fichero:\n -> %s ' %peticion)

		print('\nEl servidor esta preparando el contenido del fichero\n Un segundo!')
		time.sleep(1)

	        	#abrimos el fichero en modo lectura y lo leemos
		fichero = os.open(peticion, os.O_RDONLY)
		leer = os.read(fichero, 2048)

        		#enviamos el contenido leido del fichero
		s.sendto(leer, direccion)
		print('\nEl contenido del archivo solicitado ha sido enviado\n')
		
	s.close()

serv5()





