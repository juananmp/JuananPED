
import socket, os, sys
from datetime import datetime

def serv4():
	
	s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
	
	dir_local = '/home/fran/Escritorio/PRR/copia_trabajo/p4/fran_sockets/p4_fecha_hora/misocket'
	if os.path.exists(dir_local):
		os.remove(dir_local)

	s.bind(dir_local)
	#Escucha conexiones
	s.listen(1)

	nueva_s , nueva_dir = s.accept()
	
	fecha_hora = datetime.now()
	fecha_hora = fecha_hora.isoformat()

	nueva_s.send(bytes(fecha_hora, 'utf8'))
	print('\nLa fecha y hora han sido enviadas...\n')
	nueva_s.close()

serv4()










