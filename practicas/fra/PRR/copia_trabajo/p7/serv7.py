
import os, sys, socket, select



def serv7():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

	s.bind(('',1200))
	s.listen(4)
	
	lista = [s]
	
	while True:
	
		lectura, escritura, raro = select.select(lista,[],[],4)
		nueva_s, direccion = s.accept()	
		lista.append(nueva_s)

		mensaje_cod = nueva_s.recv(1000)
		mensaje = mensaje_cod.decode('utf8')

		contestacion = 'hola cliente'
		contes_cod = contestacion.encode('utf8')
		nueva_s.send(contes_cod)

		nueva_s.close()
		lista.remove(nueva_s)


def caca():
		ip = direccion[0]
		puerto = direccion[1]
		print('aa')
	
		nombre_cod = nueva_s.recv(1000)
		nombre = nombre_cod.decode('utf8')
		for i in range(0,len(lista)):
			
			if lista[i] != nombre:
				lista.append(nombre)
				nueva_s.send(nombre_cod)
				pass
			else:
				mensaje_error = 'nombre ya en uso'
				nueva_s.send(mensaje_error)
				print('probando error')			

	


serv7()


