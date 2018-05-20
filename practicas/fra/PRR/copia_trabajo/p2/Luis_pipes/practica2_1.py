import os, sys, time

rd1, wd1 = os.pipe()  # sentido servidor - cliente
rd2, wd2 = os.pipe()  # sentido cliente - servidor
pid = os.fork()

if pid == 0:  # padre - servidor
    os.close
    os.close(rd1)
    mensaje = os.read(rd2, 100)
    if mensaje == "hora":
        print("Servidor: Te voy a enviar la hora")
        hora = time.strftime("%H:%M:%S")
        os.write(wd1, hora.encode('utf8'))

    elif mensaje == "fecha":
        print('Servidor: Te voy a enviar la fecha')
        fecha = time.strftime("%d/%m/%y")
        os.write(wd1, fecha.encode('utf8'))

    else:
        print("Servidor:peticion erronea")

else:  # hijo - cliente
    os.close(wd1)
    os.close(rd2)
    peticion = raw_input('Cliente: "hora" o "fecha": ')
    os.write(wd2, peticion.encode('utf8'))
    hora = os.read(rd1, 100)
    print('Cliente: la %s es  %s' % (peticion, hora.decode('utf8').strip()))
