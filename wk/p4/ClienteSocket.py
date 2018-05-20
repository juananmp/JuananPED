import socket
import sys
import os

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX)

# Connect the socket to the port where the server is listening
server_address = './socket'
print('connecting to {}'.format(server_address))


try:
    sock.connect(server_address)
    mensaje = input("Abrir archivo: \n")
    sock.send(mensaje.encode('utf8'))
    rec = sock.recv(1024).decode('utf8')
    
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:
    while rec != "":
       # rec = mensaje.decode('utf8')
        sys.stdout.write(rec)
        sys.stdout.flush()
        rec = sock.recv(1024)
    

finally:
    print('closing socket')
    sock.close()
