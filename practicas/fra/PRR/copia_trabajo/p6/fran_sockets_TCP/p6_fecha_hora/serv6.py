
import os, sys, socket, time, threading, signal
from datetime import datetime

def serv6():
		#Creamos sockets UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

		#ligamos la socket al puerto 1200
	s.bind(('',1200))
	s.listen(5)

	def worker(*args):
			#codigo para atender varios a clientes a la vez
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
			print('\nUsted ha pedido la: %s' %peticion)

			if peticion == 'hora':
				print('\nSe ha recibido la peticion de hora correctamente\n')
				hora = time.strftime("%H:%M:%S")
				hora_cod = hora.encode('utf8')
				nueva_s.send(hora_cod)

			elif peticion == 'fecha':
				print('\nSe ha recibido la peticion de fecha correctamente\n')
				fecha = time.strftime("%d/%m/%y")
				fecha_cod = fecha.encode('utf8')
				nueva_s.send(fecha_cod)
	
			else:
				print('\nNo entiendo la peticion recibida pero supongo que quiere la fecha o la hora, asi que le mando las dos cosas\n')
				fecha_hora = datetime.now()
				fecha_hora = fecha_hora.isoformat()
				fecha_hora_cod = fecha_hora.encode('utf8')
				nueva_s.send(fecha_hora_cod)
		
			print('\nEl servidor ha hecho su trabajo\nEsperando otra orden\n\n')
		
		else:
			print('\nUsted ha pedido salir del servidor\n')
			nueva_s.close()
			print('\n     FIN DE LA EJECUCION DEL SERVIDOR\n')
			pid = os.getpid()
			os.kill(pid, signal.SIGKILL)

		nueva_s.close()

	while 1:
		nueva_s, direccion = s.accept()
		threading.Thread(target=worker, args = (nueva_s, direccion)).start()


	

serv6()



