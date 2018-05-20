import socket, sys, os , time


server_address = raw_input('Introduzca ruta a la que el servidor se conectara:')


try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sock.bind(server_address)

sock.listen(1)

while True:
    print('Esperando conexiones')
    sock_intercambio, client_address = sock.accept() 
    print >>sys.stderr, 'Conectado con: ', client_address
    peticion = sock_intercambio.recv(100)
        
    print >>sys.stderr, 'Recibida peticion: "%s"' % peticion
    
    if peticion == 'Dame hora': 
        print >>sys.stderr, 'Enviando hora al cliente'
        hora = time.ctime()
       	sock_intercambio.send(hora)
    else:
        print >>sys.stderr, 'Servidor no entiende peticion'
        break
            
   	sock_intercambio.close()

