import socket, sys, os , time


server_address = input('Introduzca ruta a la que el servidor se conectara:')


try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise


sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sock.bind(server_address)


sock.listen(1)

while True:
	print('Esperando conexiones')
	sock_intercambio, client_address = sock.accept() 
	print ('Conectado con: %s' %client_address)
	peticion = sock_intercambio.recv(1000)
	peticion_decode = peticion.decode('utf8')
	fichero = os.open(peticion_decode, os.O_RDONLY)
	print('El servidor se dispone a enviar el contenido del fichero %s' %peticion_decode)
 
	leer  = os.read(fichero,1000)
	#leer_cod = leer.encode('utf8')
	sock_intercambio.send(leer)
	sock_intercambio.close()


