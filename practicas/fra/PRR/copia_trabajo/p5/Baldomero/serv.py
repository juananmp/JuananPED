import sys, os, socket, time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# puerto 12000
serverSocket.bind(('', 12000))


while True:
	peticion, address = serverSocket.recvfrom(1000)
	peticion_decod = peticion.decode('utf8')
	ip = address[0]
	puerto = address[1]

	if peticion_decod == "hora":
		hora = time.strftime("%H:%M:%S")
		hora_cod = hora.encode('utf8')
		print('Servidor ha recibido peticion para enviar la hora')
		serverSocket.sendto(hora_cod, address)

	elif peticion_decod == "fecha":
		fecha = time.strftime("%d/%m/%y")
		fecha_cod = fecha.encode('utf8')
		print('Servidor ha recibido peticion para enviar la fecha')
		serverSocket.sendto(fecha_cod, address)

	else:
		print('He recibido una peticion que no se de que es, pero como soy un servidor de fecha y hora te mando las dos')
		tiempo = time.ctime()
		tiempo_cod = tiempo.encode('utf8')
		serverSocket.sendto(tiempo_cod, address)

serverSocket.close()



