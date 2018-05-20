import socket
#creo objeto socket
s = socket.socket()


#en que puerto se va a mantener a la espera el servidor, usamos bind para ello
s.bind(("localhost", 9999))
#listen--> de esta forma hacemos que el socket acepte conexiones,parametro es numero de condiciones maximas que queremos aceptar (al menos 1)
#accept --> para comenzar a escuchar, se mantiene a la espera de conexiones
s.listen(1)

sc, addr = s.accept()
#cliente usa metodos recv y send para recibir y enviar mensajes 
#recv --> toma como parametro el numero maximo de parametros a aceptar
#send --> toma como parametro los datos a enviar
while True:
#la ejecucion terminara cuando el usuario escriba quit
      recibido = sc.recv(1024)
      reci = recibido.decode()  
      if reci == "quit":  
         break        
      print ("Recibido:", reci)
 
#      sc.send(reci)  
  
print ("adios")  

sc.close()
s.close()

