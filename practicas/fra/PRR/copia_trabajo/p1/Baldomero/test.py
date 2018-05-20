
import unittest
from Bolos import Partida, Fallo


class MyTestCase (unittest.TestCase):

    def test_prueba(self):
        self.assertEquals(True , True)

    def test_exixtencia(self):
        p = Partida()
        self.assertNotEquals(p , None)

    def test_NumeroRondasCorrecto(self):
        p = Partida()
        for i in range (10):
            p.tirarRonda(0, 0)
        p.tirarRonda(0, 0)
        with self.assertRaises(Fallo):
            resultado = p.numeroRondas()
        #self.assertEqual(resultado,10)

    def test_PuntuacionCorrectaRonda(self):
        p = Partida()
        #p.tirarRonda(1,2)
        resultado = p.sumaRonda(1,1)
        self.assertEqual(resultado, 2)

    def test_PuntuacionPartida(self):
        p = Partida()
        puntuacion = 0
        for i in range (10):
            #p.tirarRonda(1, 2)
            resultado = p.sumaRonda(1,2)
            puntuacion = puntuacion + resultado

        self.assertEqual(puntuacion, 30)

    def test_PuntuacionIncorrectaRonda1(self):
        p = Partida()
        with self.assertRaises(Fallo):
            p.sumaRonda(6, 5)

    def test_PuntuacionIncorrectaRonda2(self):
        p = Partida()
        with self.assertRaises(Fallo):
            p.sumaRonda(-1, 5)














if __name__ == '__main__':
    unittest.main()
