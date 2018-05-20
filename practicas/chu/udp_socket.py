import socket
import sys
from time import strftime
hora = str(strftime("%H:%M:%S"))
fecha = str(strftime("%d/%m/%Y"))
socket_address = ('localhost',9999) #como vamos a utilizar un socket para una conexion UDP,
# la direccion tiene que una tupla indicando cual es el la ip y el puerto del socket
def cliente():
	socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #creamos el socket 
	#del cliente, poniendo como paramentros que es una conexion sobre ipv4 y 
	#con mensajes de tipop datagrama
	raw_peticion = sys.argv[2] #parametro que nos pasen por consola
	peticion = raw_peticion.encode('utf8') #codificamos la peticion 
	socket_cliente.sendto(peticion,socket_address) #enviamos el mensaje 
	raw_respuesta,servidor = socket_cliente.recvfrom(1024) # aqui el cliente se bloquea 
	#esperando la respuesta del servidor
	respuesta = raw_respuesta.decode('utf8') # decodificamos la respuesta
	print(respuesta) #pues eso
def servidor():
	socket_servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #creamos el socket 
	socket_servidor.bind(socket_address) # le asignamos una direccion al socket
	while True: # bucle para que el servidor atienda mas peticiones en el futuro
		raw_peticion,direccion = socket_servidor.recvfrom(1024) # aqui el servidor se bloquea 		#esperando que le llegue algun mensaje
		peticion = raw_peticion.decode('utf8')# decodificamos el mensaje
		if peticion == 'hora':
			respuesta = hora.encode('utf8') # codificamos la respuesta
			socket_servidor.sendto(respuesta,direccion) #la enviamos a la direccion
			# que ha generado la peticion
			
		if peticion == 'fecha':
			respuesta = fecha.encode('utf8') # codificamos la respuesta
			socket_servidor.sendto(respuesta,direccion) #la enviamos a la direccion
	


if sys.argv[1] == "cliente":
	cliente()
if sys.argv[1]== "servidor":
	servidor()
