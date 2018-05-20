import unittest
import python_bolos

class TestPython(unittest.TestCase):
	
	#Primer test 1 partida de bolos tiene 10 tiradas/rondas
	def test_que_compruebe_diez_tiradas(self):
	    self.assertEqual(10, python_bolos.get_number(10))

if __name__ == '__main__': 
        unittest.main()
