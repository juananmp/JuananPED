
import os, sys, socket, time, threading, signal
from datetime import datetime

def serv6():
		#Creamos sockets UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

		#ligamos la socket al puerto 1200
	s.bind(('',1200))
	s.listen(5)

	def worker(*args):
			#codigo para atender a varios clientes a la vez
		nueva_s = args[0]
		direccion = args[1]

			#Leemos el nombre de la peticion
		peticion_codificada = nueva_s.recv(512)
			#Decodificamos la peticion
		peticion = peticion_codificada.decode('utf8')
		
		ip = direccion[0]
		puerto = direccion[1]
		
		if peticion != 'salir':	
			print('\nLa peticion llega a traves de la ip: %s ' %ip)
			print('\nUsted ha pedido el fichero:\n -> %s' %peticion)
		
			print('\nEl servidor esta preparando el contenido del fichero\n Un segundo!')
			time.sleep(1)
		
				#abrimos el fichero en modo lectura y lo leemos
			fichero = os.open(peticion, os.O_RDONLY)
			leer = os.read(fichero, 2048)
	
				#enviamos el contenido leido del fichero
			nueva_s.send(leer)
		
			print('\nEl servidor ha hecho su trabajo\nEsperando otra orden\n\n')
		
		else:
			print('\n     ADIOS CLIENTE\n')
			nueva_s.close()	

		nueva_s.close()

	
	while 1:
		nueva_s, direccion = s.accept()
		t = threading.Thread(target=worker, args = (nueva_s, direccion)).start()
		
	

serv6()



