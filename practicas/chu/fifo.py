import os, sys 
from time import strftime

hora = str(strftime("%H:%M:%S"))

fecha = str(strftime("%d/%m/%Y"))

fifo_peticion = "/tmp/fifo_peticion" # creamos el FIFO de peticion, que es un archivo

fifo_respuesta= "/tmp/fifo_respuesta" # creamos el FIFO de peticion, que es un archivo
if not os.path.exists(fifo_peticion): # en caso de que no exista ese FIFO
	os.mkfifo(fifo_peticion) #lo creamos

if not os.path.exists(fifo_respuesta): # en caso de que no exista ese FIFO
	os.mkfifo(fifo_respuesta) #lo creamos
def hora_fecha(): 
	#en esta funcion en padre recibe un mensaje de su hijo preguntando por la hora o fecha
	# el padre lee el mensaje y le da respuesta conveniente
	# despues el hijo imprime por pantalla la respuesta de su padre
	pid = os.fork()
	if pid: # si soy el padre...
		fifo_peticion_modo_lectura = open(fifo_peticion,'r') #abrimos el fifo de peticion en modo lectura
		peticion = fifo_peticion_modo_lectura.readline() # leemos la peticion del hijo
		if not peticion: # una vez hayamos leido la peticion
			fifo_peticion_modo_lectura.close() # cerramos el fifo para no quedarnos tostados
		
		fifo_respuesta_modo_escritura = open(fifo_respuesta,'w') # abrimos el fifo de respuesta en modo escritura
		if peticion == 'hora': # si nos piden la hora
			fifo_respuesta_modo_escritura.write(hora) # la escribimos en el fifo
			fifo_respuesta_modo_escritura.close() # y cerramos la fifo para que el hijo no se quede tostado esperando mas datos
		if peticion == 'fecha':	# si nos piden la fecha
		
			fifo_respuesta_modo_escritura.write(fecha) # la escribimos en el fifo

			fifo_respuesta_modo_escritura.close() # y cerramos la fifo para que el hijo no se quede tostado esperando mas datos
	else: # si soy el hijo
		fifo_peticion_modo_escritura = open(fifo_peticion,'w') # abrimos el fifo de peticion en modo escritura
		mensaje = sys.argv[1] # parametro que nos pasen por terminal
		fifo_peticion_modo_escritura.write(mensaje) #escribimos la peticion el fifo
		
		fifo_peticion_modo_escritura.close() # y cerramos el fifo para que el padre no se quede tostado
		
		fifo_respuesta_modo_lectura = open(fifo_respuesta,'r') # abrimos el fifo de respuesta en modo lectura
		respuesta = fifo_respuesta_modo_lectura.readline() # leemos la respuesta que nos de el padre
		fifo_respuesta_modo_lectura.close() # ceramos el fifo para no quedarnos tostados
		print(respuesta)
hora_fecha()		
"""notas adicionales:
	realmente, no hace falta cerrar las fifos una vez hemos leido, pero una vez hemos obtenido lo que queremos leer, no tiene sentido dejar un objeto en memoria el cual no va a hacer nada, y en algunos casos, si quisiemos abrir ese fifo otra vez, nos daria un error. hablo de las lineas 25 y 45
 
"""	
