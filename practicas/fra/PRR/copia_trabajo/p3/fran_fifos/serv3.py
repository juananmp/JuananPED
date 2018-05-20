import os, sys, time

peticiones_fifo = 'fifo_peticiones'
respuestas_fifo = 'fifo_respuestas'

if not os.path.exists(peticiones_fifo):
    os.mkfifo(peticiones_fifo)

if not os.path.exists(respuestas_fifo):
    os.mkfifo(respuestas_fifo)

def servidor():
    peticion = os.open(peticiones_fifo, os.O_RDONLY)
            #abrimos la fifo peticiones en modo lectura
    respuesta = os.open(respuestas_fifo, os.O_WRONLY)
            #abrimos la fifo respuestas en modo escritura

    fichero_pedido = os.read(peticion,2000)
    fichero = os.open(fichero_pedido, os.O_RDONLY)

    leer = os.read(fichero,1000)

    os.write(respuesta, leer)
    
    os.close(fichero)
    os.close(peticion)
    os.close(respuesta)





if __name__ == '__main__':
	servidor()
