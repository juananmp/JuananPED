import os, time, sys

nombre_fifo = 'prueba_fifo'

def padre():
    fifo_lectura=open(nombre_fifo,'r')
    dato=fifo_lectura.readline()
    print(dato)

padre()
