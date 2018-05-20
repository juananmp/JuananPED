import unittest
from modulo import Codificador, ClaseExcepcion

class MuTestCase(unittest.TestCase):

    def test_prueba(self):
        self.assertEqual(True,True)

    def test_existe_modulo(self):
        c = Codificador()
        self.assertNotEqual(c, None)

    def test_codificar_palabra(self):
        c = Codificador()
        mensaje = 'hola'
        mensaje_cod = c.codificar(mensaje)
        self.assertEqual(mensaje_cod, b'hola' )

    def test_codificador_numeros(self):
        c= Codificador()
        numero = '123456'
        numero_cod = c.codificar(numero)
        self.assertEqual(numero_cod, b'123456')

    def test_decodificar_palabra(self):
        c = Codificador()
        mensaje_cod = b'chao'
        mensaje = c.decodificar(mensaje_cod)
        self.assertEqual(mensaje, 'chao')

    def test_decodificar_numero(self):
        c = Codificador()
        numero_cod = b'123456'
        numero = c.decodificar(numero_cod)
        self.assertEqual(numero, '123456')



if __name__ == '__main__':
    unittest.main()
