import unittest
from bolosDefinitiva import puntuacion,RondaNoValida

class TestBolos (unittest.TestCase):
	def test_no_tira_ningun_bolo(self):
		partida = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado =0
		self.assertEqual(puntuacion(partida),resultado)
	def test_tiradas_aleatorios_bien(self):
		partida = [(4,0),(1,2),(2,3),(6,2),(3,6),(8,1),(9,0),(2,4),(3,4),(5,4)]
		resultado = 69
		self.assertEqual(puntuacion(partida),resultado)
	def test_Strike(self):
		partida = [(10,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = 10
		self.assertEqual(puntuacion(partida),resultado)
	def test_Spare(self):
		partida = [(5,5),(2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = 14
		self.assertEqual(puntuacion(partida),resultado)
	def test_primera_strike_y_siguiente_spare(self):
		partida = [(10,0),(5,5),(2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = 34
		self.assertEqual(puntuacion(partida),resultado)	
	def test_tres_tiradas_bien(self):
		partida = [(1,4),(10,0),(4,2),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		resultado = 27
		self.assertEqual(puntuacion(partida),resultado)	
	def test_tiradaIlegal(self):
		partida = [(13,23),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		with self.assertRaises(RondaNoValida):
			p=puntuacion(partida)	
	def test_tirada_extra_strike_en_la_ultima(self):
		partida = [(0,0),(0,0),(1,3),(2,5),(5,2),(2,0),(0,0),(0,0),(0,0),(10,0),(3,4)]
		resultado = 44
		self.assertEqual(puntuacion(partida),resultado)		

	
			
if __name__ == '__main__':
 
    unittest.main()
