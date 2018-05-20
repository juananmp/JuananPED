import os, sys, time

peticiones_fifo = 'fifo_peticiones'
respuestas_fifo = 'fifo_respuestas'

fichero = 'prueba_fifo.txt'
#path /home/fran/Escritorio/PRR/copia_trabajo/p3/fran_fifos/prueba_fifo.txt



def cliente():

    peticion = os.open(peticiones_fifo, os.O_WRONLY)   
         #abrimos la fifo peticiones en modo escritura
    respuesta = os.open(respuestas_fifo, os.O_RDONLY)
            #abrimos la fifo respuesta en modo lectura

    path = input ('\nIntroduzca la direccion del archivo: ')
    os.write(peticion, path.encode('utf8'))
    
    bytes_texto = os.read(respuesta, 1000)
    texto = bytes_texto.decode('utf8')
        
    print('\nEl fichero seleccionado contiene lo siguiente: \n')	
    print(texto)
    print('\n')    


    os.close(peticion)
    os.close(respuesta)




if __name__ == '__main__':
    cliente()







