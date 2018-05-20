import os, sys

fifo_peticiones = 'fifopet'
fifo_respuesta = 'fifores'

def cli3():

	peticion = input('introduce la peticion')
	peticiones = os.open(fifo_peticiones, os.O_WRONLY)
	os.write(peticiones, peticion.encode('utf8'))
	os.close(peticiones)
	
	respuesta = os.open(fifo_respuesta, os.O_RDONLY)
	leido = os.read(respuesta, 500)
	print (' la %s es: ' %(peticion))
	print(leido.decode('utf8'))
	
	os.close(respuesta)
#if __name__ == '__name__':
cli3()



