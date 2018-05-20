import os, sys, time

#creamos las tuberias
rd1, wd1 = os.pipe() #servidor - cliente
rd2, wd2 = os.pipe() #cliente - servidor

#file objects
r1, w1 = os.fdopen(rd1, 'rb', 0), os.fdopen(wd1, 'wb', 0) #servidor contesta
r2, w2 = os.fdopen(rd2, 'rb', 0), os.fdopen(wd2, 'wb', 0) #cliente solicita

pid = os.fork()
if (pid == 0): #proceso hijo - CLIENTE
    w1.close()
    r2.close()
    print('\n¿Me puede dar la hora por favor?\n')
    mensaje = 'solicitud'
    print('Buscando error 111')
    w2.write(bytes(mensaje,'utf8'))
    #w2.write(mensaje.encode('utf8'))
    w2.flush()
    print('Buscando error 222')
    hora = str(r1.readline())
    print('Buscando error 333')
    print('\nAhora mismo son las :'+hora +'\n')#.decode('utf8'))

elif (pid == -1):
    print('Error')

else: #proceso padre - SERVIDOR
    print('\nBuscando error')
    w2.close()
    r1.close()
    print('Buscando error 444')
    mensaje = r2.readline(9)
    print('Buscando error 555')
    if mensaje == b'solicitud':
        print('\nClaro, le mando la hora, un segundo\n')
        time.sleep(1)
        hora = time.strftime('%H %M %S')
        #w1.write(hora.encode('utf8').strip())
        w1.write(bytes(hora,'utf8'))
    	#w1.flush()
    else:
        print('\nHay un error en la solicitud\n')
