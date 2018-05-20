import os, sys, socket
cerobytes=b""
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
s.connect(('0.0.0.0',4079))

conver = input("<Introduce lo que quieras: ")
s.send(bytes(conver,"utf8"))
datos = b"entra"
while datos != cerobytes:

    datos=s.recv(100000)
    print(datos)
s.close()

