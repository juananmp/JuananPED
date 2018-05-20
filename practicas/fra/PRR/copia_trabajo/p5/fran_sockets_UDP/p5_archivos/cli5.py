
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

	#/home/fran/Escritorio/PRR/copia_trabajo/p5/fran_sockets_UDP/p5_archivos/prueba.txt
	peticion = input('Introduzca la direccion del archivo que quiere del servidor: ')
	peticion_cod = peticion.encode('utf8')

	puerto_servidor = 1200
	direccion = (ip_servidor, puerto_servidor)
	s.sendto(peticion_cod, direccion)

		#Recibimos el contenido del fichero
	leer, address = s.recvfrom(1024)

                #lo decodificamos para poder mostrarlo en formato real
	leer_decod = leer.decode('utf8')
	print('\nEl fichero seleccionado contiene lo siguiente: \n')
	print(leer_decod)
	
	s.close()
cli5()




