import os
import sys
from time import strftime
from datetime import datetime

hora = str(strftime("%H:%M:%S"))
fecha = str(strftime("%d-%m-%Y"))
def hora_fecha():
	#en esta funcion el padre recibe un mensaje de su hijo preguntado por la fecha o por la hora
	# lee el mensaje y le responde lo que corresponda, el hijo lee el mensaje y lo imprime por pantalla
	read_descriptor,write_descriptor = os.pipe() # descriptores de fichero
	read_object,write_object = os.fdopen(read_descriptor,'rb',0), os.fdopen(write_descriptor,'wb',0) #objetos de fichero
	
	read_descriptor2,write_descriptor2 = os.pipe() # descriptores de fichero
	read_object2,write_object2 = os.fdopen(read_descriptor2,'rb',0), os.fdopen(write_descriptor2,'wb',0) #objetos de fichero
	pid = os.fork()
	if pid: # si es el padre
		write_object.close() # el padre no va a escribir en esta PIPE
		while True:
			raw_data = read_object.readline() # el padre espera a recibir un mensaje del hijo
			read_object.close() # despues de leer, cierra la lectura, para que no se quede tostado 
			data = raw_data.decode('utf8')
			if data == 'hora':
				write_object2.write(hora.encode('utf-8'))
				write_object2.close() #despues de escribir, cierra el write para que el hijo no se quede tostado,creyendo que quedan mas datos por recibir
				break
			if data == 'fecha': #esto es lo mismo que la explicacion de arriba pero con fecha.
				write_object2.write(fecha.encode('utf8'))
				write_object2.close()
				break

	else: # si es el hijo
		read_object.close() # el hijo no va a leer de esta PIPE
		mensaje = sys.argv[1] #indicamos por terminal si queremos la fecha o la hora, 
		#el comando seria python3tuberias.py fecha o python3 tuberias.py hora, tuberias.py = sys.argv[0] y fecha u hora sys.argv[1]
		write_object.write(mensaje.encode('utf8')) # escribimos en la pipe 
		write_object.close() # y la cerramos para que el padre no se quede tostado esperando mas envios
		write_object2.close()  # cerramos la segunda PIPE para que no haya colision entre padre e hijo
		respuesta =read_object2.readline()
		read_object2.close() # cerramos la pipe porque no vamos a volver a leer 
		print(respuesta.decode('utf8'))
hora_fecha()
	
