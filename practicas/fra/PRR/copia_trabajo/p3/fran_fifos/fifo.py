import os, sys, time

peticiones_fifo = 'peticiones'
respuestas_fifo = 'respuestas'

if not os.path.exists(peticiones_fifo):
    os.mkfifo(peticiones_fifo)

if not os.path.exists(respuestas_fifo):
    os.mkfifo(respuestas_fifo)

pid = os.fork()

if (pid == 0): #hijo-cliente

    peticion = os.open(peticiones_fifo, os.O_WRONLY)
            #abrimos la fifo peticiones en modo escritura
    respuesta = os.open(respuestas_fifo, os.O_RDONLY)
            #abrimos la fifo respuesta en modo lectura


else:

    peticion = os.open(peticiones_fifo, os.O_RDONLY)
            #abrimos la fifo peticiones en modo lectura
    respuesta = os.open(respuestas_fifo, os.O_WRONLY)
            #abrimos la fifo respuestas en modo escritura



