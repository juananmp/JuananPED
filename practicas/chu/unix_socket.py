import socket
import os
import sys
from time import strftime

hora = str(strftime("%H:%M:%S"))

fecha = str(strftime("%d/%m/%Y"))

socket_address = "/tmp/socket" 


#""" creamos la direccion del socket.
#Dado que vamos a utilizar un socket de tipo UNIX, la direccion es un fichero
#"""
def cliente():
	sock_cliente = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) #creamos el socket, de tipo UNIX
	sock_cliente.connect(socket_address) #nos conectamos al socket"""
	raw_mensaje = sys.argv[2] #""" parametro que nos pasen por consola, o fecha u hora"""
	mensaje = raw_mensaje.encode('utf8') #""" hay que codificar el mensaje para poder enviarlo"""
	sock_cliente.send(mensaje) #"""enviamos el mensaje"""
	raw_respuesta = sock_cliente.recv(1024) #""" aqui el cliente se queda bloquea esperando a recibir la respuesta del servidor"""
	respuesta = raw_respuesta.decode('utf8') #""" decodificamos la respuesta"""
	print(respuesta) #""" esto no lo explico"""

def servidor():
	
	socket_servidor = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)#""" creamos el socket, de tipo UNIX"""
	try:
		os.unlink(socket_address) #""" el servidor le pide al kernel que 'libere' ese archivo, 
					#	para poder utilizarlo él"""
	except: #""" si el kernel por algun motivo no puede liberalo, levanta la excepcion"""
		if os.path.exists(socket_address):
			raise

	socket_servidor.bind(socket_address) #""" se le asigna una direccion al socket"""
	socket_servidor.listen(1)#""" esto indica cuantas peticiones de conexion puede atender a la vez el socket"""
	while True: #para que el servidor siga vivo despues de atender una peticion
		conexion,cliente_address = socket_servidor.accept() #"""aceptamos la conexion que llegue"""
		raw_peticion = conexion.recv(1024)# """ el servidor se bloquea aqui esperando a recibir un mensaje del cliente"""
		peticion = raw_peticion.decode('utf8') #"""decodificamos el mensaje que llegue"""
		if peticion == 'hora': #"""si el mensaje es hora, le enviamos la hora a quien nos la haya pedido"""
			conexion.send(hora.encode('utf8'))
		elif peticion == 'fecha': #"""si el mensaje es fecha, le enviamos la fecha a quien nos la haya pedido"""
			conexion.send(fecha.encode('utf8'))

	
if sys.argv[1] == "cliente":
	cliente()

if sys.argv[1] == "servidor":
	servidor()
