
import os, sys, socket, time
from datetime import datetime

def serv5():
		#Creamos sockets UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

		#ligamos la socket al puerto 1200
	s.bind(('',1200))

	while True:
			#leemos la peticion y la direccion enviados por el cliente
		peticion_codificada, direccion = s.recvfrom(1024)
		
		peticion = peticion_codificada.decode('utf8')
		#direccion = direccion_codificada.decode('utf8')
		
		ip = direccion[0]
		puerto = direccion[1]
		
		print('\nLa peticion llega a traves de la ip: %s ' %ip)
		print('\nUsted ha pedido la: %s' %peticion)

		if peticion == 'hora':
			print('\nSe ha recibido la peticion de hora correctamente\n')
			hora = time.strftime("%H:%M:%S")
			hora_cod = hora.encode('utf8')
			s.sendto(hora_cod, direccion)

		elif peticion == 'fecha':
			print('\nSe ha recibido la peticion de fecha correctamente\n')
			fecha = time.strftime("%d/%m/%y")
			fecha_cod = fecha.encode('utf8')
			s.sendto(fecha_cod, direccion)
	
		else:
			print('\nNo entiendo la peticion recibida pero supongo que quiere la fecha o la hora, asi que le mando las dos cosas\n')
			fecha_hora = datetime.now()
			fecha_hora = fecha_hora.isoformat()
			fecha_hora_cod = fecha_hora.encode('utf8')
			s.sendto(fecha_hora_cod, direccion)
		
		print('\nEl servidor ha hecho su trabajo\nEsperando otra orden\n\n')

	s.close()


	

serv5()



