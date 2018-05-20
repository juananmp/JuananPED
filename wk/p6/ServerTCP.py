import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#con bind asociamos la direccion del servidor al socket

server_address  = ('localhost',10001)
print(sys.stderr, 'empezando a levantar %s puerto %s ', server_address)
sock.bind(server_address)
# accept --> acepta una conexion entrante de un cliente 
#listen pone al socket en modo servidor

sock.listen(1)

while True:
    print(sys.stderr, 'Esperando para conectarse')
    connection, client_address = sock.accept()
    # accept nos devuelve una conexion abierta entre el servidor y el cliente, junto con la direccion del cliente. Los datos de la conexion se leen con el metodo recv() y se transmiten con el metodo sendall()
    try:
        print (sys.stderr, 'concexion desde', client_address)
         # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(19)
            print (sys.stderr, 'recibido', data)
            if data:
                print (sys.stderr, 'enviando mensaje de vuelta al cliente')
                connection.sendall(data)
            else:
                print (sys.stderr, 'no hay mas datos', client_address)
                break
             
    finally:
    # Cerrando conexion
        connection.close()
