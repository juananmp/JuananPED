
import os, sys, socket, select,time

def cli7():
		#Creamos socket 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
	
		#nombre_servidor = 'localhost'
	nombre_servidor = input('Introduzca el nombre del servidor: ')
		#obtenemos la ip del servidor......127.0.0.1
	ip_servidor = socket.gethostbyname(nombre_servidor)
	puerto = 1200
	direccion = (ip_servidor, puerto)

	s.connect(direccion)
	
	nombre_correcto = True
	while nombre_correcto:
		nombre = input('\nIntroduzca el nombre del cliente: \n')
		nombre_cod = nombre.encode('utf8')
		s.send(nombre_cod)
		nombre_verificado_cod = s.recv(1000)
		nombre_verificado = nombre_verificado_cod.decode('utf8')		
		print(nombre_verificado)
		s.close()
		nombre_correcto = False




def caca():
	if nombre_verificado == nombre:
		nombre_correcto = False
		print('\nNombre valido\n')	
				

	while True:
		print('\nConexión establecida\n')
		time.sleep(15)
		pass

	s.close()
cli7()




