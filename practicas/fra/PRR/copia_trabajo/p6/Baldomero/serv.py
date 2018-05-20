import sys, os, socket, time 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('', 12000))
serverSocket.listen(5)

while True:

	socketIntercambio, client_address = serverSocket.accept()
	peticion = socketIntercambio.recv(1000)
	peticion_decod = peticion.decode('utf8')
	ip = client_address[0]
	puerto = client_address[1]

	print('Peticion recibida de: %s:%s ' % (ip,puerto) )
	print('El cliente me solicita la %s' % peticion)


	if peticion_decod=="hora":
		hora=time.strftime("%H:%M:%S")
		hora_cod=hora.encode('utf8')
		print('Servidor ha recibido peticion para enviar la hora')
		socketIntercambio.send(hora_cod)

	elif peticion_decod=="fecha":
		fecha=time.strftime("%d/%m/%y")
		fecha_cod=fecha.encode('utf8')
		print('Servidor ha recibido peticion para enviar la fecha')
		socketIntercambio.send(fecha_cod)

	else:
		print('He recibido una peticion que no se de que es, pero como soy un servidor de fecha y hora te mando las dos')
		tiempo=time.ctime()
		tiempo_cod=tiempo.encode('utf8')
		socketIntercambio.send(tiempo_cod)


	
	print('Servidor ha respondido')
	socketIntercambio.close()
