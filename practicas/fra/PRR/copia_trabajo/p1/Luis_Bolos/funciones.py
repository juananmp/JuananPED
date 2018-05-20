class Puntuacion_erronea(BaseException):
    def __init__(self, message):
        pass

class Ronda_erronea(BaseException):
    def __init__(self,message):
        pass

class Numero_ronda_incorrecta(BaseException):
    def __init__(self, message):
        pass
class Ronda_strike_erroneo(BaseException):
    def __init__(self, message):
        pass

class Puntuacion_tras_strike_erronea(BaseException):
    def __init__(self, message):
        pass

class  Pleno_bola2_erroneo(BaseException):
    def __init__(self,message):
        pass
class Puntuacion_tras_Strike_bola2_erronea(BaseException):
    def __init__(self):
        pass

class Partida(object):
    num_ronda=0
    punt= []

    def __init__(self):
        pass

    def puntuacion_correcta(self, bola1, bola2):
        suma = bola1 + bola2
        if suma <=10:
            self.num_ronda= self.num_ronda +1
            self.punt.append([bola1, bola2])
        else:
            raise Puntuacion_erronea('Tirada no valida')
        return suma


    def ronda_sin_strikes(self, bola1,bola2):
        suma = bola1 + bola2
        if suma < 10:
            self.num_ronda = self.num_ronda + 1
            return suma
        else:
            raise Ronda_erronea('ronda no valida')


    def numero_rondas(self):
        if self.num_ronda<=10:
            return self.num_ronda
        else:
            raise Numero_ronda_incorrecta('Maximo 10')

    def tirar_strike(self, bola1):
        self.num_ronda=self.num_ronda + 1;
        if bola1 ==10:
            self.punt.append([bola1])
        else:
            raise Ronda_strike_erroneo('Tirada erronea(strike maximo 10)')

    def puntuacion_pleno_bola_2_anterior(self,bola1,bola2):
        if self.punt.__len__() - 1== 10:
            self.punt.append([bola1 + 10, bola2])
        else:
            raise Puntuacion_tras_Strike_bola2_erronea('Suma tras strike erroneo')
    def puntuacion_tras_Strike(self, bola1, bola2):
        if (self.punt.__len__()) - 1 == 10:
            self.punt.append([(bola1+10),(bola2+10)])
        else:
            raise Puntuacion_tras_strike_erronea('error tras Strike')

    def pleno_bola_2(self,bola1,bola2):
        self.num_ronda= self.num_ronda +1
        suma = bola1 + bola2
        if bola1 != 10 and suma ==10:
            self.punt.append([bola1 + bola2])
        else:
            raise Pleno_bola2_erroneo('pleno erroneo')

