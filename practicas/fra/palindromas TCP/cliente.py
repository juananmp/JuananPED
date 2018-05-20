import socket, sys, os

def cliente():

		#creamos socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

		#nombre_servidor = 'localhost'
	nombre_servidor = input('Introduzca el nombre del servidor: ')

		#obtenemos la ip del servidor........127.0.0.1
	ip_servidor = socket.gethostbyname(nombre_servidor)
	print('La IP asociada a este servidor es: %s\n'%ip_servidor)
	
	puerto_servidor = 1200
	direccion = (ip_servidor, puerto_servidor)

		#Establecemos la conexion
	s.connect(direccion)
	
	variable = True
	while variable == True:
		print("Elija una de estas opciones (RESPETE LAS MAYUSCULAS)")
		print("1. Frase")
		print("2. NumeroNatural")
		print("3. Salir (Salir del cliente)")
		peticion = input("Peticion: ")
		print('\n')
		peticion_cod = peticion.encode('utf8')
	
		if peticion == 'Frase':
			#Pedimos el fichero mandando la peticion
			s.send(peticion_cod)
		
			enunciado_cod = s.recv(1024)
			enunciado = enunciado_cod.decode('utf8')
			print(enunciado)
			
			frase_comprobar = input('-->')
			frase_comprobar_cod = frase_comprobar.encode('utf8')
			s.send(frase_comprobar_cod)

			respuesta_cod = s.recv(512)
			respuesta = respuesta_cod.decode('utf8')
			print(respuesta)
			print('\n')

		elif peticion == 'NumeroNatural':
        	                #Pedimos el fichero mandando la peticion
                	s.send(peticion_cod)

	                enunciado_cod = s.recv(1024)
        	        enunciado = enunciado_cod.decode('utf8')
	                print(enunciado)

        	        frase_comprobar = input('-->')
        	        frase_comprobar_cod = frase_comprobar.encode('utf8')
	                s.send(frase_comprobar_cod)

        	        respuesta_cod = s.recv(512)
	                respuesta = respuesta_cod.decode('utf8')
        	        print(respuesta,'\n')

		elif peticion == 'Salir':
			print('\nUsted quiere cerrar el Cliente\n')
			variable = False

		else:
			print('Opcion no valida\nIntroduzca una valida\n')



cliente()

