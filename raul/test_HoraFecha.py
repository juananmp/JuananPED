import unittest, serverHoraTCP, time

class TestServer (unittest.TestCase):
	def setUp(self):
		serverHoraTCP.haElegidoMenu = []
	
	def test_escribeMenu(self):
		socket=0
		mensaje= "Menu"
		resultado= "Elija una de estas opciones" + "\n" + "1. Fecha" + "\n" + "2. Hora" + "\n" + "3. Exit"
		self.assertEqual(serverHoraTCP.generar_respuesta(mensaje, socket), resultado)

	def test_escribirMalMenu(self):
		socket=0
		mensaje= "Menulll"
		resultado = "Escribiste mal la palabra Menu, por favor vuelve a escribirla"
		self.assertEqual(serverHoraTCP.generar_respuesta(mensaje,socket), resultado)

	def test_escribirHora(self):
		socket = "Juanan"

		serverHoraTCP.haElegidoMenu = ["Juanan"]
		mensaje = "2"
		resultado = "Su hora es " + time.strftime("%X")
		self.assertEqual(serverHoraTCP.generar_respuesta(mensaje,socket), resultado)

	def test_escribirFecha(self):
                socket = "Juanan"

                serverHoraTCP.haElegidoMenu = ["Juanan"]
                mensaje = "1"
                resultado = "La fecha es: " + time.strftime("%x")
                self.assertEqual(serverHoraTCP.generar_respuesta(mensaje,socket), resultado)
	def test_exit(self):
		socket = "Juanan"
		serverHoraTCP.haElegidoMenu = ["Juanan"]
		mensaje = "Exit"
		resultado = "Para continuar probando, Escriba nuevamente Menu"
		self.assertEqual(serverHoraTCP.generar_respuesta(mensaje, socket), resultado)

if __name__ == '__main__':
	unittest.main()
