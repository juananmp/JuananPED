import unittest
from funciones import Partida, Puntuacion_erronea, Ronda_erronea, Numero_ronda_incorrecta, Ronda_strike_erroneo,Puntuacion_tras_strike_erronea,Pleno_bola2_erroneo,Puntuacion_tras_Strike_bola2_erronea

class myTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEquals(True,True)

    def test_partida_correcta(self):
        partida = Partida()
        self.assertNotEquals(partida, None)

    def test_puntuacionCorrecta(self):
        partida = Partida()
        resultado = partida.puntuacion_correcta(5,4)
        self.assertEquals(resultado,9)
    def test_partida_sin_strikes(self):
        partida = Partida()
        for i in range(10):
            partida.ronda_sin_strikes(2,4)
        resultado = partida.numero_rondas()

    def test_strike(self):
        partida=Partida()
        resultado=partida.tirar_strike(10)

    def test_puntuacion_tras_Strike(self):
        partida=Partida()
        partida.tirar_strike(10)
        with self.assertRaises(Puntuacion_tras_strike_erronea):
            resultado= partida.puntuacion_tras_Strike(3,5)

    def test_pleno_bola_2(self):
        partida=Partida()
        resultado=partida.pleno_bola_2(2,8)
        with self.assertRaises(Pleno_bola2_erroneo):
            resultado=partida.pleno_bola_2(3,5)


    def test_puntuacion_pleno_bola_2(self):
        partida=Partida()
        partida.pleno_bola_2(2,8)
        with self.assertRaises(Pleno_bola2_erroneo):
            resultado= partida.puntuacion_pleno_bola_2_anterior(3,5)



if __name__ =='__main__':
    unittest.main()