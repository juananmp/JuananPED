import unittest, servidor

class TestServer (unittest.TestCase):
	def setUp(self):
		servidor.pendienteAutentificar = []

	def test_escribeLogin(self):
		socket =0
		mensaje  = "/login"
		resultado = "Dame tu nick"
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)


	def test_noEscribeLogin(self):
		socket =0
		mensaje  = "nologin"
		resultado = "Escribeme login"
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)

	def test_escribeLoginYNick(self):
		socket =0
		mensaje  = "/login"
		resultado = "Dame tu nick"
		servidor.generar_respuesta(mensaje,socket)
		mensaje = "Pedro"
		resultado = "Hola, Pedro bienvenido al chat"	
		self.assertEqual(servidor.generar_respuesta(mensaje,socket),resultado)
if __name__ == '__main__':
    unittest.main()		