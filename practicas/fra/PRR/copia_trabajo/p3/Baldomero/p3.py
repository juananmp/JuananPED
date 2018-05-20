import os, sys, time

fifo_peticiones = 'fifopet'
fifo_respuesta = 'fifores'


if not os.path.exists(fifo_peticiones):
	os.mkfifo(fifo_peticiones)
if not os.path.exists(fifo_respuesta):
	os.mkfifo(fifo_respuesta)

def serv3():


	peticiones = os.open(fifo_peticiones, os.O_RDONLY)#abrimos la tuberia en modo lectura
	respuesta = os.open(fifo_respuesta, os.O_WRONLY)
	peticion = os.read(peticiones, 500)

	if peticion == b'fecha':
		fecha=time.strftime("%d / %m / %h")
		print('peticion de fecha recibida')
		os.write(respuesta,fecha.encode('utf8'))
		os.close(respuesta)
		os.close(peticiones)

	elif peticion == b'hora':
		hora=time.strftime("%H : %M : %S")
		print('peticion de hora recibida')
		os.write(respuesta, hora.encode('utf8'))
		os.close(respuesta)
		os.close(peticiones)

	else:
		print('se ha recibido una peticion incorrecta')

#if __name__ == '__name__':
serv3()


