import os, time, sys
nombre_fifo = 'prueba_fifo'
def hijo():
    fifo_escritura = os.open(nombre_fifo, os.O_WRONLY)
    numero = 0
    #file = open('Texto', 'r')
    #str = file.read()
    #list = list(str)
    #print list
    while True:
        time.sleep(1)
        os.write(fifo_escritura, 'Contador %03d\n' % numero)
        numero = (numero+1) % 5
def padre():
    fifo_lectura = open(nombre_fifo, 'r')
    while True:
        dato = fifo_lectura.readline()[:-1]
        print 'Numero %s' % (dato)
if not os.path.exists(nombre_fifo):
    os.mkfifo(nombre_fifo)
if os.fork() == 0:
    hijo()
else:
    padre()