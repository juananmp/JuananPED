import socket, signal,sys, select, time
"""
pendienteAutentificar = []

def conexion(socket_conexion):
	print('Alquien se quiere conectar')
	n_sock,addr= socket_conexion.accept()
	rlist.append(n_sock)


def generar_respuesta(datos, elemento):
	if datos == "/login":
		pendienteAutentificar.append(elemento)
		respuesta = "Dame tu nick"

	elif elemento in pendienteAutentificar:
		respuesta = "Hola, "+ datos + " bienvenido al chat"	

	else:
		respuesta= "Escribeme login"	
	return respuesta	

def signal_handler(signal,frame):
	sys.exit(0)

if __name__ == '__main__':

	socket_conexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket_conexion.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	socket_conexion.bind((sys.argv[1], int(sys.argv[2])))
	socket_conexion.listen(5)

	
	lista_nick=[]
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
#por si el addr esta jodido, para que reutilices un addr, tira lo que hay empieza de nuevo
socket_conexion.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#donde escucha el seerver argv1 = localhost (ip), lo siguiente (puerto)
socket_conexion.bind((sys.argv[1], int(sys.argv[2])))
#la gente que esta escuchando, los clientes se quedan en el listen a la espera, hasta 5 personas a la espera, un 6 deniega
socket_conexion.listen(5)
#lista nicks vale que no se repitan
lista_nick=[]

#control c no se usa, señal de teclado
def signal_handler(signal,frame):
	sys.exit(0)

#impor. es como funciona el select 
rlist = [socket_conexion]

while True:	
#se compone de read, escritura, excepciones. solo importante read rlist en el select le pasamos 3 parametros, rlist se va a componer dde los sockets, el primer socket que establece la conexion es el socket_conexion, todos los socckets siguientes se meteran en la lista, y cuando lo cierre se sacaran de la lista. El ready le dira que quieres, si nadie le dice nada se queda en espera todo el rato, asi evitamos que se nos quede parado, cada vez que alguien quiere hacer algo ready lo ve y le deja hacer de todo

	ready_rlist, ready_wlist, ready_xlist = select.select(rlist,[],[])

	for elemento in ready_rlist:
#le dice a rlist quiero hacer algo, quien de rlist que es el elemento ha llamado a ready_rlist, le llama el socketconexion
		if elemento == socket_conexion:
#no sirve
			signal.signal(signal.SIGINT,signal_handler)
			print('Alquien se quiere conectar')
#el socket_conexion acepta la conexion y le da un nuevo socket al cliente, este nuevo socket lo metemos dentro de rlist
			n_sock,addr= socket_conexion.accept()
#aqui metemos el socket del cliente, la rlist tendria [socket-conexion y socket-cliente]
			rlist.append(n_sock)
			n_sock.send('Dime tu nick:'.encode('utf-8'))
#recibe el nick, pero se bloquea el server
			nick = n_sock.recv(1024)

			if nick in lista_nick:
				n_sock.send("Vete a suplanatar a tu madre".encode('utf-8'))
#quitamos este socket de la rlist, porque no tiene sentido no le queremos
				rlist.remove(n_sock)
#cerramos la conexion
				elemento.close()
			else:
#y en caso contrario añade a la lista
				lista_nick.append(nick)
				print('El usuario ' + nick.decode('utf-8') + ' se ha conectado')
#envio al cliente
				n_sock.send('Estás conectado al chat, ya puedes chatear'.encode('utf-8'))
#si ahora hablan los sockets dentro rlist, tambien levantan a ready_rlist (ve que alguien quiere hacer algo) y se ejecuta
#si alguien no es socket_conexion, entonces se comienza la charla porque ya no quieren una conexion quieren charlar, ya no me despierta socket_conexion es otro socket 
		else:
#solo recibe el mensaje porque le ha mandado algo ya el cliente, NO ES BLOQUEANTE
			mensaje = elemento.recv(1024)
			if mensaje.decode('utf-8') == "exit" or mensaje.decode('utf-8') == '':
#la forma de expulsar cliente, quito el socket de la lista y cierro el elemento que es el socket
				rlist.remove(elemento)
				elemento.close()
#para el resto de los mensajes que lleguen, 
#para todos los sockets, para cliente de la rlist, recorre todos los sockets de la lista, aqui socket es cliente pero tambibne es(elemento, n_sock, cliente)
			for cliente in rlist:
#esto evita que te lo autoenvies y que se lo envies al socket_conexion (por eso no se muestra el mensaje en el servidor)
				if cliente == socket_conexion or cliente == elemento:
					pass
				else:
					cliente.send(mensaje)

