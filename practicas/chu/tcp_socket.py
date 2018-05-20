import socket,os
import sys
from time import strftime
hora = str(strftime("%H:%M:%S"))

fecha = str(strftime("%d:%m:%Y"))
socket_address = ('localhost',9999) #variable que define la direccion del socket

def cliente():
	socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creamos el socket 
	#del cliente, indicando que es de tipo ipv4 y orientado a conexion
	socket_cliente.connect(socket_address) # nos conectamos con el socket a la direccion
	raw_peticion = sys.argv[2] # parametro que se pase por consola
	peticion = raw_peticion.encode('utf8') #codificamos la peticion
	socket_cliente.send(peticion) #enviamos la peticion
	raw_respuesta,servidor = socket_cliente.recvfrom(1024) # el cliente se bloquea
	#esperando la respuesta del servidor
	respuesta = raw_respuesta.decode('utf8') # decodificamos la respuesta
	print(respuesta)#pues eso


def servidor():

	socket_servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creamos el socket del servidor
	#indicando es de ipv4 y orientado a conexion
	socket_servidor.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)# esto es una opcion para que no nos salte el error de que la direccion ya esta en uso
	socket_servidor.bind(socket_address) #le asignamos una direccion de escucha
	socket_servidor.listen(1) # numero de conexion simultaneas que puede antender
	while True: #bucle para que el servidor no muera despues de atender una conexion
		conexion,direccion = socket_servidor.accept() # aceptamos la conexion que llegue
		raw_peticion = conexion.recv(1024)
		peticion = raw_peticion.decode('utf8') # decodificamos la peticion
		
		if peticion == 'hora': #si la peticion es la hora
			respuesta = hora.encode('utf8') # codificamos la respuesta
			conexion.send(respuesta) # mandamos la respuesta a quien haya hecho la peticion
		if peticion == 'fecha':# si la peticion es la fecha
			respuesta = fecha.encode('utf8') # codificamos la respuesta
			conexion.send(respuesta) #mandamos la respuesta a quien haya hecho la peticion

	


if sys.argv[1] == 'cliente':
	cliente()
if sys.argv[1] == 'servidor':
	servidor()
