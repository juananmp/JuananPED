import socket
import sys

#el cliente utiliza el socket de manera distinta a como lo hace el servidor, en lugar de unirse al puerto para escuchar conexiones, utiliza el connect() para fijar la conexion remota

#creando socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 10001)
print (sys.stderr, 'conectando a %s puerto %s' % server_address)
sock.connect(server_address)
#Después que la conexión esté establecida, la información puede ser enviada con el método sendall() y recibida con el método recv(), igual que el servidor. 

try:
     
    # Enviando datos
 #   message = ('Este es el mensaje.  Se repitio.', 'utf8')
    print (sys.stderr, 'enviando ')
    sock.sendall(bytes('juanan','utf8'))
 
    # Buscando respuesta
    amount_received = 0
   # amount_expected = len(message)
     
    while amount_received < amount_expected:
        data = sock.recv(19)
        amount_received += len(data)
        print(sys.stderr, 'recibiendo', data)
 
finally:
    print (sys.stderr, 'cerrando socket')
    sock.close()
