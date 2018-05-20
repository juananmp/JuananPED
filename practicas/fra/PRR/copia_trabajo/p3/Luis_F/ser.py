import sys, os, time


pet_fifo = 'fifo_peticiones'
resp_fifo = 'fifo_respuestas'

if not os.path.exists(pet_fifo):
    os.mkfifo(pet_fifo)

if not os.path.exists(resp_fifo):
    os.mkfifo(resp_fifo)


def serv():

    pet=os.open(pet_fifo,os.O_RDONLY)
    resp= os.open(resp_fifo, os.O_WRONLY)

    fich= os.read(pet, 2000)
    fich2 =os.open(fich, os.O_RDONLY)

    lectura= os.read(fich2,1000)

    os.write(resp,lectura)
    os.close(fich2)
    os.close(pet)
    os.close(resp)

if __name__=='__main__':
    serv()