
import sys, os, socket, time



def palindroma(mensaje):
	mensaje_sin_espacios = mensaje.replace(' ','') 
 
	if mensaje_sin_espacios == mensaje_sin_espacios[::-1]: 
		return "si"
	else: 
		return "no"



# Crea socket UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Lo liga al puerto 12000
serverSocket.bind(('', 12000))


while True:
	#Lee nombre del fichero a enviar
	peticion, address = serverSocket.recvfrom(1000)

	ip = address[0]
	puerto = address[1]

	print('Peticion recibida de: %s ' % ip)
	print('El opcion del menu pedida es: %s' % peticion)

	if peticion=="1":
		palabra, address = serverSocket.recvfrom(1000)
		respuesta_palindroma=palindroma(palabra)
		print(respuesta_palindroma)
		if respuesta_palindroma=="si":
			respuesta_cliente="Es palindroma"
		else:
			respuesta_cliente="No es palindroma"
		serverSocket.sendto(respuesta_cliente, address)

	if peticion=="2":
		numero, address = serverSocket.recvfrom(1000)
		respuesta_palindromo=palindroma(numero)
		print(respuesta_palindromo)
		if respuesta_palindromo=="si":
			respuesta_cliente="Es palindroma"
		else:
			respuesta_cliente="No es palindroma"
		
		serverSocket.sendto(respuesta_cliente, address)

	serverSocket.sendto('', address)


	print('Servidor ha respondido. Peticion despachada.')	

