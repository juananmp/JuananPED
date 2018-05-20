import socket, sys, os, select

sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

dir_server=(sys.argv[1], int(sys.argv[2]))
sock.connect(dir_server)

"""
peticion_nick=sock.recv(1024)
print(peticion_nick.decode('utf-8'))
nick=input()

sock.send(nick.encode('utf-8'))
mensaje_ok=sock.recv(1024)
print(mensaje_ok.decode('utf-8'))
"""

while True:
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
				#mensaje = nick + ': ' + mensaje
				sock.send(mensaje.encode('utf-8'))
		else:
			mensaje = sock.recv(1024)
			print(mensaje.decode('utf-8'))
#comentario cliente