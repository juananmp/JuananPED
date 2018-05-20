import sys, time, os

pet_fifo = 'fifo_peticiones'
resp_fifo = 'fifo_respuestas'


fichero = 'prueba.txt'



def cli():
    pet = os.open(pet_fifo,os.O_WRONLY)
    resp = os.open(resp_fifo, os.O_RDONLY)

    path =input('/home/user/Escritorio/wc/p3/Luis_F/pruebas.txt')
    os.write(pet, path.encode('utf8'))
    tam_text= os.read(resp, 1000)
    text = tam_text.decode('utf8')
    os.close(pet)
    os.close(resp)

if __name__== '__main__':
        cli()
    
