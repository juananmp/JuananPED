import socket, signal,sys, select, time

pendienteAutentificar = []
yaAutentificados = []
lista_nick=[]

def conexion(socket_conexion):
	print('Alquien se quiere conectar')
	n_sock,addr= socket_conexion.accept()
	rlist.append(n_sock)


def generar_respuesta(datos, elemento):
	if not (elemento in pendienteAutentificar)  and datos == "/login":
		pendienteAutentificar.append(elemento)
		respuesta = "Dame tu nick"

	elif elemento in pendienteAutentificar and not (datos in lista_nick):
		lista_nick.append(datos)
		yaAutentificados.append(elemento)
		pendienteAutentificar.remove(elemento)
		respuesta = "Hola, "+ datos + " bienvenido al chat"

	elif elemento in pendienteAutentificar and datos in lista_nick:
		respuesta = "El nick "+ datos + " ya está cogido, por favor escriba otro"

	#chat
	elif elemento in yaAutentificados:
		for cliente in yaAutentificados:
				#if cliente.getpeername == elemento.getpeername():
					#pass
				if  cliente == elemento:
					pass
				else:
					cliente.send(datos.encode('utf-8'))
				respuesta = "Enviado"

		

	elif elemento in yaAutentificados and datos == "/exit":
		pass

		yaAutentificados.remove(elemento)
		#hay que borrar el nick de la lista de nicks, pero como podemos conseguir el nick asociado a un elemento?
		#elemento.close() (hay que borrar ese socket pero si lo ponemos aqui luego no se puede enviar el mensaje de hasta pronto)
		respuesta = "Hasta pronto!!"
	else:
		respuesta= "Escribe /login"	

	return respuesta	



def signal_handler(signal,frame):
	sys.exit(0)

if __name__ == '__main__':

	socket_conexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket_conexion.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	socket_conexion.bind((sys.argv[1], int(sys.argv[2])))
	socket_conexion.listen(5)

	rlist = [socket_conexion]

	while True:
		ready_rlist, ready_wlist, ready_xlist = select.select(rlist,[],[])
		for elemento in ready_rlist:
			if elemento == socket_conexion:
				conexion(elemento)
			else:
				mensaje = elemento.recv(1024)
				datos = mensaje.decode('utf8')
				respuesta = generar_respuesta(datos, elemento)
				mres = respuesta.encode('utf8')
				elemento.send(mres)

"""
socket_conexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_conexion.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

socket_conexion.bind((sys.argv[1], int(sys.argv[2])))
socket_conexion.listen(5)
lista_nick=[]
def signal_handler(signal,frame):
	sys.exit(0)


rlist = [socket_conexion]

while True:	
	ready_rlist, ready_wlist, ready_xlist = select.select(rlist,[],[])
	for elemento in ready_rlist:
		if elemento == socket_conexion:
			signal.signal(signal.SIGINT,signal_handler)
			print('Alquien se quiere conectar')
			n_sock,addr= socket_conexion.accept()
			rlist.append(n_sock)
			n_sock.send('Dime tu nick:'.encode('utf-8'))
			nick = n_sock.recv(1024)
			if nick in lista_nick:
				n_sock.send("Vete a suplanatar a tu madre".encode('utf-8'))
				rlist.remove(n_sock)
				elemento.close()
			else:
				lista_nick.append(nick)
				print('El usuario ' + nick.decode('utf-8') + ' se ha conectado')
				n_sock.send('Estás conectado al chat, ya puedes chatear'.encode('utf-8'))
		else:
			mensaje = elemento.recv(1024)
			if mensaje.decode('utf-8') == "exit" or mensaje.decode('utf-8') == '':
				rlist.remove(elemento)
				elemento.close()

			for cliente in rlist:
				if cliente == socket_conexion or cliente == elemento:
					pass
				else:
					cliente.send(mensaje)
"""
