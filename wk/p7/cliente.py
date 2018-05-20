import socket, sys, os, select
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

dir_server=(sys.argv[1], int(sys.argv[2]))
#bind donde escucha connect conectarse a esa escucha
sock.connect(dir_server)

#descifra mensaje del send dime tu nick
peticion_nick=sock.recv(1024)
print(peticion_nick.decode('utf-8'))
nick=input()
sock.send(nick.encode('utf-8'))
#el aceptado
mensaje_ok=sock.recv(1024)
print(mensaje_ok.decode('utf-8'))

while True:
#2 sockets forman el select del cliente, la rlist[socket, sys..] NO CONFUNDIR ready-rlist
#si el que llama al ready_rlist es el sys.stdin(teclado) si escribes algo entras dentro del bucle y el if
	ready_rlist, ready_wlist, ready_xlist = select.select([sock, sys.stdin],[],[])
	for elemento in ready_rlist:
		if elemento == sys.stdin:
			#if KeyboardInterrupt:
			#	sock.send('exit')
			#	sock.close()
			#	sys.exit(1)
			#else:	
                        mensaje = input()
                        if mensaje == 'exit' or mensaje == '':
                            sock.send(mensaje.encode('utf-8'))
                            sock.close()
                            break
                        
                        else:
                            mensaje = nick + ': ' + mensaje
                            sock.send(mensaje.encode('utf-8'))
#si el server te quiere enviar algo es que quieres recibir que es el sock dentro de rlist
#rlist (tiene pato juanan) ready_rlist(opera)
#el server llama a ready_rlist y este al sock y recibimos 
		else:
			mensaje = sock.recv(1024)
			print(mensaje.decode('utf-8'))
#comentario cliente
