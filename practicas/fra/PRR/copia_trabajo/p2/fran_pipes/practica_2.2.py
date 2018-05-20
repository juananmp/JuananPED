
import os, sys, time

#Creamos las tuberias
r1, w1 = os.pipe() #servidor - cliente
r2, w2 = os.pipe() #cliente - servidor


pid = os.fork()

if (pid == 0): #hijo - cliente
	os.close(w1)
	os.close(r2)
	solicitud = input ('\nQué desea consultar, la -hora- o la -fecha-: ')
	os.write(w2, solicitud.encode('utf8'))
	mensaje = os.read(r1,50)
	print('Usted ha solicitado la %s, y aqui tiene su solicitud %s \n\n' % (solicitud, mensaje.decode('utf8')))

else: #padre - servidor
	os.close(w2)
	os.close(r1)
	solicitud = os.read(r2,50)
	#print(solicitud)
	#time.sleep(3)
	if solicitud==b'hora':
		print('consultando la hora al servidor...\n')
		time.sleep(2)
		hora = time.strftime('%H %M %S')
		os.write(w1, hora.encode('utf8'))
	elif solicitud==b'fecha':
		print('consultando la fecha al servidor...\n')
		time.sleep(2)
		fecha = time.strftime('%d - %m - %y')
		os.write(w1, fecha.encode('utf8'))
	else:
		print('Lo que pide no podemos facilitarselo')
		
		
