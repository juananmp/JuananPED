class ClaseExcepcion(BaseException):
    def __init__(self, mensaje):
        pass


class Codificador (object):


    def __init__(self):
        pass


    def codificar(self, mensaje):
        mensaje_cod = mensaje.encode('utf8')
        return mensaje_cod

    def decodificar(self, mensaje_cod):
        mensaje = mensaje_cod.decode('utf8')
        return mensaje




