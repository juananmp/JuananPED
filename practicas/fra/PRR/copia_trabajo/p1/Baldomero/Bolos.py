class Fallo (BaseException):

    def __init__(self, mensaje):
        pass


class Partida (object):

    Rondas = 0

    def __init__(self):
        pass

    def tirarRonda(self, a,b):
        if a==10 and b==None:
            self.Rondas = self.Rondas+1
            #return a+b

        elif a+b<11 and a!=None and b!=None:
            self.Rondas = self.Rondas+1

        else:
            raise Fallo('error')


    def numeroRondas(self):
        if self.Rondas < 11 :
            return self.Rondas
        else:
            raise Fallo ('error')

    def sumaRonda(self,a,b):
        if a+b < 11 and a >= 0 and b >= 0:
            return a+b
        else:
            raise Fallo('error')

