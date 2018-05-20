class ClaseExcepcion (BaseException):
    def __init__(self, mensaje):
        pass

class Partida (object):

    numero_ronda = 0
    puntuacion= 0
    lista_puntuacion = []

    def __init__(self):
        pass

    def Tirar_Ronda(self, bola_1, bola_2):

        if bola_2 != None:
            suma = bola_1 + bola_2
            if suma <= 10 and bola_1 >= 0 and bola_2 >= 0:
                self.numero_ronda = self.numero_ronda + 1
                self.puntuacion = self.puntuacion + suma
                self.lista_puntuacion.append(self.puntuacion)
                return self.puntuacion
            else:
                raise ClaseExcepcion('error')

        else:
            suma = bola_1
            if bola_1 == 10:
                self.numero_ronda = self.numero_ronda + 1
                self.puntuacion = self.puntuacion + suma
                self.lista_puntuacion.append(self.puntuacion)
                return self.puntuacion
            else:
                raise ClaseExcepcion('error')


    def Dame_Numero_Rondas(self):
        if self.numero_ronda <= 10:
            return self.numero_ronda
        else:
            raise ClaseExcepcion('error')