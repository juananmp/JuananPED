import unittest, servidor

class TestServer (unittest.TestCase):
	def setUp(self):
		servidor.pendienteAutentificar = []
		servidor.yaAutentificados = []
		servidor.lista_nick = []

	def test_escribeLogin(self):
		socket =0
		mensaje  = "/login"
		resultado = "Dame tu nick"
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)


	def test_noEscribeLogin(self):
		socket =0
		mensaje  = "nologin"
		resultado = "Escribe /login"
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)

	def test_escribeLoginYNick(self):
		socket =0
		mensaje  = "/login"
		resultado = "Dame tu nick"
		servidor.generar_respuesta(mensaje,socket)
		mensaje = "Pedro"
		resultado = "Hola, Pedro bienvenido al chat"	
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)

	def test_escribeLoginYNickRepetido(self):
		servidor.lista_nick = ["Pedro"]
		socket =0
		mensaje  = "/login"
		resultado = "Dame tu nick"
		servidor.generar_respuesta(mensaje,socket)
		mensaje = "Pedro"
		resultado = "El nick Pedro ya está cogido, por favor escriba otro"	
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)

	def test_escribeLoginYNickYChat(self):
		socket =0
		mensaje  = "/login"
		resultado = "Dame tu nick"
		servidor.generar_respuesta(mensaje,socket)
		mensaje = "Pedro"
		resultado = "El nick Pedro ya está cogido, por favor escriba otro"	
		servidor.generar_respuesta(mensaje,socket)
		mensaje  = "Hola"
		resultado = "Enviado"
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)	

if __name__ == '__main__':
    unittest.main()		