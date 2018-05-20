import os, time, sys
nombre_fifo = 'prueba_fifo'

def hijo():
        fifo_escritura=os.open(nombre_fifo, os.O_WRONLY)
        hora=time.strftime("%c")
        os.write(fifo_escritura,bytes(hora,"utf8"))

hijo()


