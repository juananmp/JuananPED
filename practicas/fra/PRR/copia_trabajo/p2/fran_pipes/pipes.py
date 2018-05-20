import os, sys, time

rd,wd = os.pipe()
r, w = os.fdopen(rd, 'rb', 0), os.fdopen(wd, 'wb', 0)

pid = os.fork()

if (pid == 0):
    print('if')
    r.close()
    #time.sleep(5)
    for i in range(10):
        print('bucle for')
        mensaje = 'linea %d \n' %i
        w.write(mensaje.encode('utf8'))
        w.flush()
        #Podemos comentar la siguiente linea y observamos el comportamiento, ayuda a entender el ejercicio
        time.sleep(1)
    print('Soy el hijo \n')

if (pid == -1):
    print ('Error')

else:
    print('else')
    w.close()
    while True:
        print('while True')
        data = r.readline()
        print('data')
        if not data:
            print('No hay mas lineas que leer \n')
            break
        print('El padre lee: '+ data.decode('utf8'))#.strip())
    print('soy el padre \n')