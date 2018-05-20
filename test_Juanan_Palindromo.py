import unittest, JuananServer

class TestServer (unittest.TestCase):
	def setUp(self):
		JuananServer.haElegigoMenu = []
		JuananServer.haSeleccionadoMenu = []
		JuananServer.haSeleccionadoFrase = []

	def test_escribeMenu(self):
		socket=0
		mensaje= "Menu"
		resultado= "Elija una de estas opciones" + "\n" + "1. Frase" + "\n" + "2. Numero" + "\n" + "3. Exit"
		self.assertEqual(JuananServer.generar_respuesta(mensaje, socket), resultado)
	
	def test_escribeMalMenu(self):
		socket = 0
		mensaje = "Menulo"
		resultado = "Escribiste mal la palabra Menu, por favor vuelve a escribirla"
		self.assertEqual(JuananServer.generar_respuesta(mensaje,socket), resultado)
	def test_escribeOpcion(self):
		socket = 0
		mensaje = "1"
	#	JuananServer.haElegidoMenu = ["Juanan"]
		JuananServer.haSeleccionadoFrase = ["Juanan"]	
		resultado = "Introduce su frase palindroma, por favor"
		self.assertEqual(JuananServer.generar_respuesta(mensaje,socket), resultado)

if __name__ == '__main__':
	unittest.main()
