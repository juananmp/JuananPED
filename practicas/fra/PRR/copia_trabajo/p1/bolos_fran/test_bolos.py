import unittest
from bolos import Partida, ClaseExcepcion

class MyTestCase (unittest.TestCase):

    def test_prueba(self):
        self.assertEqual(True, True)

    def test_existe_partida(self):
        partida = Partida()
        self.assertNotEqual(partida, None)

    def test_La_Partida_Tiene_10_Rondas (self):
        partida = Partida()
        for i in range (10):
            partida.Tirar_Ronda(0,0)
        #Genero una ronda más para hacer la partida incorrecta y que salte la excepción
        partida.Tirar_Ronda(0,0)
        with self.assertRaises(ClaseExcepcion):
            resultado = partida.Dame_Numero_Rondas()

    def test_Puntuacion_En_Tirada_Correcta (self):
        partida = Partida()
        resultado = partida.Tirar_Ronda(5, 3)
        self.assertEqual(resultado, 8)

    def test_Tirada_Incorrecta_Mas_Puntos (self):
        partida = Partida()
        with self.assertRaises(ClaseExcepcion):
            resultado = partida.Tirar_Ronda(5, 6)

    def test_Tirada_Incorrecta_Numero_Negativo(self):
        partida = Partida()
        with self.assertRaises(ClaseExcepcion):
            resultado = partida.Tirar_Ronda(-1, 5)

            #No se como hacer con cadena de caracteres
    def Tirada_Incorrecta_Cadena_Caracteres(self):
        partida = Partida()
        with self.assertRaises(ClaseExcepcion):
            resultado = partida.Tirar_Ronda('', 5)

    def test_Puntuacion_En_Partida_Correcta(self):
        partida = Partida()
        for i in range (10):
            resultado = partida.Tirar_Ronda(5,1)
        self.assertEqual(resultado, 60)

    def test_Tirada_Con_Strike (self):
        partida = Partida()
        resultado = partida.Tirar_Ronda(10, None)
        self.assertEqual(resultado,10)

    def Tirada_Con_10_Strikes (self):
        partida = Partida()
        for i in range(10):
            resultado = partida.Tirar_Ronda(10,None)
        self.assertEqual(resultado,300)

    def Puntuacion_Tirada_Con_Strike(self):
        partida = Partida()
        resultado_strike = partida.Tirar_Ronda(10,None)
        resultado = partida.Tirar_Ronda(3,2)





if __name__ == '__main__':
    unittest.main()
