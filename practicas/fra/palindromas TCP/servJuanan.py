import os, sys, socket

def servidor():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

	s.bind(('',1200))
	s.listen(5)
	print('\nServidor escuchando peticiones\n')	

	while True:
		nueva_s, direccion = s.accept()

		peticion_codificada = nueva_s.recv(512)
		peticion = peticion_codificada.decode('utf8')
	
		ip = direccion[0]
		print('La peticion llega por la ip %s'%ip)
		
		if peticion == 'Frase':
			print('\nServidor comprobando frase\n')
			enunciado = 'Frase que quieres comprobar'
			enunciado_cod = enunciado.encode('utf8')
			nueva_s.send(enunciado_cod)

			frase_cod = nueva_s.recv(4096)
			frase = frase_cod.decode('utf8')

			if str(frase) == str(frase)[::-1]:
				respuesta = 'Si es palindroma'
				respuesta_cod = respuesta.encode('utf8')
				nueva_s.send(respuesta_cod)

			else:
				respuesta = 'No es palindroma'
				respuesta_cod = respuesta.encode('utf8')
				nueva_s.send(respuesta_cod)

		elif peticion == 'NumeroNatural':
			print('\nServidor comprobando numero\n')
			enunciado = 'Numero natural que quieres comprobar'
			enunciado_cod = enunciado.encode('utf8')
			nueva_s.send(enunciado_cod)

			numero_cod = nueva_s.recv(1024)
			numero = numero_cod.decode('utf8')
			if str(numero) == str(numero)[::-1]:
				respuesta = 'Si es palindromo'
				respuesta_cod = respuesta.encode('utf8')
				nueva_s.send(respuesta_cod)
			else:
				respuesta = 'No es palindromo'
				respuesta_cod = respuesta.encode('utf8')
				nueva_s.send(respuesta_cod)
				
		print('\nEl servidor ha hecho su trabajo\nEsperando nueva orden\n')

	nueva_s.close()

servidor()








